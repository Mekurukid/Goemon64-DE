# Mithelfen

Danke für dein Interesse an **Goemon64 DE**.

## Übersetzungsfehler melden

Am einfachsten ist ein GitHub-Issue über die Vorlage **Übersetzungsfehler**.

Bitte nenne möglichst:

1. Mod-Version
2. Ort / Szene
3. NPC, Menü oder Gegenstand
4. englischen Originaltext, falls bekannt
5. aktuellen deutschen Text
6. gewünschten deutschen Text
7. Screenshot, wenn möglich

## Pull Requests

Für direkte Änderungen an der Übersetzung:

1. Repository forken.
2. Einen neuen Branch erstellen.
3. `translations/de_DE.json` bearbeiten.
4. Mod lokal mit `tools/build_mod.py` bauen.
5. Prüfen, dass kein Text sein vorhandenes Textfeld überschreitet.
6. Keine ROM, keine dekomprimierte ROM und keine extrahierten Originaldateien committen.
7. Pull Request mit kurzer Beschreibung erstellen.

## Schreibstil

- natürliches, verständliches Deutsch
- Namen und spielinterne Eigennamen konsistent halten
- wegen der aktuellen ROM-Zeichentabelle in den Spieldaten bevorzugt `ae`, `oe`, `ue` und `ss`
- möglichst kurze Formulierungen, wenn das Originalfeld wenig Platz bietet
- Formatierung immer am englischen Original ausrichten: Farben, Klammern und Satzzeichen dürfen nicht frei erfunden werden; die semantische Zuordnung muss zum deutschen Gegenstück passen

## Nicht erlaubt

Bitte niemals hochladen oder committen:

- `.z64`, `.n64`, `.v64`
- dekomprimierte ROMs
- vollständige Original-Spieldaten
- kommerziell geschützte Assets außerhalb dessen, was für einen Patch technisch erforderlich ist
