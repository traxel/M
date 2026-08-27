# Übergabe an die lokale Session

Stand: 2026-08-27. Vorherige Arbeit lief in einer Cloud-Session.
Ab hier lokal auf dem Mac.

---

## Wo wir stehen

**Entschieden:** Sometra verkauft Schulung und Umsetzungsbegleitung, keine
Plattform. → `entscheidungen/2026-08-26_schulung-statt-plattform.md`

**Modell:** kostenlose Live-Session → Landingpage → Tagesworkshop „5 Agenten"
mit Geld-zurück-Garantie → Retainer. → `funnel/funnel.md`

**Reihenfolge:** Erst Content, der Ergebnisse zeigt. Dann der Termin.
Termin noch in 2026. → `content/content-struktur.md`

**Nächster Schritt:** Drei Content-Einheiten produzieren — Watchdog Frühcheck,
Versand, Recherche. Vorher der YouTube-Recherchelauf.
→ `arbeitsteilung.md`, `naechste-schritte.md`

---

## Warum lokal

Was für die Produktion gebraucht wird, liegt auf dem Mac:

| | |
|---|---|
| Kling über `media-gen` / Fal | `FAL_KEY` steht lokal |
| Thumbnail-Render | `Thumbnail rendern.command` |
| Apify | Desktop-Erweiterung |
| YouTube-Key | Schlüsselbund |

Was die Cloud hatte — Airtable, Drive, Descript — ist per Connector auch hier
erreichbar. Umgekehrt gilt das nicht. Details: `verifiziert.md`.

---

## Erster Lauf

```bash
YT_API_KEY=$(security find-generic-password -s yt-api-key -w) \
  python3 agenten/scripts/yt_outlier.py @BenAI
```

Erwartet: Kanal, Abonnenten, Median-Views, darunter die Videos mit
Outlier-Ratio ab 2,0. Am Ende das verbrauchte Kontingent (~3 von 10.000).

Grundlage: `agenten/recherche-agent-content.md`.

---

## Was offen ist

1. Welche englischen Kanäle neben Ben AI in die Liste — 15 bis 25 als Ziel
2. Testansicht in Airtable mit erfundenen Datensätzen, bevor gefilmt wird
3. Drehtag 1 im Kalender
4. Preis R2 bestätigen (3.500 €/Monat vorgeschlagen)
5. Landingpage-System, Zahlungsweg, Screen-Recording-Werkzeug

---

## Arbeitsregeln, die gelten

- Kurz antworten, in Bullets
- Kein Vorschlag ohne vorherige Prüfung — Prüfreihenfolge in `CLAUDE.md`
- Vor dem Ausschließen drei Fragen: Ist es vorhanden? Läuft es von hier?
  Lässt es sich nachinstallieren?
