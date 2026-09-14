# Goemon64 DE 🇩🇪

Eine inoffizielle deutsche Fan-Übersetzung für **Mystical Ninja Starring Goemon (Nintendo 64)** zur Verwendung mit **Goemon 64: Recompiled**.

> **Status:** Beta v0.2.0  
> **Übersetzt:** 927 Textsegmente  
> **Schwerpunkt dieser Beta:** früher Oedo-Stadt-/Storybereich, Systemtexte, Gegenstände, Hinweise und erste Tutorials

## 📥 Download

Lade die aktuelle `.nrm`-Datei unter **Releases** herunter:

**`Goemon64-DE-Beta-v0.2.0.nrm`**

Die ROM selbst wird **nicht** mitgeliefert.

## ✅ Voraussetzungen

- Goemon 64: Recompiled
- Mod-Unterstützung / `.nrm`-Modloader
- eine eigene US-ROM von *Mystical Ninja Starring Goemon*
- für diese Beta: Goemon64Recompiled **0.2.0-dev oder neuer**

Upstream-Projekt: https://github.com/klorfmorf/Goemon64Recomp

## 🛠️ Installation

1. Lade `Goemon64-DE-Beta-v0.2.0.nrm` aus dem neuesten GitHub-Release herunter.
2. Starte **Goemon 64: Recompiled**.
3. Öffne das Menü **Mods**.
4. Wähle **Mod installieren**.
5. Wähle die heruntergeladene `.nrm`-Datei aus.
6. Aktiviere **Deutsche Uebersetzung (Beta v0.2.0)**.
7. Deaktiviere ältere Versionen der Übersetzungsmod.
8. Starte das Spiel bzw. Goemon64Recompiled vollständig neu.

Eine ausführlichere Anleitung findest du unter [docs/INSTALLATION.md](docs/INSTALLATION.md).

## 🇩🇪 Was ist bereits übersetzt?

Beta v0.2.0 enthält derzeit **927 Übersetzungseinträge**. Davon liegen **667 Einträge im frühen Oedo-Textbereich**.

Enthalten sind unter anderem:

- erste Dialoge und NPCs in Oedo-Stadt
- frühe Storytexte
- Torwächter und Polizisten
- Omitsu-/UFO-bezogene frühe Dialoge
- Schilder und Wegbeschreibungen
- Speichern sowie Ja/Nein-Abfragen
- Gegenstands- und Schlüsselmeldungen
- erste Waffen-/Fähigkeiten-Hinweise
- frühe Orts- und Burgbezeichnungen

Die Übersetzung ist **noch nicht vollständig**. Einige Bereiche des Spiels bleiben in dieser Beta auf Englisch.

## ⚠️ Bekannte Einschränkungen

- Noch keine 100-%-Übersetzung des gesamten Spiels.
- Einige Texte sind bewusst kürzer formuliert, weil die ursprünglichen N64-Textfelder feste Platzgrenzen haben.
- In der aktuellen Beta werden wegen der ursprünglichen Zeichentabelle überwiegend Schreibweisen wie `ae`, `oe` und `ue` verwendet.
- Alte Versionen der Mod sollten nicht gleichzeitig aktiviert sein.

## 🐞 Fehler melden

Wenn ein Text falsch, abgeschnitten oder weiterhin Englisch ist, erstelle bitte ein Issue und nutze die Vorlage **Übersetzungsfehler**.

Hilfreich sind:

- Ort / Szene
- Name des NPCs oder Menüs
- aktueller Text
- gewünschte Formulierung
- Screenshot, falls möglich
- verwendete Mod-Version

Siehe auch [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).

## 🔨 Selbst bauen

Das Repository enthält ein reproduzierbares Build-Werkzeug. Eine ROM wird dabei **nicht** gespeichert oder verteilt.

```bash
python3 tools/build_mod.py \
  --rom "/pfad/zu/Mystical Ninja Starring Goemon (USA).n64" \
  --translation translations/de_DE.json \
  --output-dir dist
```

Das Skript:

1. erkennt `.z64`, `.n64` und `.v64`,
2. normalisiert die ROM intern auf Big-Endian,
3. prüft die unterstützte US-ROM,
4. dekomprimiert die Goemon-ROM-Struktur,
5. liest die Texttabellen,
6. trägt `translations/de_DE.json` ein,
7. baut `patch.bps`,
8. erstellt die fertige `.nrm`.

Mehr dazu: [docs/BUILDING.md](docs/BUILDING.md).

## 🤝 Mithelfen

Korrekturen und bessere deutsche Formulierungen sind willkommen. Bitte lies vorher [CONTRIBUTING.md](CONTRIBUTING.md).

## 🗺️ Roadmap

Siehe [docs/ROADMAP.md](docs/ROADMAP.md).

## 📜 Lizenz und Rechtliches

Die eigenen Tools und die eigene Dokumentation dieses Repositorys stehen unter der MIT-Lizenz. Rechte an *Mystical Ninja Starring Goemon* und allen Original-Spieldaten verbleiben bei den jeweiligen Rechteinhabern.

Dieses Projekt enthält **keine ROM**. Siehe [LEGAL.md](LEGAL.md).

## ❤️ Credits

- **Mekurukid** – Projekt, deutsche Fan-Übersetzung und Tests
- **klorfmorf / Goemon64Recomp** – Goemon 64: Recompiled
- **N64Recomp-Team** – N64Recomp / N64ModernRuntime
- Konami – Originalspiel *Mystical Ninja Starring Goemon*

Weitere Hinweise: [CREDITS.md](CREDITS.md)
