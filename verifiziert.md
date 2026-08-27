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
| ~~Landingpage-System~~ | **Geklärt 27.08.: Hosteurope, WordPress, Oxygen Builder.** Die Seite wird in sometra.de integriert. Impressum und Firmendaten stehen dort bereits. sometra.de selbst ist aus dem Container blockiert (403 vom Proxy, per Abruf und curl geprüft) — ich kann die Seite von hier nicht ansehen |
| ~~Zahlungsweg~~ | **Entschieden 27.08.: Stripe, Einrichtung durch Mariana am Wochenende.** Kein Zahlungs-Connector in dieser Umgebung, Optionen und Empfehlung in `angebot/zahlungsweg.md` — dort alles zu Gebühren und Fristen ausdrücklich nur Websuche |
| Screen-Recording-Werkzeug | Unbekannt, womit du aufnimmst |
| LinkedIn-Content-Scanner | Beruht auf deiner Aussage, dass die Agenten Profile erreichen. Die Agenten-Prompts selbst habe ich nie gesehen — sie liegen lokal, nicht in Drive |
| Kalender-/Buchungswerkzeug | Google Calendar ist verbunden — ob du damit buchen lassen willst, ist offen |
| HeyGen | Keine Spur im Werkzeugbestand — siehe Umgebungskarte unten |
| Apify | Keine Verbindung. Prüfung nur über Websuche |

Diese fünf klären wir, bevor ich etwas darauf aufbaue.

---

## Umgebungskarte — was läuft wo

Nachgeprüft am 27.08. Drei Anläufe haben dasselbe Muster ergeben, deshalb
steht es jetzt als Karte da statt als Einzelfall.

**Dein Mac hat den vollen Werkzeugkasten. Diese Cloud-Session hat eine
Teilmenge.** Wenn ich sage „geht nicht", muss ich sagen, welches der beiden
ich meine.

| Werkzeug | Hier | Lokal | Beleg |
|---|---|---|---|
| Airtable | ✓ `create` auf 3 Bases | ✓ | Connector, live aufgerufen |
| Google Drive | ✓ lesen und schreiben | ✓ | Connector, live aufgerufen |
| Descript | ✓ Import, Transkript, Schnitt, Publish | ✓ | Connector, Schema gelesen |
| Canva, Gmail, Calendar, HubSpot, M365, Zoom, Granola | ✓ | ✓ | `ListConnectors` |
| YouTube Data API | ✓ **sobald ein Key da ist** | ✓ | `googleapis.com` antwortet |
| **Kling** | ✗ | **✓** | in `media-gen` über Fal: `fal-ai/kling-video/v3/pro/image-to-video` und `v3/4k`. Braucht `FAL_KEY` — hier nicht gesetzt, `fal.run` nicht erreichbar |
| Alle anderen Fal-Modelle | ✗ | ✓ | dieselbe Ursache |
| **HyperFrames** | **✓ end-to-end getestet** | ✓ | siehe unten |
| **Thumbnail-Render** | ✗ | ✓ | `Thumbnail rendern.command`, headless Chrome, lokal |
| **HeyGen** | ✓ Connector `HyperFrames by HeyGen` | ✓ | HeyGen und HyperFrames sind derselbe Anbieter |

### Kling — korrigiert

Ich hatte geschrieben, für Kling gäbe es „keine Verbindung". Falsch.
Kling ist über die `media-gen`-Skill und Fal.ai eingebunden, mit zwei Modellen
für Bild-zu-Video. Nur ausführen kann ich es von hier nicht: `FAL_KEY` ist im
Container nicht gesetzt, und `fal.run` ist nicht erreichbar.

Für die Videoarbeit heißt das: **Kling-Prompts schreibe ich hier, ausgeführt
wird lokal.** Genau die Rollenteilung, die `visual-regie` ohnehin vorsieht —
sie liefert den Prompt, das Tool baut.

### HeyGen = HyperFrames — und beides läuft hier

Der Connector heißt **`HyperFrames by HeyGen`**. Damit ist die Frage
beantwortet: HeyGen und HyperFrames sind derselbe Anbieter, und mein
„HeyGen finde ich nirgends" war eine Suche nach dem falschen Namen.

**Am 27.08. end-to-end getestet, nicht aus der Doku übernommen:**

```
npx skills add heygen-com/hyperframes     → 9 Skills installiert
npx hyperframes init … --example blank    → Projekt angelegt
npx hyperframes render --quality draft    → out.mp4
```

