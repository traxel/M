# Entscheidung: F2F in drei Städten, November 2026

Stand: 2026-08-27. Ersetzt den Remote-Rahmen aus `funnel/funnel.md` und
`funnel/workshop-5-agenten.md`.

---

## Was Mariana festgelegt hat

| | |
|---|---|
| Format | **Präsenz**, nicht remote |
| Städte | Hamburg · München · Köln |
| Termine | Hamburg Do 29.10. · München Mo 02.11. · Köln Do 05.11.2026 |
| Dauer | ein Tag, 09:00–17:00 |
| Preis | **2.356 € netto** je Person (bestätigt 27.08.) |
| Teilnehmer | max. **12** je Stadt — Zahl gehört ausdrücklich in die Kommunikation |
| Pausen | 30 Min Frühstück · 60 Min Mittag · 45 Min Kaffee |
| Vormittag | Grundlagen: Code, Codex (OpenAI) vs. Claude (Anthropic), Cowork/Work, Artefakte, Skills, Connectoren, MCPs, APIs |
| Nachmittag | fünf LinkedIn-Agenten bauen |
| Steuerung | Airtable **und** Excel |
| Genannte Agenten | Such-/Finde-Agent, DM-Schreibe-Agent |

Titel der Schulung: **So bauen Sie sich Ihre Vertriebsagenten — Schritt für Schritt.**

---

## Was sich dadurch überholt

`funnel/funnel.md` und `funnel/workshop-5-agenten.md` beschreiben einen
Remote-Workshop zu 490 € (Pilot) bzw. 890 €. Das ist überholt. Beide
Dokumente bleiben als Herleitung stehen, gelten aber nicht mehr als Rahmen.

### Das Versprechen ist enger gefasst worden

Nicht mehr „fünf Agenten laufen", sondern:

> **Sie haben mindestens einen funktionierenden Agenten selbst programmiert.**

Gebaut werden am Tag weiterhin fünf. Zugesagt wird einer.

Gründe:
- Fünf Agenten bei zwölf Leuten sind erreichbar, aber nicht garantierbar
- Einer, am Platz nachgeprüft, ist garantierbar — und die Garantie hängt genau
  an dem, was nachgeprüft wird
- „Selbst programmiert" ist für den Marketing- und Vertriebsleiter der stärkere
  Satz. Er kann ihn am Montag im Haus sagen

**Ein Widerspruch, der dabei aufgelöst werden musste:** Auf derselben Seite
stand „selbst programmiert" und „Sie müssen nicht programmieren, keine Zeile".
Beides zusammen ist unglaubwürdig. Aufgelöst so: Eine Programmiersprache
braucht niemand. Auftrag, Prüflogik und Abbruchregeln schreibt der Teilnehmer
selbst, in seiner Sprache — und das Ergebnis läuft weiter, wenn er den Rechner
zuklappt. Das ist ein Programm, und so steht es jetzt auf der Seite und in der
FAQ.

**Was aus dem alten Rahmen bleibt:**
- Konstruktionsregel: kein Agent klickt auf Senden
- Garantie: es läuft bei Ihnen oder Sie bekommen den Preis zurück
- Jeder baut in seinem eigenen Konto, mit seinen eigenen Daten
- Die fünf Agenten als Ablauf: finden, prüfen, ansprechen, nachfassen, sichtbar bleiben

---

## Der Rechenkonflikt, der aufgelöst werden musste

345 Minuten Lernzeit. Bei striktem Schnitt „Vormittag Grundlagen,
Nachmittag Agenten" ergibt das:

| | Minuten |
|---|---|
| Vormittag (Block 1 + 2) | 195 |
| Nachmittag (Block 3 + 4) | **150** |

150 Minuten für fünf Agenten sind 30 Minuten pro Agent — ohne Kontrollpunkt,
ohne Abschluss, ohne Puffer. **Das geht nicht.** Ein Agent, der in 30 Minuten
gebaut, angebunden und einmal durchgelaufen sein soll, ist bei zwölf
Teilnehmern in einem fremden Raum nicht zu halten.

**Aufgelöst so:** Die Grundlagen bekommen 90 Minuten als Überblick. Skills,
Connectoren und MCPs werden nicht zweimal behandelt — sie werden am ersten
Agenten praktisch gelernt. Damit fängt der Bau um 11:00 an statt um 13:45,
und die Agenten haben **235 Minuten** statt 150.

Details in `schulung/tagesplan-f2f.md`.

---

## Die Rechnung

Bei 12 Plätzen und 2.356 € je Person:

| | |
|---|---|
| Ein voller Tag (12 × 2.356 € netto) | 28.272 € |
| Drei Städte voll | **84.816 €** |
| Halb voll (6 je Stadt) | 42.408 € |
| Deckung ab | ca. 2 Teilnehmern je Stadt (Raum + Catering + Anreise) |

Raum und Catering sind bei diesem Preis kein Kostenproblem. **Das Problem ist
die Füllung:** 36 Plätze bis November.

Zum Vergleich die Rechnung aus `funnel/funnel.md`: Für 10 Käufer über den
offenen Funnel wären rund 8.500 erreichte Kontakte im Monat nötig. Für 36
Käufer zum vierfachen Preis ist die Zahl größer, nicht kleiner.

**Konsequenz, unverändert gegenüber dem alten Plan:** Der erste Durchlauf
wird nicht über Content gefüllt, sondern über Direktansprache. Content baut
das Vertrauen auf, das die Direktansprache braucht. Beides läuft parallel,
nicht nacheinander.

---

## Offen — vor dem Livegang zu klären

| Punkt | Warum es blockiert |
|---|---|
| **Konkrete Termine** | **Bestätigt 27.08.:** Hamburg Do 29.10. · München Mo 02.11. · Köln Do 05.11.2026 |
| **Räume** | nicht gebucht. Drei Tagungsräume für 12 Personen plus Catering |
| **Zahlungsweg** | weiterhin ungeklärt (siehe `verifiziert.md`) |
| **Landingpage-System** | weiterhin ungeklärt. Die Seite liegt als eigenständige HTML-Datei vor und ist damit unabhängig vom System |
| **Storno- und Ausfallregel** | bei Präsenz nötig, bei remote nicht. Ein Teilnehmer, der nicht erscheint, blockiert einen Platz und ein Catering |
