# YouTube-API-Key — woher

Stand: 2026-08-27

---

## Was ich selbst geprüft habe

Der Aufruf gegen die echte API, aus dieser Session:

```
GET https://www.googleapis.com/youtube/v3/videos?part=statistics&id=…
```

Antwort von Google, wörtlich:

> „Method doesn't allow unregistered callers (callers without established
> identity). Please use **API Key** or other form of API consumer identity
> to call this API."  — HTTP 403, `PERMISSION_DENIED`

Belegt damit zweierlei:
1. Die API ist **von hier erreichbar** — es fehlt nur die Identität
2. Ein **API-Key** ist das, was fehlt (kein OAuth nötig für öffentliche Daten)

## Was ich nicht prüfen konnte

`console.cloud.google.com`, `developers.google.com` und
`docs.cloud.google.com` sind vom Egress-Proxy blockiert. Den Klickweg in der
Console konnte ich also **nicht an der Primärquelle nachlesen**.

---

## Der Weg — Quelle: Websuche, nicht Google direkt

Mehrere übereinstimmende Anleitungen beschreiben denselben Ablauf:

1. `console.cloud.google.com` öffnen, mit Google-Konto anmelden
2. Ein **Projekt** anlegen (oder ein vorhandenes wählen)
3. **APIs & Dienste → Bibliothek** → nach „YouTube Data API v3" suchen → **Aktivieren**
4. **APIs & Dienste → Anmeldedaten** → **Anmeldedaten erstellen → API-Schlüssel**
5. Schlüssel kopieren

Angaben aus denselben Quellen: kostenlos, keine Kreditkarte nötig,
10.000 Kontingenteinheiten am Tag.

**Diese Schritte sind zweiter Hand.** Sollte die Console anders aussehen,
ist die Beschreibung veraltet — nicht du hast etwas falsch gemacht.

---

## Sicherheit

- **Schlüssel einschränken** auf die YouTube Data API v3, nicht offen lassen
  (in der Console beim Schlüssel unter „API-Einschränkungen"). Ein offener
  Schlüssel gilt für alles, was im Projekt aktiviert ist.
- **Nicht in den Chat schreiben.** Er stünde dauerhaft im Verlauf.
- Er lässt sich jederzeit löschen und neu erstellen.

## Wie er zu mir kommt — drei Wege

| Weg | Bewertung |
|---|---|
| **Umgebungsvariable in den Umgebungs-Einstellungen** dieser Remote-Umgebung | sauberster Weg, steht in keinem Verlauf |
| Datei in Google Drive, ich lese sie über den Connector, du löschst sie danach | funktioniert, ich habe Drive-Zugriff |
| In den Chat schreiben | geht, steht dann aber dauerhaft im Verlauf. Nur wenn der Schlüssel eingeschränkt ist und du ihn danach ersetzt |

---

## Die eigentliche Prüfung kommt danach

Sobald der Schlüssel da ist, rufe ich die API hier auf und zeige dir echte
Zahlen zu einem echten Kanal — Views, Median, Outlier-Ratio.

Dann ist belegt, dass der Recherche-Agent funktioniert, statt dass ich es
behaupte.


---

## Nachtrag: Nein, wir hatten nie einen Key

Geprüft am 27.08., in dieser Reihenfolge:

| Prüfung | Ergebnis |
|---|---|
| Umgebungsvariablen dieser Session | kein YouTube-/Google-Key. Nur `CLOUDSDK_*` der Plattform |
| Das GCP-Token gegen die YouTube-API getestet | **401 Invalid Credentials** — gehört nicht zu deinem Konto |
| `.env`-, Credential-, Secret-Dateien in Home und Repo | keine |
| Drive nach `kanal_scanner` durchsucht | gefunden |

### Der alte Scanner sagt es selbst

In `weekly_kanal_scanner_runner.py` (106 KB, Drive-ID
`19pRni3QwrFjUjMI5ARUF9cmGo23ZWNbP`) steht im Kopf wörtlich:

> „**Keine YouTube Data API. Keine YouTube Transcript API.**
> Kein Caption-Abruf als Standard."

So lief er stattdessen:
- Kanäle aus einem Google Sheet, Tab „Kanäle"
- Neue Long-Videos über **RSS-Feeds** mit gesetztem User-Agent, `yt-dlp` als Rückfall
- Transkription über **yt-dlp-Audio + OpenAI Speech-to-Text**
- Sheets und Drive über ein **Service-Account-JSON**

Die `.env` verlangte: `OPENAI_API_KEY`, `GOOGLE_CREDENTIALS_PATH`,
`GOOGLE_SHEET_ID` und zwei Drive-Ordner-IDs. **Kein YouTube-Key darunter.**

Die Zugangsdaten liegen auf deinem Mac:
`/Users/marianatheux/Library/Application Support/yt_scanner/google_credentials.json`

### Und er lief lokal, nicht hier

Von dieser Umgebung aus: `youtube.com` und die RSS-Adresse sind **nicht
erreichbar** (000), `yt-dlp` fehlt, `OPENAI_API_KEY` ist nicht gesetzt.
Der alte Weg ist von hier also gar nicht gangbar.

### Warum der Key trotzdem gebraucht wird — nicht aus Bequemlichkeit

Der alte Scanner war nie auf Kennzahlen ausgelegt. Seine Spalten:
Video-ID, Kanal, Titel, VÖ-Datum, URL, Kapitel, Zusammenfassung, Kategorie,
Score, Themenbereich, Transfer, Go/NoGo, Priorität, Status …

**Keine Views. Keine Kanal-Kennzahlen.** Er hat Inhalte zusammengefasst und
bewertet — nicht gemessen, was funktioniert hat.

Die Outlier-Ratio aus `agenten/recherche-agent-content.md` braucht Views des
Videos und den Median des Kanals. Beides liefert nur die Data API.

**Damit ist der Unterschied klar:** Der alte Scanner beantwortete „worum geht
es in diesen Videos". Der neue soll beantworten „was hat funktioniert und
warum". Das ist eine andere Frage und braucht andere Daten.
