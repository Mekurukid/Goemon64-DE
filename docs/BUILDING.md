# Build-Hinweise

## Release v0.8.5

Der veröffentlichte Beta-v0.8.5-Build verwendet neben der reinen Übersetzung auch einen erweiterten Text-Repack- und Formatierungsdurchlauf. Dieser erhält unter anderem Farbzustände, Klammern/Satzzeichen sowie Portrait-Textbox-Einrückungen und kann längere deutsche Texte innerhalb sicherer ROM-Textpools neu anordnen.

Die **autoritativen fertigen Dateien** sind deshalb die Assets des GitHub-Releases:

- `Goemon64-DE-Beta-v0.8.5.nrm`
- `Goemon64-DE-Beta-v0.8.5.bps`
- `SHA256SUMS-v0.8.5.txt`

## Übersetzungsquellen

Im Repository liegen:

- `translations/de_DE.json` – deutscher Textstand
- `translations/color_map.json` – semantische Zuordnung der Original-Farbspannen
- `translations/ascii_ui.json` – zusätzliche UI-/ASCII-Patches

## Legacy-Builder

`tools/build_mod.py` stammt aus einem früheren Entwicklungsstand und ist weiterhin als technische Referenz enthalten. Er bildet **nicht** alle Formatierungs-/Repack-Schritte von Beta v0.8.5 ab und soll daher nicht zur Erzeugung eines byteidentischen v0.8.5-Releases verwendet werden.

## ROM-Sicherheit

Keine `.n64`, `.z64` oder `.v64` ins Repository committen. Die ROM bleibt immer Eigentum des Nutzers und wird nicht mit diesem Projekt verteilt.
