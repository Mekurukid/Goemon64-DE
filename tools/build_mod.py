#!/usr/bin/env python3
"""Build Goemon64 DE without distributing a ROM.

Usage:
  python3 tools/build_mod.py --rom game.n64 --translation translations/de_DE.json --output-dir dist
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import zlib
import zipfile
from pathlib import Path

VERSION = "0.2.0"
EXPECTED_Z64_SHA256 = "1603be37427a33548857fc3d2e8867ede71121c353fb631b79b44f1d94845d80"
EXPECTED_DECOMP_HEADER_CRC = bytes.fromhex("9cc11f4babaa8538")
FILE_TABLE = 0x57FD8
MESSAGE_POINTER_TABLE = 0x785A0
MESSAGE_FILE_TABLE = 0x79208
MESSAGE_COUNT = 794

ENC = {
    " ": 0x0000, "!": 0x0001, '"': 0x0002, "'": 0x0007,
    "(": 0x0008, ")": 0x0009, ",": 0x000C, "-": 0x000D,
    ".": 0x000E, "/": 0x000F, ":": 0x001A, "?": 0x001F,
    "[": 0x003B, "]": 0x003D,
}
for i, ch in enumerate("0123456789"):
    ENC[ch] = 0x0010 + i
for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    ENC[ch] = 0x0021 + i
for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
    ENC[ch] = 0x0041 + i

TOK = {
    "end": 0xFFB9,
    "begin": 0xFFBA,
    "newwindow": 0xFFC1,
    "waitinput": 0xFFC2,
    "button": 0xFFC3,
    "newline": 0xFFC4,
    "endline": 0xFFFF,
}
STRUCTURAL_TOKENS = set(TOK)

DEC = {
    0x0000: " ", 0x0001: "!", 0x0002: '"', 0x0007: "'",
    0x0008: "(", 0x0009: ")", 0x000C: ",", 0x000D: "-",
    0x000E: ".", 0x000F: "/", 0x001A: ":", 0x001F: "?",
    0x003B: "[", 0x003D: "]",
}
for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
    DEC[0x41 + i] = ch
for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    DEC[0x21 + i] = ch
for i, ch in enumerate("0123456789"):
    DEC[0x10 + i] = ch
DEC.update({
    0xFFB9: "{end}", 0xFFBA: "{begin}", 0xFFC1: "{newwindow}",
    0xFFC2: "{waitinput}", 0xFFC3: "{button}", 0xFFC4: "{newline}",
    0xFFC7: "{/big}", 0xFFC8: "{big}", 0xFFCD: "{/blink}",
    0xFFCE: "{blink}", 0xFFDB: "{unknown-ffdb}", 0xFFDC: "{em-green}",
    0xFFDD: "{em-blue}", 0xFFDE: "{em-red}", 0xFFDF: "{em-yellow}",
    0xFFE0: "{/em}", 0xFFFF: "{endline}",
})

SCRIPT_PARAM_LENGTH = {
    0x8002: 4, 0x8003: 4, 0x8004: 4, 0x8006: 4, 0x8008: 0,
    0x8009: 4, 0x800A: 4, 0x800B: 4, 0x800C: 4, 0x8010: 4,
    0x8011: 0, 0x8012: 0, 0x8013: 4, 0x8015: 4, 0x8017: 4,
    0x8020: 4, 0x8021: 4, 0x8022: 8, 0x8030: 4,
}


def be32(buf: bytes | bytearray, off: int) -> int:
    return int.from_bytes(buf[off:off + 4], "big")


def wr32(buf: bytearray, off: int, value: int) -> None:
    buf[off:off + 4] = value.to_bytes(4, "big")


def normalize_rom(data: bytes) -> bytes:
    magic = data[:4]
    if magic == bytes.fromhex("80371240"):  # z64
        return data
    if magic == bytes.fromhex("37804012"):  # v64 byte-swapped
        out = bytearray(len(data))
        for i in range(0, len(data), 2):
            out[i:i + 2] = data[i:i + 2][::-1]
        return bytes(out)
    if magic == bytes.fromhex("40123780"):  # n64 little-endian words
        out = bytearray(len(data))
        for i in range(0, len(data), 4):
            out[i:i + 4] = data[i:i + 4][::-1]
        return bytes(out)
    raise ValueError("Unbekanntes N64-ROM-Byteformat.")


def decompress_chunk(data: bytes) -> bytes:
    comp = int.from_bytes(data[:4], "big")
    ip = 4
    out = bytearray()
    if comp > len(data):
        raise ValueError("Ungueltige komprimierte Datei.")
    while ip < comp:
        cmd = data[ip]
        ip += 1
        if cmd <= 0x7F:
            ln = ((cmd & 0x7C) >> 2) + 2
            off = (((cmd & 0x03) << 8) | data[ip]) & 0x3FF
            ip += 1
            if off == 0 or off > len(out):
                raise ValueError("Ungueltiger Backreference-Offset.")
            for _ in range(ln):
                out.append(out[-off])
        elif cmd <= 0x9F:
            ln = cmd & 0x1F
            out.extend(data[ip:ip + ln])
            ip += ln
        elif cmd <= 0xDF:
            ln = (cmd & 0x1F) + 2
            val = data[ip]
            ip += 1
            out.extend(bytes([val]) * ln)
        elif cmd <= 0xFE:
            ln = (cmd & 0x1F) + 2
            out.extend(b"\0" * ln)
        else:
            ln = data[ip] + 2
            ip += 1
            out.extend(b"\0" * ln)
    return bytes(out)


def decompress_rom(rom: bytes) -> bytes:
    ret = bytearray(0x4000000)
    ret[:len(rom)] = rom
    inoff = FILE_TABLE
    outoff = FILE_TABLE
    rom_offset = be32(rom, inoff) & 0x7FFFFFFF
    while be32(rom, inoff) != 0 and be32(rom, inoff + 4) != 0:
        a = be32(rom, inoff)
        b = be32(rom, inoff + 4)
        compressed = (a >> 31) & 1
        fileoff = a & 0x7FFFFFFF
        filesize = (b & 0x7FFFFFFF) - fileoff
        blob = decompress_chunk(rom[fileoff:fileoff + filesize]) if compressed else rom[fileoff:fileoff + filesize]
        ret[rom_offset:rom_offset + len(blob)] = blob
        aligned = (len(blob) + 0xF) & ~0xF
        wr32(ret, outoff, rom_offset)
        wr32(ret, outoff + 4, rom_offset + aligned)
        rom_offset += aligned
        inoff += 4
        outoff += 4
    final = 1 << (rom_offset - 1).bit_length()
    ret = ret[:final]
    wr32(ret, 0x10, 0x9CC11F4B)
    wr32(ret, 0x14, 0xABAA8538)
    return bytes(ret)


def decode_text(blob: bytes, p: int) -> tuple[str, int, list[int]]:
    out: list[str] = []
    unknown: list[int] = []
    start = p
    for _ in range(10000):
        if p + 2 > len(blob):
            break
        c = int.from_bytes(blob[p:p + 2], "big")
        p += 2
        if c in DEC:
            out.append(DEC[c])
        else:
            out.append(f"{{char-{c:04x}}}")
            unknown.append(c)
        if c == 0xFFFF:
            return "".join(out), p - start, unknown
    raise ValueError(f"Unterminierter Text bei 0x{start:X}")


def extract_text_records(data: bytes) -> tuple[list[dict], list[dict]]:
    def file_blob(fi: int) -> tuple[int, int, bytes]:
        s = be32(data, FILE_TABLE + (fi - 1) * 4) & 0x7FFFFFFF
        e = be32(data, FILE_TABLE + fi * 4) & 0x7FFFFFFF
        return s, e, data[s:e]

    def parse_script(blob: bytes, p: int, seen: set[int], out: list[dict], msg: int, fi: int) -> None:
        if p in seen or not (0 <= p < len(blob) - 4):
            return
        seen.add(p)
        start = p
        for _ in range(10000):
            if p + 4 > len(blob):
                break
            op = int.from_bytes(blob[p:p + 4], "big")
            q = p + 4
            if op not in SCRIPT_PARAM_LENGTH:
                out.append({"message": msg, "file": fi, "script": start, "instruction": p, "error": f"unknown opcode {op:08x}"})
                return
            ln = SCRIPT_PARAM_LENGTH[op]
            if q + ln > len(blob):
                return
            arg = blob[q:q + ln]
            if op == 0x8010:
                tp = int.from_bytes(arg[1:4], "big")
                try:
                    text, size, unknown = decode_text(blob, tp)
                except Exception as exc:
                    text, size, unknown = f"[[DECODE ERROR {exc}]]", 0, []
                out.append({
                    "message": msg, "file": fi, "script": start,
                    "instruction": p, "text_pointer": tp,
                    "text_size": size, "prefix": arg[0],
                    "text": text, "unknown_chars": unknown,
                })
            if op == 0x800A:
                parse_script(blob, int.from_bytes(arg[-3:], "big"), seen, out, msg, fi)
            elif op == 0x8022:
                parse_script(blob, int.from_bytes(arg[-3:], "big"), seen, out, msg, fi)
            p = q + ln
            if op == 0x8008:
                return

    records: list[dict] = []
    per_file_seen: dict[int, set[int]] = {}
    for i in range(MESSAGE_COUNT):
        rec = data[MESSAGE_POINTER_TABLE + i * 4:MESSAGE_POINTER_TABLE + i * 4 + 4]
        ptr = int.from_bytes(rec[1:], "big")
        fi = int.from_bytes(data[MESSAGE_FILE_TABLE + i * 2:MESSAGE_FILE_TABLE + i * 2 + 2], "big")
        if not fi or not ptr:
            continue
        _, _, blob = file_blob(fi)
        parse_script(blob, ptr, per_file_seen.setdefault(fi, set()), records, i, fi)

    texts: dict[tuple[int, int], dict] = {}
    errors: list[dict] = []
    for r in records:
        if "text" not in r:
            errors.append(r)
            continue
        key = (r["file"], r["text_pointer"])
        if key not in texts:
            x = dict(r)
            x["messages"] = [r["message"]]
            texts[key] = x
        elif r["message"] not in texts[key]["messages"]:
            texts[key]["messages"].append(r["message"])
    return sorted(texts.values(), key=lambda r: (r["file"], r["text_pointer"])), errors


def structural_tokens(original: str) -> list[str]:
    return [t for t in re.findall(r"\{([^}]+)\}", original) if t in STRUCTURAL_TOKENS]


def encode_visible(original: str, new: str) -> bytes:
    toks = structural_tokens(original)
    seq: list[int] = [TOK[t] for t in toks if t == "begin"]
    for ch in new:
        if ch not in ENC:
            raise ValueError(f"Nicht unterstuetztes Zeichen {ch!r} in: {new!r}")
        seq.append(ENC[ch])
    seq.extend(TOK[t] for t in toks if t != "begin")
    return b"".join(x.to_bytes(2, "big") for x in seq)


def bps_num(n: int) -> bytes:
    out = bytearray()
    while True:
        x = n & 0x7F
        n >>= 7
        if n == 0:
            out.append(0x80 | x)
            break
        out.append(x)
        n -= 1
    return bytes(out)


def make_bps(src: bytes, tgt: bytes) -> bytes:
    out = bytearray(b"BPS1")
    out += bps_num(len(src)) + bps_num(len(tgt)) + bps_num(0)
    i = 0
    while i < len(tgt):
        if src[i] == tgt[i]:
            j = i + 1
            while j < len(tgt) and src[j] == tgt[j]:
                j += 1
            out += bps_num(((j - i - 1) << 2) | 0)
            i = j
        else:
            j = i + 1
            while j < len(tgt) and src[j] != tgt[j]:
                j += 1
            lit = tgt[i:j]
            out += bps_num(((len(lit) - 1) << 2) | 1)
            out += lit
            i = j
    out += struct.pack("<I", zlib.crc32(src) & 0xFFFFFFFF)
    out += struct.pack("<I", zlib.crc32(tgt) & 0xFFFFFFFF)
    out += struct.pack("<I", zlib.crc32(out) & 0xFFFFFFFF)
    return bytes(out)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Goemon64 DE .nrm from your own US ROM")
    ap.add_argument("--rom", required=True, type=Path, help="Path to your own US ROM (.z64/.n64/.v64)")
    ap.add_argument("--translation", default=Path("translations/de_DE.json"), type=Path)
    ap.add_argument("--output-dir", default=Path("dist"), type=Path)
    args = ap.parse_args()

    raw = args.rom.read_bytes()
    z64 = normalize_rom(raw)
    z64_sha = hashlib.sha256(z64).hexdigest()
    if z64_sha != EXPECTED_Z64_SHA256:
        raise SystemExit(
            "Nicht unterstuetzte ROM. Erwarteter normalisierter SHA-256:\n"
            f"  {EXPECTED_Z64_SHA256}\nGefunden:\n  {z64_sha}"
        )

    src = decompress_rom(z64)
    if len(src) != 0x2000000 or src[0x10:0x18] != EXPECTED_DECOMP_HEADER_CRC:
        raise SystemExit("Die dekomprimierte ROM entspricht nicht der erwarteten 32-MiB-Basis.")

    items, script_errors = extract_text_records(src)
    if len(items) != 5393:
        raise SystemExit(f"Unerwartete Texttabellen: {len(items)} statt 5393 Eintraege.")
    if script_errors:
        raise SystemExit(f"Skriptfehler in der Basis-ROM: {len(script_errors)}")

    translations = {int(k): v for k, v in json.loads(args.translation.read_text(encoding="utf-8")).items()}
    tgt = bytearray(src)
    changed_records = 0
    for idx, new in sorted(translations.items()):
        if not (0 <= idx < len(items)):
            raise SystemExit(f"Ungueltige Text-ID in translation JSON: {idx}")
        r = items[idx]
        fi = int(r["file"])
        file_start = be32(src, FILE_TABLE + (fi - 1) * 4) & 0x7FFFFFFF
        enc = encode_visible(r["text"], new)
        cap = int(r["text_size"])
        if len(enc) > cap:
            raise SystemExit(f"Text {idx} ist zu lang: {len(enc)}>{cap}: {new!r}")
        off = file_start + int(r["text_pointer"])
        replacement = enc + b"\x00" * (cap - len(enc))
        if bytes(tgt[off:off + cap]) != replacement:
            changed_records += 1
        tgt[off:off + cap] = replacement

    if tgt[:0x1000] != src[:0x1000]:
        raise SystemExit("Header wurde unerwartet veraendert.")

    patched_items, patched_errors = extract_text_records(bytes(tgt))
    unknown = sorted({c for r in patched_items for c in r.get("unknown_chars", [])})
    if len(patched_items) != 5393 or patched_errors or unknown:
        raise SystemExit(
            f"QA fehlgeschlagen: refs={len(patched_items)}, errors={len(patched_errors)}, unknown={unknown}"
        )

    patch = make_bps(src, bytes(tgt))
    manifest = {
        "game_id": "mnsg",
        "id": "goemon64_de_beta_v020",
        "version": VERSION,
        "display_name": "Deutsche Uebersetzung (Beta v0.2.0)",
        "description": "Deutsche Fan-Uebersetzung fuer Mystical Ninja Starring Goemon. Beta v0.2.0 uebersetzt Systemtexte, Gegenstaende, erste Storyszenen und den fruehen Oedo-Stadt-Dialogblock.",
        "short_description": "Deutsche Fan-Uebersetzung - erweiterter Oedo-Startbereich",
        "authors": ["Mekurukid"],
        "minimum_recomp_version": "0.2.0-dev",
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    bps_path = args.output_dir / "Goemon64-DE-Beta-v0.2.0.bps"
    nrm_path = args.output_dir / "Goemon64-DE-Beta-v0.2.0.nrm"
    report_path = args.output_dir / "build-report.txt"
    bps_path.write_bytes(patch)
    with zipfile.ZipFile(nrm_path, "w", compression=zipfile.ZIP_STORED) as zf:
        manifest_bytes = (json.dumps(manifest, ensure_ascii=True, indent=2) + "\n").encode("utf-8")
        for name, payload in (("mod.json", manifest_bytes), ("patch.bps", patch)):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, payload)

    report = [
        "Goemon64 DE build report",
        "",
        f"Version: {VERSION}",
        f"ROM normalized SHA256: {z64_sha}",
        f"Decompressed source SHA1: {hashlib.sha1(src).hexdigest()}",
        f"Target SHA1: {hashlib.sha1(tgt).hexdigest()}",
        f"Translation records: {len(translations)}",
        f"Records that changed bytes: {changed_records}",
        f"Text references: {len(patched_items)}",
        f"Script errors: {len(patched_errors)}",
        f"Unknown chars: {len(unknown)}",
        f"BPS SHA256: {hashlib.sha256(patch).hexdigest()}",
        f"NRM SHA256: {hashlib.sha256(nrm_path.read_bytes()).hexdigest()}",
        "",
        "PASS",
    ]
    report_path.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    print(f"\nNRM: {nrm_path}")


if __name__ == "__main__":
    main()
