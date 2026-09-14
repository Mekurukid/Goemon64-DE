# Mod selbst bauen

Diese Anleitung erstellt die `.nrm`-Mod aus deiner **eigenen** US-ROM. Die ROM wird nicht in das Repository kopiert.

## Voraussetzungen

- Python 3.10 oder neuer
- eigene US-ROM von *Mystical Ninja Starring Goemon*
- dieses Repository

Es werden keine zusätzlichen Python-Pakete benötigt.

## Build

Im Repository ausführen:

```bash
python3 tools/build_mod.py \
  --rom "/pfad/zu/Mystical Ninja Starring Goemon (USA).n64" \
  --translation translations/de_DE.json \
  --output-dir dist
```

Unter Linux/Nobara kann ein Beispiel so aussehen:

```bash
python3 tools/build_mod.py \
  --rom "$HOME/Spiele/ROMs/Mystical Ninja Starring Goemon (USA).n64" \
  --translation translations/de_DE.json \
  --output-dir dist
```

## Ausgabe

Im Ordner `dist/` entstehen:

- `Goemon64-DE-Beta-v0.2.0.nrm`
- `Goemon64-DE-Beta-v0.2.0.bps`
- `build-report.txt`

## Unterstützte ROM-Byte-Reihenfolge

Der Builder erkennt automatisch:

- `.z64` – Big-Endian
- `.n64` – Little-Endian / word-swapped
- `.v64` – byte-swapped

Anschließend wird intern auf die erwartete Big-Endian-US-ROM normalisiert.

## ROM-Prüfung

Der Builder akzeptiert die bekannte US-Basis mit normalisiertem SHA-256:

`1603be37427a33548857fc3d2e8867ede71121c353fb631b79b44f1d94845d80`

Bei einer anderen ROM-Version bricht der Build ab, damit nicht versehentlich ein inkompatibler Patch erzeugt wird.

## Sicherheit

Committe niemals den `dist/`-Ordner zusammen mit einer ROM und entferne niemals die ROM-Regeln aus `.gitignore`, wenn du nicht genau weißt, was du tust.
