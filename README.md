# Goemon64 DE 🇩🇪

Eine inoffizielle deutsche Fan-Übersetzung für **Mystical Ninja Starring Goemon (Nintendo 64)** zur Verwendung mit **Goemon 64: Recompiled**.

> **Status:** Beta v0.5.0  
> **Übersetzt:** 1.796 Textsegmente  
> **Schwerpunkt dieser Beta:** weitere Story- und NPC-Dialoge, zusätzliche Spielbereiche, Systemtexte, Gegenstände, Hinweise, Tutorials sowie Charakter- und Fähigkeitstexte

## 📥 Download

Lade die aktuelle `.nrm`-Datei unter **Releases** herunter:

**`Goemon64-DE-Beta-v0.5.0.nrm`**

Die ROM selbst wird **nicht** mitgeliefert.

## ✅ Voraussetzungen

- Goemon 64: Recompiled
- Mod-Unterstützung / `.nrm`-Modloader
- eine eigene US-ROM von *Mystical Ninja Starring Goemon*
- für diese Beta: Goemon64Recompiled **0.5.0-dev oder neuer**

Upstream-Projekt: https://github.com/klorfmorf/Goemon64Recomp

## 🛠️ Installation

1. Lade `Goemon64-DE-Beta-v0.5.0.nrm` aus dem neuesten GitHub-Release herunter.
2. Starte **Goemon 64: Recompiled**.
3. Öffne das Menü **Mods**.
4. Wähle **Mod installieren**.
5. Wähle die heruntergeladene `.nrm`-Datei aus.
6. Aktiviere **Deutsche Uebersetzung (Beta v0.5.0)**.
7. Deaktiviere ältere Versionen der Übersetzungsmod.
8. Starte das Spiel bzw. Goemon64Recompiled vollständig neu.

Eine ausführlichere Anleitung findest du unter [docs/INSTALLATION.md](docs/INSTALLATION.md).

# 🇩🇪 Goemon64-DE – Beta v0.5.0

Ein neues Update der deutschen Übersetzung für **Mystical Ninja Starring Goemon** ist da!

## 🆕 Änderungen

- 🇩🇪 Deutlich mehr Spieltexte ins Deutsche übersetzt
- 💬 Weitere NPC-Dialoge übersetzt
- 🎮 Weitere Menü- und Systemtexte übersetzt
- 📖 Weitere Storytexte bearbeitet
- 😂 Dialoge überarbeitet, damit Humor und Charakter des englischen Originals auch auf Deutsch möglichst gut erhalten bleiben
- ✍️ Viele Formulierungen natürlicher gestaltet
- 🔧 Bereits vorhandene Übersetzungen verbessert und korrigiert
- 📝 Rechtschreibung und Zeichensetzung an mehreren Stellen überarbeitet
- 🎭 Wortspiele und ungewöhnliche Dialoge teilweise neu angepasst, damit sie im Deutschen besser funktionieren
- 🛠️ Kleinere Fehler aus vorherigen Beta-Versionen behoben

## ⚠️ Beta-Hinweis

Die Übersetzung ist weiterhin **nicht vollständig**.

Im Spiel können deshalb noch:

- englische Texte
- nicht übersetzte NPC-Dialoge
- Tippfehler
- abgeschnittene Texte
- oder noch nicht optimal formulierte Übersetzungen

auftauchen.

Wenn ihr etwas findet, könnt ihr gerne ein **GitHub Issue** erstellen. Screenshots und die genaue Stelle im Spiel helfen dabei sehr.

## 📦 Update

**Version:** `Beta v0.5.0`

**Datei:** `Goemon64-DE-Beta-v0.5.0.nrm`

Vor der Installation sollte eine ältere Version der Übersetzungsmod deaktiviert bzw. entfernt werden.

---

Danke an alle, die das Projekt testen und Feedback geben! ❤️

Die Übersetzung wird weiter Stück für Stück erweitert und verbessert.

**Viel Spaß mit Goemon64-DE Beta v0.5.0! 🇩🇪🥷**

— **Mekurukid**

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