Ergebnis: **1920×1080, h264, 10,0 s, gerendert in 25,5 s.**
Mit `ffprobe` gegengeprüft, nicht nur „hat nicht gemeckert".

Damit ist belegt: **Animierte HyperFrames kann ich aus dieser Umgebung
bauen und rendern.** Meine gegenteilige Aussage war falsch — sie beruhte
darauf, dass ich nur den Skills-Ordner durchsucht und daraus geschlossen
habe, statt zu versuchen zu installieren.

**Installierte Skills:** `hyperframes`, `-core`, `-cli`, `-animation`,
`-keyframes`, `-audio`, `-creative`, `-registry`, `remotion-to-hyperframes`.

**Zwei Dinge mussten nachinstalliert werden:**
- `ffmpeg` und `ffprobe` über `apt-get install ffmpeg`. Das mitgelieferte
  Playwright-ffmpeg reicht nicht — **ffprobe fehlt dort**, und der Renderer
  braucht es.
- Chrome lädt der Renderer beim ersten Lauf selbst nach (114 MB).

**Wichtig: Der Container ist flüchtig.** Beides ist nach einer neuen Session
wieder weg. Das gehört in einen SessionStart-Hook, sonst kostet es jedes Mal
ein paar Minuten.

**Eine Einschränkung, ehrlich:** Der Testrender lief mit der Warnung
`sub_timeline_script_failure` durch — aus der Blank-Vorlage, nicht aus eigenem
Code. Die MP4 ist gültig. Bei einer echten Komposition ist das nachzuprüfen.

### Der Connector selbst — teilweise geprüft

`list_projects` funktioniert, liefert eine leere Liste. Passt ins Bild: deine
bisherigen HyperFrames waren lokale Dateien, keine HeyGen-Projekte.

`compose` und `render_video` sind laut Anbieter-Beschreibung **für
CLI-Clients wie diesen deaktiviert** — mit dem ausdrücklichen Hinweis,
stattdessen die lokalen Skills zu nutzen. Genau die laufen jetzt.

**Ungetestet gelassen, mit Absicht:** `compose` löst einen Cloud-Render aus,
und der kostet. Ob die Sperre für diese Session wirklich greift, sage ich
erst nach deinem Okay — nicht auf deine Rechnung geraten.

Brauchen wir ohnehin nur, wenn ein Projekt in `app.heygen.com` liegen soll,
zum Teilen oder Weiterbearbeiten. Für die Videoproduktion reicht lokal.

### Noch ein Fund: Whisper ist eingebaut

`hyperframes init --audio <datei>` **transkribiert beim Anlegen** —
Modellauswahl `tiny.en`, `base.en`, `small.en`, `medium.en`, `large`,
dazu `--language`.

Das ist vermutlich der Weg, an den du dich erinnert hast. Damit gibt es für
Hooks jetzt **zwei** geprüfte Wege: Descript (`srt` mit Zeitmarken) und
HyperFrames-CLI mit Whisper.

### Die Regel, die daraus folgt

Bevor ich ein Werkzeug ausschließe, prüfe ich beide Ebenen:
1. Ist es im Werkzeugbestand vorhanden — Connector, Skill, Modellliste?
2. Ist es **von hier** ausführbar — Key gesetzt, Host erreichbar?

Und eine dritte Frage, die ich ganz vergessen hatte:
3. **Lässt es sich hier nachinstallieren?**

Genau daran ist die HyperFrames-Einschätzung gescheitert. Ich habe einen
Ordner durchsucht, nichts gefunden und daraus „geht nicht" gemacht — statt
`npx skills add` zu versuchen, was in der Anbieter-Beschreibung sogar
danebenstand. Nicht suchen und schließen, sondern versuchen.

---

## Was kostet was — geprüft am 27.08.

Quelle: die Anbieter-Doku, die mit den Skills ausgeliefert wird
(`hyperframes-cli/references/cloud.md`, `preview-render.md`, `lambda.md`).
Die Website `hyperframes.heygen.com` ist von hier nicht erreichbar.

**Deine Aussage: „Nur Rendern kostet Geld, das Erstellen nicht."**
→ **Im Kern richtig. Zwei Präzisierungen.**

