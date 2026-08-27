# Was noch fehlt — und was nicht

Stand: 2026-08-27

---

## Kurz: ein API-Key. Sonst nichts.

Für die anstehende Arbeit — Content-Struktur, drei Einheiten, Recherche-Agent —
fehlt genau ein Zugang: **ein YouTube-Data-API-Key.**

Alles andere ist geprüft vorhanden: Airtable mit Schreibrechten, Google Drive,
Descript, Canva, HubSpot, Gmail, Kalender, HyperFrames lokal lauffähig.

---

## YouTube: kein Connector nötig, ein Key reicht

**Apify brauchen wir dafür nicht.** Begründung:

| | YouTube Data API v3 | Apify |
|---|---|---|
| Offiziell vom Anbieter | ja | nein, Scraping |
| Kosten | kostenlos, 10.000 Einheiten am Tag | pro Lauf |
| Von hier erreichbar | **ja** — `googleapis.com` antwortet | **nein** — `api.apify.com` nicht erreichbar |
| Nutzungsbedingungen | eingehalten | Grauzone |
| Liefert was wir brauchen | Views, Titel, Description, Thumbnails, Kanaldaten, Kommentare | dasselbe |

Die API gibt alles her, was in `agenten/recherche-agent-content.md` gebraucht
wird. Ein Scraper daneben wäre teurer, riskanter und brächte nichts dazu.

**So kommst du an den Key** (Standardweg; die Doku-Seite selbst ist von hier
blockiert, deshalb nicht Schritt für Schritt nachgeprüft):
Google Cloud Console → Projekt anlegen → „YouTube Data API v3" aktivieren →
Anmeldedaten → API-Schlüssel erstellen. Kostenlos, keine Kreditkarte.

Den Key nicht in den Chat schreiben — als Umgebungsvariable setzen oder in
einer Datei ablegen, die nicht im Repository landet.

Damit kann ich den Recherche-Agenten hier **bauen und gegen echte Daten
testen**, statt ihn zu beschreiben.

---

## Apify: nur für einen Fall interessant

Nicht für YouTube. Der einzige Ort, an dem es etwas löst, ist **LinkedIn** —
dort gibt es keine offizielle API für fremde Beiträge.

**Das Argument dafür:** Apify fährt die Scraper auf eigener Infrastruktur mit
eigenen Proxys. Das Sperr-Risiko läge damit nicht mehr auf deinem
LinkedIn-Konto.

**Die Argumente dagegen:**
- Dein bestehender Weg läuft bereits — die Akquise-Agenten lesen über deine
  Sitzung, und du hast die Mengengrenzen dafür akzeptiert
- LinkedIn geht gegen Scraping-Anbieter vor. Ein Dienst, der heute funktioniert,
  kann morgen leer zurückkommen
- **Datenschutz:** Beim Scrapen von Personendaten über einen Dienstleister
  bleibst du die Verantwortliche im Sinne der DSGVO, brauchst also einen
  Auftragsverarbeitungsvertrag. Das ist eine Rechtsfrage, keine technische
- Kosten pro Lauf statt einmalig

**Prüfstand:** Ich kann Apify von hier **nicht** prüfen. Kein Connector im
Verzeichnis, `api.apify.com` und `mcp.apify.com` sind nicht erreichbar.
Alles, was ich zu deren Actors sagen würde, käme aus der Websuche — also aus
zweiter Hand.

**Empfehlung:** Erst wenn der LinkedIn-Scanner an eine Mengengrenze stößt,
die dein Konto gefährdet. Vorher ist es eine Lösung ohne Problem.

Wichtig für die Einordnung: **Connectoren laufen nicht über den
Container-Egress.** Airtable ist per Connector nutzbar, obwohl `airtable.com`
per curl nicht erreichbar ist. Ein Apify-Connector könnte also funktionieren,
auch wenn curl scheitert — im Verzeichnis steht aber keiner.

---

## Weiterhin offen, aber nicht blockierend

Diese vier stehen seit der ersten Prüfung offen und halten nichts auf,
solange wir bei Content und Drehvorbereitung sind:

1. Worauf läuft die Website — WordPress? Entscheidet, wie die Landingpage entsteht
2. Zahlungsweg für den Workshop
3. Womit nimmst du den Bildschirm auf
4. Buchung und Kalender — Google Calendar ist verbunden, ob du damit buchen
   lassen willst, ist offen

