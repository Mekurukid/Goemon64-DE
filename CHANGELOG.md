# Changelog

Alle wichtigen Änderungen an der deutschen Fan-Übersetzung werden hier dokumentiert.

## [0.8.5] - 2026-09-14

### Übersetzung

- Vollständige geprüfte Textabdeckung des extrahierten ROM-Textkatalogs.
- NPC- und Storydialoge sprachlich geglättet; Humor und Figurenstimmen sinngemäß erhalten.
- Menüs, Shops, Restaurants, Gasthäuser, Trainings-, Speicher- und Systemtexte vervollständigt.
- Mehrteilige Dialogketten auf Doppelungen, Satzabbrüche und unnatürliche Übergänge korrigiert.

### Originalgetreue Formatierung

- 1.931 originale Farbspannen vollständig in der deutschen Fassung erhalten.
- Gelb, Rot, Grün und Blau getrennt gegen die Original-ROM geprüft.
- Namen, Schlüsselbegriffe, Auswahltexte sowie farbige Klammern und Satzzeichen semantisch auf das deutsche Gegenstück gemappt.
- 327 Klammer-/Bracket-bezogene Farbspannen geprüft.
- Portrait-/Avatar-Textbox-Einrückungen nach Originalvorbild wiederhergestellt.
- Textdaten innerhalb sicherer ROM-Textpools neu gepackt, damit längere deutsche Begriffe ihre Originalformatierung behalten können.

### QA

- 5.393 Textreferenzen geprüft.
- 5.147 Übersetzungseinträge.
- 0 Scriptfehler.
- 0 unbekannte Zeichen.
- 0 Farbgrenzen mitten in Wörtern.
- 0 sichtbare Textabweichungen.

### Hinweis

- Der Release bleibt bewusst **Beta v0.8.5**, bis weitere vollständige In-Game-Durchläufe abgeschlossen sind.

## [0.3.0] - 2026-09-14

### Hinzugefügt

- Übersetzungsumfang von **927 auf 1.294 Textsegmente** erhöht.
- **367 neue Textsegmente** im anschließenden Story-/NPC-Block übersetzt.
- Yae-Beitritt und Peach-Mountain-Shoguns-Gespräch erweitert.
- Benkei-, Kihachi- und Ushiwaka-Dialoge ergänzt.
- Goldener Tempel, Training, Wegweiser und weitere Kansai-NPCs übersetzt.
- Humor und Wortspiele bewusst sinngemäß statt steif wörtlich übertragen.

### Übersetzungsstil

- Schräge NPC-Sprüche bleiben locker und überdreht.
- Pointen werden bei Bedarf für natürliches Deutsch angepasst.
- Figurenstimmen sollen erkennbar bleiben.
- Wegen der N64-Zeichentabelle weiterhin `ae`, `oe`, `ue` und `ss` in den Spieldaten.

### Technisch

- QA erneut über **5.393 Textverweise**.
- 0 Skriptfehler und 0 unbekannte Zeichen im Ziel-ROM-Abbild.
- Reproduzierbarer Build weiterhin über `tools/build_mod.py`.

## [0.2.0] - 2026-09-14

### Hinzugefügt

- Übersetzungsumfang auf **927 Textsegmente** erweitert.
- **667 Texte** aus dem frühen Oedo-Bereich aufgenommen.
- Mehr frühe NPC-Dialoge und Storytexte.
- Oedo-Stadt, Torwächter, Polizisten und frühe Hinweise erweitert.
- Weitere Speicher-, Ja/Nein-, Gegenstands- und Systemtexte.
- Reproduzierbarer GitHub-Build mit `tools/build_mod.py`.

### Technisch

- BPS-Patch wird gegen die von Goemon64Recompiled verwendete dekomprimierte ROM-Basis erzeugt.
- NRM-Struktur besteht aus `mod.json` und `patch.bps`.
- QA: 5.393 Textverweise erfolgreich verarbeitet.
- QA: 0 Skriptfehler und 0 unbekannte Zeichen im geprüften Ziel-ROM-Abbild.

### Bekannt

- Übersetzung ist weiterhin unvollständig.
- Teilweise englische Dialoge in späteren Gebieten.

## [0.1.1] - 2026-09-14

- Technischer Testbuild zur Korrektur des Mod-Ladevorgangs.

## [0.1.0] - 2026-09-14

- Erste öffentliche Beta-Grundlage.
- Erste System-, Item- und Storytexte.