| Schritt | Geld bei HeyGen | Token | Beleg |
|---|---|---|---|
| Projekt anlegen, Komposition schreiben | **nein** | **ja** — das Schreiben ist die Arbeit | Testlauf lief ohne Anmeldung, `~/.heygen` existiert nicht |
| `hyperframes render` **lokal** | **nein** | fast keine | Doku: „(local): fastest iteration loop, use while authoring". Kein Credit-Hinweis. Mein Render lief ohne Konto durch |
| `hyperframes cloud render` | **ja** | fast keine | Doku wörtlich: „HeyGen runs the render and you **pay per credit**" |
| `hyperframes lambda render` | ja, an AWS | fast keine | „Lambda billing is per-invocation + duration" |
| `hyperframes cloudrun render` | ja, an GCP | fast keine | „billing enabled" vorausgesetzt |
| `hyperframes publish` | **unklar** | keine | Lädt Quellen hoch, gibt öffentliche URL. Kein Credit-Hinweis in der Doku — heißt nicht „kostenlos", nur „steht nicht da" |

### Präzisierung 1 — deine Aussage ist zu vorsichtig

Nicht „Rendern kostet", sondern **Cloud-Rendern kostet.**
Der lokale Render braucht kein HeyGen-Konto: Chromium und FFmpeg laufen hier
im Container. Belegt dadurch, dass mein Testrender ohne jede Anmeldung
durchlief — `~/.heygen/credentials` gibt es nicht.

Für die Videoproduktion heißt das: **iterieren so oft wie nötig, ohne Kosten.**
Die Cloud brauchen wir nur, wenn eine Komposition hier zu groß oder zu lang
wird, oder wenn ein Projekt in `app.heygen.com` liegen soll.

### Präzisierung 2 — Token und Geld sind zwei verschiedene Achsen

Sie verhalten sich sogar gegenläufig:

- **Erstellen** kostet Token (ich schreibe die Komposition), aber kein Geld
- **Lokal rendern** kostet weder Token noch Geld, nur Rechenzeit
- **Cloud rendern** kostet Geld, aber kaum Token

Der teure Teil in Token ist also genau der, den du für kostenlos gehalten hast —
und umgekehrt.

### Korrektur an mir

Ich hatte geschrieben, das MCP-Werkzeug `compose` löse einen
kostenpflichtigen Cloud-Render aus. **Das war eine Annahme, kein Beleg.**
Die Anbieter-Beschreibung trennt Authoring (`compose`) und Rendering
(`render_video`) als zwei Schritte — was eher für deine Lesart spricht.

Ob ein `compose`-Aufruf allein schon Credits zieht, steht in keiner Quelle,
die ich gesehen habe. Der Connector ist gerade nicht verbunden, ich kann das
Schema nicht nachlesen. **Bleibt offen** — brauchen wir für die
Videoproduktion aber ohnehin nicht, weil lokal reicht.

---

## Nachtrag 27.08., Abend — HeyGen und HyperFrames in *dieser* Session

Am selben Tag geprüft, mit gegenteiligem Ergebnis als am Nachmittag —
**weil es ein anderer Container ist:**

| Prüfung | Ergebnis |
|---|---|
| `which ffmpeg ffprobe` | nicht vorhanden |
| `~/.claude/skills/` | nur `session-start-hook` und `synced`. **Keine hyperframes-Skills** |
| `~/.heygen` | existiert nicht |
| `HEYGEN_*`, `FAL_KEY` in der Umgebung | nicht gesetzt |

Das widerspricht dem Eintrag oben nicht. Dort steht ausdrücklich: **„Der
Container ist flüchtig. Beides ist nach einer neuen Session wieder weg."**
Genau das ist eingetreten.

**Nachinstallierbar, am 27.08. nachmittags end-to-end belegt:**
```
npx skills add heygen-com/hyperframes
apt-get install -y ffmpeg
```
Kostet ein paar Minuten und keine Credits.

### Die Grenze, die dadurch nicht verschwindet

HyperFrames rendert **programmierte HTML-Videos**. Ein sprechender Avatar
ist etwas anderes:

| Was | Von hier |
|---|---|
| Animiertes HTML-Video, lokal gerendert | **geht**, nach Nachinstallation, kostenlos |
| Sprachausgabe über `hyperframes-media` (TTS) | **ungeprüft**, ob ohne HeyGen-Konto |
| **Sprechender Avatar** („Mike") | **geht nicht von hier.** Das ist ein HeyGen-Produkt, braucht Konto und Credits |
| MCP-Werkzeuge `compose` und `render_video` | vom Anbieter **für CLI-Clients wie diesen gesperrt**, mit Verweis auf die lokalen Skills |

Für ein Promo-Video mit einem sprechenden Avatar heißt das: Der Avatar
entsteht in Marianas HeyGen-Konto, nicht hier. Ich liefere Skript,
Sprechtext und die animierten Einblendungen.