Gebraucht werden sie erst, wenn der Termin steht.


---

## Nachtrag 27.08. — Apify-Verbindung kommt hier nicht an

Geprüft direkt nach deiner Meldung:

| Prüfung | Ergebnis |
|---|---|
| `ListConnectors` mit Stichwort „apify" | leer |
| `ListConnectors` ohne Filter, alle 12 Connectoren | **Apify nicht dabei** |
| `ToolSearch` nach apify, actor, dataset, scraper | keine Apify-Werkzeuge |

Apify steht also weder auf Konto-Ebene noch in diesem Chat zur Verfügung.

### Dabei aufgefallen: HyperFrames ist stumm geschaltet

`HyperFrames by HeyGen` ist gelistet mit `connected: true`, aber
**`enabledInChat: false`**. Deshalb sind die Werkzeuge nach ein paar Zügen
verschwunden.

**Connectoren haben zwei Schalter:**
1. `connected` — auf Kontoebene verbunden
2. `enabledInChat` — für diesen Chat freigeschaltet

Beides muss an sein. Das ist vermutlich auch bei Apify der Punkt.

### Was zu tun ist

In den Connector-Einstellungen **dieses Chats** nachsehen, ob Apify dort
aufgeführt und aktiviert ist. Falls es nur auf Kontoebene verbunden wurde,
fehlt der zweite Schalter.

HyperFrames muss nicht zurückgeholt werden — die lokalen Skills laufen hier
und decken Bauen und Rendern ab.

### Und die Einordnung von vorher bleibt

Für YouTube brauchen wir Apify nicht. Ein API-Key genügt, ist kostenlos und
regelkonform. Apify wäre nur für LinkedIn interessant — und dort erst, wenn
die Menge dein Konto gefährdet.

Kein Grund zur Eile also. Der YouTube-Key bringt uns weiter, Apify nicht.


---

## Nachtrag 2 — Apify ist installiert, aber als Desktop-Erweiterung

Der Screenshot löst den Widerspruch auf. Die Überschrift lautet
**„Auf deinem Computer installiert"**. Apify steht dort neben
Control Chrome, Filesystem, PowerPoint und Word.

Das sind **Desktop-Erweiterungen** (`.mcpb` / `.dxt`), installiert in der
Claude-Desktop-App auf deinem Mac. Sie laufen dort — nicht in einer
Remote-Session in der Cloud.

Erkennbar auch daran, was sonst in der Liste steht: „Control Chrome" und
„Filesystem" steuern *deinen* Browser und *dein* Dateisystem. Von einem
Cloud-Container aus ergibt das gar keinen Sinn.

**Drei Ebenen, nicht zwei:**

| Ebene | Wo installiert | Erreicht Remote-Sessions |
|---|---|---|
| claude.ai-Connectoren | Konto | **ja** — Airtable, Drive, Descript, Canva … |
| Desktop-Erweiterungen (`.mcpb`/`.dxt`) | Mac, Desktop-App | **nein** — Apify, Control Chrome, Filesystem |
| Lokale Skills und CLI | Mac bzw. per `npx` nachinstallierbar | teils — HyperFrames ließ sich hier nachinstallieren |

### Wenn Apify auch in Remote-Sessions verfügbar sein soll

Dann nicht als Desktop-Erweiterung, sondern als **Connector auf claude.ai**
mit der Server-Adresse `https://mcp.apify.com`, Anmeldung per OAuth beim
ersten Aufruf.

**Quelle: nur Websuche** (Apify-Doku, `docs.apify.com`). Von hier aus konnte
ich das nicht am Dienst selbst prüfen — die Adresse ist über den
Container-Egress nicht erreichbar, was für einen Connector aber nichts
bedeutet.

### Ob sich das lohnt

Für den aktuellen Plan nicht. Apify wird nur für LinkedIn gebraucht, und
dort erst, wenn die Menge dein Konto gefährdet. Für YouTube ist die
offizielle API besser.

**Praktischer:** Wenn Apify-Arbeit ansteht, in einer lokalen Session
arbeiten. Dort ist es bereits eingerichtet.
