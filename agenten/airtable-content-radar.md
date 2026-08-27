# Airtable "Content_Radar" — Aufbau

Datum: 2026-08-27. Status: Vorschlag, noch nicht angelegt.
Eine Base für beide Plattformen. Nachfolger des abgeschafften Kanal-Scanners.

---

## Warum eine Base und nicht zwei

YouTube und LinkedIn liefern verschiedene Kennzahlen, aber dieselbe Frage:
was hat funktioniert und warum. Zwei Systeme heißt zweimal bewerten und nie
vergleichen können. Plattform ist ein Feld, keine Base.

---

## Tabelle 1 — `Quellen`

Ein Datensatz je Kanal oder Person.

| Feld | Typ | Anmerkung |
|---|---|---|
| Name | Text | |
| Plattform | Auswahl | YouTube / LinkedIn |
| URL | URL | |
| Größe | Zahl | Abonnenten bzw. Follower |
| Kategorie | Auswahl | Akquise / Automation / Plattform-Praxis / Positionierung |
| Warum drin | Text | ein Satz — verhindert Sammeln ohne Grund |
| Median-Kennzahl | Zahl | Basis der Outlier-Ratio, je Lauf neu berechnet |
| Letzter Lauf | Datum | |
| Status | Auswahl | aktiv / pausiert / raus |
| Aufgenommen am | Datum | |

Quartalsweise durchsehen. Wer dreimal keinen Outlier geliefert hat: auf `raus`.

---

## Tabelle 2 — `Beiträge`

Ein Datensatz je Video oder Post. Nur Outlier landen hier.

| Feld | Typ | YT | LI |
|---|---|---|---|
| Quelle | Verknüpfung → `Quellen` | ✓ | ✓ |
| Plattform | Auswahl | ✓ | ✓ |
| Titel / Erste Zeile | Text | ✓ | ✓ |
| URL | URL | ✓ | ✓ |
| Veröffentlicht | Datum | ✓ | ✓ |
| Kennzahl | Zahl | Views | Reaktionen + 3× Kommentare |
| **Outlier-Ratio** | Formel | ✓ | ✓ |
| Format | Auswahl | Long / Short | Text / Bild / Karussell / Video / Dokument |
| Länge | Zahl | Sekunden | Zeichen |
| Thumbnail | Anhang | ✓ | — |
| TN-Muster | Mehrfachauswahl | Gesicht / Text / Zahl / Kontrast / Blick | — |
| Hook | Langtext | erste 30 Sek, diktiert | erste 2 Zeilen |
| Hook-Typ | Auswahl | Frage / Behauptung / Zahl / Widerspruch / Vorher-Nachher | ✓ |
| Volltext | Langtext | Description | Post-Text |
| CTA | Text | ✓ | ✓ |
| CTA-Position | Auswahl | Anfang / Mitte / Ende / keiner | ✓ |
| Top-Kommentare | Langtext | ✓ | ✓ |
| Übertragbar auf DACH | Auswahl | ja / teilweise / nein | ✓ |
| Warum nicht | Text | nur bei „nein" | ✓ |
| Status | Auswahl | neu / ausgewertet / verworfen / übernommen | ✓ |

**Outlier-Ratio als Formel**, nicht als getippte Zahl. Sonst rechnet niemand nach.

Ansicht `Muster`: gruppiert nach Hook-Typ und Plattform, sortiert nach
Durchschnitts-Ratio. Erst wenn diese Ansicht nicht mehr reicht, wird daraus
eine eigene Tabelle.

---

## Tabelle 3 — `Themen-Kandidaten`

Die Ausgabe. Genau das Format der Datei „lose Video-Ideen", damit nichts
umgeschrieben werden muss.

| Feld | Typ |
|---|---|
| Titel | Text |
| Zielperson + Schmerz | Langtext |
| Kernbotschaft | Langtext |
| Angebotsbezug | Langtext |
| Kernthema | Auswahl (1 / 2 / 3 aus `video-ideas`) |
| Belege | Verknüpfung → `Beiträge` |
| Status | Auswahl: Vorschlag / übernommen / verworfen |
| Verworfen weil | Text |

`Verworfen weil` ist der Lernteil. Nach zwanzig Ablehnungen steht dort, welche
Art Vorschlag nie passt — und der Agent bekommt die Regel.

---

## Ablauf pro Woche

1. YouTube-Lauf (API) → neue Datensätze in `Beiträge`
2. LinkedIn-Lauf (Browser, anderer Tag) → neue Datensätze in `Beiträge`
3. Hooks der 10–15 stärksten Outlier nachtragen, YouTube diktiert
4. Ansicht `Muster` durchsehen: was lief diese Woche über alle Quellen hinweg
5. Agent schlägt 3–5 `Themen-Kandidaten` vor
6. Freigabe → in die Datei „lose Video-Ideen", von dort übernimmt `video-ideas`

Der Radar endet bei Schritt 6. Er erfindet keine Konzepte.

---

## Abgrenzung zum alten Kanal-Scanner

Der `kanal_scanner` wurde in `video-ideas` abgeschafft, weil er Themen
automatisch erzeugt hat. Ideen entstehen aber im Gespräch, ausgehend vom
Schmerz eines Geschäftsführers — nicht aus dem Ranking eines fremden Kanals.

Der Radar macht deshalb ausdrücklich etwas anderes: Er liefert **Mechanik und
Belege**, keine fertigen Themen. Die Spalte „Übertragbar auf DACH" ist die
Stelle, an der der alte Fehler abgefangen wird.
