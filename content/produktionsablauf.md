# Produktionsablauf je Einheit

Stand: 2026-08-27, zweite Fassung.
Erste Fassung war an zwei Stellen falsch — siehe unten.

---

## Was an der ersten Fassung nicht stimmte

**1. „Schnitt — Descript" war ungeprüft.**
Nachgelesen im Werkzeug-Schema des verbundenen Connectors:
`prompt_project_agent` nimmt **Anweisungen in natürlicher Sprache** entgegen
und arbeitet auf einem Projekt, in das vorher Material importiert wurde.

Es kann also schneiden — aber **nur, was man ihm sagt.** „Schneide das gut"
ist keine Anweisung. Das Werkzeug weiß nicht, welcher Take gilt, wo ein
Screen-Recording einsetzt, wo eine Pause raus soll.

**Das ist keine Werkzeugfrage, sondern eine Regiefrage.** Sie gehört ins
Drehbuch, nicht in den Schnitt. Wenn im Drehbuch steht, was wann zu sehen
ist, kann Descript es umsetzen. Sonst nicht.

**2. „Aufnehmen" ist kein Schritt.**
Ein Video über den Watchdog braucht mehrere Aufnahmen:

- Talking Head — du vor der Kamera
- Terminal mit dem laufenden Agenten
- Airtable mit den Herzschlag-Zeitstempeln
- gegebenenfalls CoWork, Codex oder Claude Code als Oberfläche

Vier bis sechs getrennte Aufnahmen je Einheit, jede mit eigener Vorgabe:
was ist zu sehen, was passiert darin, wie lang, an welcher Stelle im Skript.

Das stand in der ersten Fassung als eine Zeile. Falsch.

---

## Korrigierter Ablauf

| # | Schritt | Wer | Ergebnis |
|---|---|---|---|
| 1 | Genre und Titel | ich schlage vor, **du wählst** | ein Titel |
| 2 | Story-Spine, gelockt | ich schreibe, **du gibst frei** | Kausalkette |
| 3 | Skript, 500–700 Wörter | ich | Sprechtext |
| 4 | **Visual-Regie je Beat** | ich, über `visual-regie` | je Beat: Talking Head, Screen, HyperFrame oder Kling |
| 5 | **Aufnahmeliste** | ich | 4–6 einzelne Aufnahmen, je mit Inhalt, Dauer, Reihenfolge |
| 6 | **Aufnehmen** | **du** | die Dateien aus Schritt 5 |
| 7 | Schnittanweisung | ich | welcher Take wann, was raus, wo Screens liegen |
| 8 | Schnitt | Descript, nach Schritt 7 | Rohschnitt |
| 9 | Thumbnail | ich baue, **du renderst** | PNG 1280×720 |

Neu gegenüber der ersten Fassung: Schritt 4, 5 und 7.
Ohne 5 weißt du nicht, was du aufnehmen sollst. Ohne 7 weiß Descript nicht,
was es schneiden soll.

---

## Dein Setup — beantwortet 27.08.

| | |
|---|---|
| Screen | **OBS** |
| Talking Head | **iPhone-Rückkamera + externes Mikro** |
| Schnitt | **CapCut** (überwiegend), sonst VEED.io |
| Footage | **Kling**, Pexels, Stock-Anbieter |
| Descript | **fällt raus** — Zugriff nur über Fal, und alles ist auf Deutsch |

### Was das am Ablauf ändert

- **Kein Descript.** Schritt 8 heißt jetzt: Schnitt in CapCut, von dir.
  Ich liefere die Schnittanweisung als Liste, keine Werkzeug-Automatik.
- **Zwei getrennte Quellen** — OBS für Screen, iPhone für Talking Head. Die
  Aufnahmeliste muss beides getrennt ausweisen, inklusive Reihenfolge.
- **Ton kommt vom externen Mikro**, nicht aus OBS. In CapCut wird auf den
  Ton synchronisiert, nicht auf das Bild.
- **Kling ist gesetzt** für alles, was nicht Screen und nicht du ist. Prompts
  schreibe ich, ausgeführt wird lokal über `media-gen`.

---

## Was davon unberührt bleibt

Schritt 1 bis 3 hängen an keiner dieser Fragen. Titel, Spine und Skript
kann ich sofort bauen — die Frage, womit gefilmt wird, ändert am Sprechtext
nichts.
