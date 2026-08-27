# Was geprüft ist — und was nicht

Stand: 2026-08-27. Wird bei jedem neuen Vorschlag fortgeschrieben.

Regel: Kein Vorschlag ohne vorherige Prüfung. Wenn eine Prüfung nicht möglich
ist, steht das hier als „ungeprüft" — nicht als stillschweigende Annahme.

---

## Gefundene Fehler in meinen bisherigen Vorschlägen

### 1. Airtable: Outlier-Ratio als Formel — so nicht umsetzbar

Ich hatte geschrieben: „Outlier-Ratio als Formel, nicht als getippte Zahl."

Geprüft: **Airtable-Rollups können SUM, MIN, MAX, AVERAGE, COUNT, COUNTA,
COUNTALL — keinen Median.** Es gibt keine MEDIAN-Funktion.

**Korrektur, die funktioniert:**
1. Der Agent hat die Rohliste der letzten 30 Videos ohnehin im Speicher und
   berechnet den Median selbst
2. Er schreibt ihn als einfache Zahl in `Quellen.Median-Kennzahl`
3. In `Beiträge` liegt ein Lookup auf dieses Feld
4. Die Ratio ist dann eine echte Formel auf dem Lookup: `Kennzahl / Median`

Ergebnis unverändert, Rechenweg anders. Der Median kommt vom Agenten, nicht
von Airtable.

### 2. HyperFrames: Ich kann briefen, nicht bauen

Geprüft: Die Skill **`hyperframes` ist in dieser Umgebung nicht vorhanden.**
`visual-regie` sagt selbst: „Baut nichts selbst — delegiert HF an `hyperframes`."
Diese Empfängerin fehlt.

Was das für das Pipeline-Übersichtsbild heißt:
- Ich kann den **Brief** schreiben (visual-regie ist da)
- Ich kann ein **statisches SVG** direkt schreiben — die vorhandenen
  `04_menschliche-freigabe.svg` und `01_technischer_agent_freigabeprozess.svg`
  sind genau das
- Ich kann **kein animiertes HyperFrame** produzieren

Für ein Titelbild reicht SVG. Für animierte Beats brauchst du deine lokale
HyperFrames-Umgebung.

### 3. Thumbnails: dieselbe Grenze

Geprüft in `mariana-thumbnail`: Der Render läuft über
`Thumbnail rendern.command` auf deinem Mac, headless Chrome, lokal.
Ich baue `thumbs/NAME/index.html`. **Du klickst.** So war es beschrieben, so
bleibt es — ich kann hier nichts rendern.

---

## Geprüft und bestätigt

### YouTube Data API v3
Über Websuche bestätigt (Google-Doku direkt ist blockiert, siehe unten):

| | |
|---|---|
| Tageskontingent | 10.000 Einheiten |
| `search.list` | **100 Einheiten** pro Aufruf |
| `videos.list` | 1 Einheit |
| `captions.download` | 200 Einheiten, **nur als Eigentümer des Videos** |

Was das für den Recherche-Agenten bedeutet:
- 14 Seed-Begriffe × 100 = **1.400 Einheiten pro Suchlauf.** Passt ins
  Tageskontingent, aber Suchen sind teuer — der Kanal-Aufbau läuft quartalsweise,
  nicht wöchentlich. So war es vorgeschlagen, das hält.
- Die wöchentliche Auswertung bekannter Kanäle läuft über `videos.list` und
  `playlistItems.list` zu 1 Einheit — praktisch kostenlos.
- **Meine Aussage zu Transkripten war richtig:** fremde Videos gibt die API
  nicht her. Der Handdurchgang für die ersten 30 Sekunden bleibt.

### Zugänge, die ich tatsächlich habe

Direkt am Werkzeug geprüft, nicht aus der Doku:

| Werkzeug | Status | Was ich damit kann |
|---|---|---|
| Airtable | verbunden, `create` auf 3 Bases | Tabellen und Felder **selbst anlegen** — `Content_Radar` kann ich bauen |
| Google Drive | verbunden | lesen, suchen, Dateien anlegen |
| Descript | verbunden, „Mariana's Drive" | Material importieren, schneiden lassen, exportieren — der Shorts-Schnitt ist real machbar |
| Skills | lokal | `video-ideas`, `video-script`, `mariana-voice`, `visual-regie`, `humanizer-de` |

Vorhandene Bases: `LinkedIn Outreach`, `LinkedIn Agent`,
`Mika – Kälte-Signal-Scout`.

---

## Grenze dieser Umgebung

**Herstellerdokumentation ist direkt nicht erreichbar.** Getestet:
`developers.google.com`, `airtable.com`, `support.airtable.com` — alle vom
Egress-Proxy blockiert, auch über curl.

Verifizieren kann ich also über zwei Wege:
1. **Websuche** — liefert Zusammenfassungen, keine Primärquelle
2. **Den Aufruf selbst** — ich rufe das Werkzeug auf und sehe, was zurückkommt

Weg 2 ist der belastbare. Wo er möglich ist, nehme ich ihn.

Für Anbieter, mit denen wir noch nicht verbunden sind (Apify, HeyGen, Kling,
Stripe), kann ich in dieser Umgebung **nur über Websuche prüfen**. Das sage ich
dann dazu, statt es als gesichert zu verkaufen.

---

## Noch ungeprüft — offene Annahmen in meinen Vorschlägen

| Annahme | Warum ungeprüft |
|---|---|
| Landingpage-System | Weiß nicht, worauf sometra.de läuft. In Drive liegt `wp_article_04.html`, das deutet auf WordPress — geraten, nicht geprüft |
| Zahlungsweg für den Workshop | Unbekannt, ob Stripe oder etwas anderes vorhanden ist |
| Screen-Recording-Werkzeug | Unbekannt, womit du aufnimmst |
| LinkedIn-Content-Scanner | Beruht auf deiner Aussage, dass die Agenten Profile erreichen. Die Agenten-Prompts selbst habe ich nie gesehen — sie liegen lokal, nicht in Drive |
| Kalender-/Buchungswerkzeug | Unbekannt |

Diese fünf klären wir, bevor ich etwas darauf aufbaue.
