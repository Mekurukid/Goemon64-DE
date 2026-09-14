# GitHub einrichten – Schritt für Schritt

## Empfohlener Repository-Name

`Goemon64-DE`

## Beschreibung für das GitHub-Feld „Description“

`Deutsche Fan-Übersetzung für Mystical Ninja Starring Goemon – für Goemon 64: Recompiled.`

## Empfohlene Topics

`goemon`, `mystical-ninja`, `nintendo-64`, `n64`, `n64recomp`, `goemon64-recompiled`, `german`, `translation`, `fan-translation`, `nrm`, `bps`

## Repository erstellen

1. Bei GitHub anmelden.
2. Oben rechts auf **+ → New repository** klicken.
3. Repository-Name: `Goemon64-DE`.
4. Beschreibung aus diesem Dokument eintragen.
5. **Public** auswählen.
6. **Kein** zusätzliches README, `.gitignore` oder License von GitHub erzeugen lassen, weil diese Dateien bereits vorbereitet sind.
7. **Create repository** klicken.

## Dateien hochladen – einfache Browser-Methode

1. Im neuen Repository auf **uploading an existing file** oder **Add file → Upload files** klicken.
2. Den **Inhalt des Ordners `repository/`** aus dem vorbereiteten Paket hochladen.
3. Kontrollieren, dass keine `.n64`, `.z64` oder `.v64` dabei ist.
4. Commit-Nachricht: `Initial release of Goemon64 DE`.
5. **Commit changes** klicken.

## Release v0.2.0 erstellen

1. Rechts im Repository bei **Releases** auf **Create a new release** klicken.
2. **Choose a tag** → neuen Tag `v0.2.0-beta` erstellen.
3. Release title: `Goemon64 DE – Beta v0.2.0`.
4. Den Inhalt aus `RELEASE-NOTES-v0.2.0.md` in die Beschreibung kopieren.
5. Aus dem Paketordner `release-assets/v0.2.0/` diese Dateien anhängen:
   - `Goemon64-DE-Beta-v0.2.0.nrm`
   - optional `Goemon64-DE-Beta-v0.2.0.bps`
   - `SHA256SUMS.txt`
6. **Set as a pre-release** aktivieren, weil es eine Beta ist.
7. **Publish release** klicken.

## Nach dem Upload

1. Unter **About** die Beschreibung setzen.
2. Die empfohlenen Topics hinzufügen.
3. Unter **Issues** prüfen, ob Issues aktiviert sind.
4. Optional **Discussions** aktivieren, falls du Feedback sammeln möchtest.
5. Niemals eine ROM als Release-Asset oder Repository-Datei hochladen.
