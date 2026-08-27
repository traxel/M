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

### 2. HyperFrames — meine Aussage war zu pauschal

Ich hatte geschrieben: „Ich kann kein animiertes HyperFrame produzieren."
Richtig ist: **nicht aus dieser Umgebung heraus.** Auf deinem Mac habe ich das
bereits gemacht.

Nachgeprüft, alle drei Wege:

| Prüfung | Ergebnis |
|---|---|
| Dateisystem, gesamt (`find / -iname "*hyperframe*"`) | kein Treffer |
| `ListConnectors` — alle Connectoren des Kontos | Airtable, Canva, Descript, Gmail, Google Calendar, Google Drive, Granola, HubSpot, Microsoft 365, Zoom, Spotify. **Kein HyperFrames** |
| `ListSkills` mit Stichwort hyperframes | nur `visual-regie`, die dorthin delegiert |

**Das ist keine Fähigkeitsgrenze, sondern eine Umgebungsgrenze.**
Diese Session läuft in einem Cloud-Container mit einer gesyncten Teilmenge
deiner Skills. Die HyperFrames-Studio-Engine liegt lokal auf deinem Mac —
genau wie die Thumbnail-Render-Maschine.

Konsequenz für die Arbeitsteilung:
- **HyperFrames-Arbeit gehört in eine lokale CLI-Session**, nicht hierher
- Von hier aus: Brief über `visual-regie`, statisches SVG direkt geschrieben
- Wenn ein HyperFrame gebraucht wird, sage ich das und du startest lokal

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
- Zu Transkripten: Die API gibt fremde Videos nicht her — das stimmt. Dass
  daraus ein Handdurchgang folgt, stimmt **nicht**. Siehe unten.

### Transkripte — der Weg über Audio funktioniert

Ich hatte eine Sackgasse behauptet, weil ich nur die YouTube-API geprüft habe
und nicht die Werkzeuge daneben. Du hattest recht: über Audio ist es gelöst.

Geprüft am Schema der verbundenen Descript-Werkzeuge, nicht aus der Doku:

- `import_media` **transkribiert beim Import.** Das Feld `language` ist dort
  ausdrücklich „ISO 639-1 language code for transcription", mit
  Spracherkennung wenn leer.
- `export_transcript` liefert `txt`, `markdown`, `html`, `rtf` und **`srt`** —
  mit Zeitmarken, wahlweise auf Absätze, Sprecherwechsel oder in festem
  Intervall.

`srt` mit Zeitmarken ist für die Hook-Analyse genau richtig: die ersten
30 Sekunden sind darin ein abgegrenzter Block.

**Die Grenze, die bleibt** — auch am Schema geprüft:
`import_media` nimmt laut eigener Beschreibung „URLs (direct links, Google
Drive, Dropbox)". **YouTube-Links stehen dort nicht.** Die Audiodatei muss
also vorliegen oder in Drive liegen.

Und in dieser Umgebung: kein `yt-dlp`, kein `ffmpeg`, `youtube.com` nicht
erreichbar. **Das Ziehen der Audiospur passiert bei dir lokal**, danach
übernimmt Descript von hier aus.

Damit ist der Handdurchgang vom Tisch. Der Ablauf ist:
Audio lokal ziehen → in Drive oder direkt zu Descript → `srt` exportieren →
Hook-Analyse automatisch.

### googleapis.com ist erreichbar — anders als gedacht

`https://www.googleapis.com/youtube/v3/videos` beantwortet Anfragen. Die 403
kommt **von Google, nicht vom Proxy**: „Method doesn't allow unregistered
callers... Please use API Key."

Das heißt: **Mit einem API-Key kann ich den Recherche-Agenten von hier aus
bauen und testen**, nicht nur beschreiben. Nur die Dokumentationsseiten
(`developers.google.com`) sind blockiert, die API selbst nicht.

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

**Herstellerdokumentation ist blockiert, die APIs selbst oft nicht.**

| Ziel | Ergebnis |
|---|---|
| `developers.google.com` | blockiert |
| `airtable.com`, `support.airtable.com` | blockiert |
| `outlierkit.com` und ähnliche | blockiert |
| **`www.googleapis.com`** | **erreichbar**, antwortet mit Googles eigener Fehlermeldung |
| `youtube.com` | nicht erreichbar |

Der Unterschied ist wichtig: Eine blockierte Doku heißt nicht, dass der Dienst
nicht nutzbar ist.

Prüfreihenfolge, von belastbar nach schwach:

1. **Den Dienst aufrufen** und sehen, was zurückkommt
2. **Das Werkzeug-Schema lesen** — bei verbundenen Connectoren steht dort, was
   der Anbieter tatsächlich zusagt (so ist der Descript-Weg oben belegt)
3. **Umgebung prüfen** — `ListConnectors`, `ListSkills`, Dateisystem, curl
4. **Websuche** — Zusammenfassungen, keine Primärquelle

Erst wenn 1 bis 3 nichts hergeben, zählt 4 — und dann sage ich dazu, dass es
nur Websuche war.

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
| Kalender-/Buchungswerkzeug | Google Calendar ist verbunden — ob du damit buchen lassen willst, ist offen |
| Kling, HeyGen, Apify | Keine Verbindung vorhanden. Prüfung dort nur über Websuche möglich, das sage ich künftig dazu |

Diese fünf klären wir, bevor ich etwas darauf aufbaue.
