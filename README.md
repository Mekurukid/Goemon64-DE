# Goemon64 DE 🇩🇪

Eine inoffizielle deutsche Fan-Übersetzung für **Mystical Ninja Starring Goemon (Nintendo 64)** zur Verwendung mit **Goemon 64: Recompiled**.

> **Aktueller Release:** Beta v0.8.5  
> **Status:** vollständige geprüfte Textabdeckung, weitere In-Game-Feinprüfung  
> **Formatierung:** Originalfarben, Klammern/Satzzeichen, Auswahl-Hervorhebungen und Portrait-Textbox-Einrückungen werden nach der US-Original-ROM übernommen.

## 📥 Download

Lade unter **Releases** die Datei herunter:

**`Goemon64-DE-Beta-v0.8.5.nrm`**

Die ROM selbst wird **nicht** mitgeliefert.

## ✅ Voraussetzungen

- **Goemon 64: Recompiled**
- Mod-Unterstützung / `.nrm`-Modloader
- eigene legal erstellte US-ROM von *Mystical Ninja Starring Goemon*
- Goemon64Recompiled **0.2.0-dev oder neuer**

Upstream: https://github.com/klorfmorf/Goemon64Recomp

## 🛠️ Installation

1. `Goemon64-DE-Beta-v0.8.5.nrm` aus dem neuesten Release herunterladen.
2. **Goemon 64: Recompiled** starten.
3. **Mods** öffnen.
4. **Mod installieren** wählen und die `.nrm` auswählen.
5. **Deutsche Uebersetzung Beta v0.8.5** aktivieren.
6. Alle älteren Goemon64-DE-Versionen deaktivieren.
7. Goemon64Recompiled vollständig neu starten.

Mehr: [docs/INSTALLATION.md](docs/INSTALLATION.md)

## 🇩🇪 Was ist übersetzt?

Der geprüfte Textkatalog ist vollständig deutsch abgedeckt. Dazu gehören unter anderem:

- Story- und NPC-Dialoge
- Menüs und Systemmeldungen
- Shops, Restaurants und Gasthäuser
- Speichern / Abenteuerbuch
- Gegenstands-, Schlüssel- und Fähigkeitsmeldungen
- Trainings- und Minispieltexte
- Karten-, Status- und Optionshinweise
- versteckte UI-/Nachspieltexte, soweit sie als ROM-Text vorliegen

Humor, Wortspiele und Figurenstimmen werden **sinngemäß** ins Deutsche übertragen, nicht steif Wort für Wort.

## 🎨 Originalgetreue Textformatierung

Beta v0.8.5 übernimmt die Formatierungslogik der englischen US-ROM möglichst exakt:

- Gelb, Rot, Grün und Blau
- farbige Namen und Schlüsselbegriffe
- `[Klammern]` und `(Klammern)`, wenn diese im Original Teil der Farbe sind
- farbige Satzzeichen, Ellipsen und Apostrophe
- Auswahl-Hervorhebungen
- Groß-/Blinkeffekte
- blockübergreifende Farbzustände
- Portrait-/Avatar-Einrückungen

Die deutsche Satzstellung wird bei Bedarf angepasst, damit das entsprechende deutsche Wort vollständig und korrekt formatiert werden kann.

## ✅ QA Beta v0.8.5

- **5.393** Textreferenzen geprüft
- **5.147** Übersetzungseinträge
- **1.931 / 1.931** Original-Farbspannen erhalten
- **327** Klammer-/Bracket-Farbmarkierungen geprüft
- **0** Scriptfehler
- **0** unbekannte Zeichen
- **0** Farbgrenzen mitten im Wort
- **0** sichtbare Textabweichungen

Details: `QA-Bericht-v0.8.5.txt` im Release.

## ⚠️ Beta / bekannte Grenzen

- v0.8.5 bleibt bewusst Beta, bis noch mehr komplette In-Game-Durchläufe erfolgt sind.
- Texte, die fest als **Grafik/Textur** im Original gespeichert sind, gehören nicht zum normalen ROM-Textkatalog und können separat behandelt werden.
- Die Spieldaten verwenden aufgrund der Zeichentabelle überwiegend `ae`, `oe`, `ue` und `ss`.
- Immer nur **eine** Version von Goemon64 DE gleichzeitig aktivieren.

## 🐞 Fehler melden

Bitte über **Issues → Übersetzungsfehler** melden und möglichst angeben:

- Mod-Version: Beta v0.8.5
- Ort / Szene
- NPC / Menü
- sichtbarer deutscher Text
- Screenshot
- was falsch wirkt (Text, Farbe, Klammer, Einrückung, Doppelung usw.)

## 📜 Lizenz / Rechtliches

Eigene Tools und Dokumentation stehen unter der MIT-Lizenz. Rechte am Originalspiel, seinen Figuren, Texten, Grafiken, Musik- und Spieldaten verbleiben bei den jeweiligen Rechteinhabern.

**Dieses Repository und seine Releases enthalten keine ROM.** Siehe [LEGAL.md](LEGAL.md).

## ❤️ Credits

- **Mekurukid** – Projekt, deutsche Fan-Übersetzung, Tests und Release-Pflege
- **klorfmorf / Goemon64Recomp** – Goemon 64: Recompiled
- **N64Recomp-Team** – N64: Recompiled / Runtime-Grundlage
- **Konami** – Originalspiel *Mystical Ninja Starring Goemon*

Weitere Hinweise: [CREDITS.md](CREDITS.md)
