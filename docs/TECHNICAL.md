# Technische Informationen

## Mod-Format

Die Release-Datei ist eine `.nrm` und enthält:

- `mod.json`
- `patch.bps`

Es wird keine ROM in der Mod gespeichert.

## Version v0.2.0

- Mod-ID: `goemon64_de_beta_v020`
- Game-ID: `mnsg`
- Mindestversion laut Manifest: `0.2.0-dev`
- Übersetzungseinträge: **927**
- Textreferenzen bei QA: **5.393**
- Scriptfehler bei QA: **0**
- unbekannte Zeichen bei QA: **0**

## Unterstützte ROM-Basis

Normalisierte US-ROM (Big-Endian / z64):

- SHA-256: `1603be37427a33548857fc3d2e8867ede71121c353fb631b79b44f1d94845d80`

Der Builder akzeptiert unterschiedliche N64-Byte-Reihenfolgen, normalisiert die Datei intern und prüft anschließend diesen Hash.

## Dekomprimierte Basis

- Größe: `33554432` Bytes (`32 MiB`)
- SHA-1: `6ea0ed71032ce08fc2745f412d84936382197494`

## Ziel von Beta v0.2.0

- SHA-1: `d89bc4702a551f0d049311c5fb95efd1b60ae6ac`

## Release-Patch

- BPS SHA-256: `8d516fc9459f1cbe28fee1b9e114b97c09cec20ed4129b7481f9acc824ceb351`

Die aktuelle GitHub-Paketversion baut die `.nrm` deterministisch. Die genaue `.nrm`-Prüfsumme steht in `SHA256SUMS.txt` des jeweiligen Releases.
