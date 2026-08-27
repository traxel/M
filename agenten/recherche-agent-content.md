# Recherche-Agent Content — YouTube + LinkedIn

Datum: 2026-08-27. Status: Vorschlag, noch nicht gebaut.
Sprache der Quellen: zunächst nur Englisch.

---

## Einordnung

Zwei Agenten im Content-System:

1. **Recherche-Agent** — was funktioniert draußen, und warum (dieses Dokument).
   Zwei Läufe auf einer Ablage: YouTube über die API, LinkedIn über den
   bestehenden Browser-Weg der Akquise-Agenten.
2. **Content-Agent** — Kern + Zweig Text (LinkedIn) / Zweig Video
   (`agenten/content-agent.md`)

Der Workshop bleibt bei fünf Agenten. Die zwei Zweige betreffen nur das
Content-System.

---

## Warum "mehr als 1000 Views" das falsche Kriterium ist

Ein Kanal mit 500.000 Abonnenten macht mit einem schlechten Video 1.000 Views.
Ein Kanal mit 8.000 Abonnenten macht mit einem sehr guten Video 1.000 Views.
Dieselbe Zahl, gegensätzliche Aussage.

**Richtiges Maß: Outlier-Ratio.**

```
Outlier-Ratio = Views des Videos ÷ Median-Views der letzten 30 Videos desselben Kanals
```

- ≥ 2,0 → Outlier. Hier haben Hook, Titel und Thumbnail gearbeitet.
- 0,8–1,5 → Normalfall des Kanals. Uninteressant.
- ≤ 0,5 → Flop. Auch lehrreich, aber später.

Nur Videos mit Ratio ≥ 2,0 und einem Alter zwischen 14 und 365 Tagen werden
ausgewertet. Jünger als 14 Tage ist noch nicht eingelaufen.

Das ist das einzige Kriterium, das über Kanalgrößen hinweg vergleichbar ist.

---

## YouTube: offizielle API, kein Scraping

Die YouTube Data API v3 liefert alles Nötige — kostenlos, 10.000 Einheiten am Tag,
ohne Regelverstoß:

| Gebraucht | Quelle |
|---|---|
| Videos je Suchbegriff | `search.list` |
| Views, Likes, Kommentarzahl | `videos.list` (statistics) |
| Titel, Description, Tags, Veröffentlichung | `videos.list` (snippet) |
| Thumbnail in voller Auflösung | `videos.list` (snippet.thumbnails.maxres) |
| Abonnenten, Videozahl des Kanals | `channels.list` |
| Kommentare | `commentThreads.list` |

**Kein Scraping nötig. Kein Konto-Risiko.**

Eine Einschränkung, offen benannt: **Transkripte fremder Videos gibt die API nicht
her** (`captions.download` funktioniert nur für eigene Videos). Der Hook steckt aber
in den ersten 30 Sekunden.

Lösung ohne Grauzone: Der Agent liefert wöchentlich die 10–15 stärksten Outlier
mit Zeitstempel-Link. Die ersten 30 Sekunden werden angesehen und diktiert —
15 Videos × 30 Sekunden = 8 Minuten Handarbeit pro Woche. Dafür sauber.

---

## LinkedIn: eigener Scanner über den bestehenden Weg

Es gibt keine offizielle API für fremde Beiträge. Aber die Akquise-Agenten
erreichen LinkedIn-Profile bereits — derselbe Weg, dieselbe Sitzung. Ein
Content-Scanner ist kein neues Verfahren, sondern eine zweite Auswertung auf
demselben Zugang.

Also gebaut, aber begrenzt.

### Was der Scanner tut

1. Liest die Tabelle `Quellen`, Plattform LinkedIn — Personen, denen bewusst
   gefolgt wird
2. Öffnet die Beitragsübersicht des Profils, liest die letzten Beiträge
3. Ermittelt je Beitrag: Text, Datum, Reaktionen, Kommentare, Format
   (Text / Bild / Karussell / Video / Dokument)
4. Berechnet die Outlier-Ratio gegen den Median derselben Person
5. Legt Outlier als Datensatz in `Beiträge` an

Er schreibt nichts, er reagiert nicht, er vernetzt nicht. Nur lesen.
Die Regel „kein Agent klickt auf Senden" bleibt unberührt — Lesen ist die
risikoärmere Hälfte.

### Kennzahl auf LinkedIn

Views gibt es für fremde Beiträge nicht. Ersatz:

```
Interaktion = Reaktionen + (3 × Kommentare)
Outlier-Ratio = Interaktion ÷ Median der letzten 20 Beiträge derselben Person
```

Kommentare zählen dreifach: sie kosten den Leser mehr und sind schwerer zu
bekommen als ein Daumen.

### Grenzen, damit das Konto ruhig bleibt

Nicht die Handlung führt zu Beschränkungen, sondern die Menge und das Tempo.

| | |
|---|---|
| Quellen gesamt | max. 30 |
| Lauf | 1× pro Woche, nicht täglich |
| Profile je Lauf | max. 10 |
| Beiträge je Profil | die letzten 5 |
| Tempo | menschlich, mit Pausen, nacheinander |
| Reichweite | nur Personen, denen gefolgt wird oder mit denen Vernetzung besteht |
| Terminlage | **nicht am selben Tag wie ein großer Akquise-Lauf** |

Der letzte Punkt ist der wichtige: Akquise-Agenten und Content-Scanner laufen
über dasselbe Konto. Die Last addiert sich. Getrennte Tage, nicht getrennte
Agenten, lösen das.

### Zusätzlich, ohne jedes Risiko

Der eigene Analytics-Export. Was bei Sometra selbst funktioniert, ist das
einzige Signal mit echten Zahlen und gehört in dieselbe Tabelle.

### Für den Workshop gilt etwas anderes

Im Workshop wird die kuratierte Variante gezeigt, nicht der automatisierte
Scanner. Eigenes Konto, eigenes Risiko, geringe Menge — das ist eine
Entscheidung, die jeder für sich trifft. Zwölf Teilnehmern gleichzeitig
beizubringen, Profile automatisiert abzugreifen, ist eine andere Sache.

---

## Wie die relevanten YouTube-Creator gefunden werden

Die frühere Kanalliste ist raus — der `kanal_scanner` wurde in `video-ideas`
bewusst abgeschafft. Eine feste Liste veraltet und verengt. Was bleibt, ist eine
Suchmethode, die die Liste jedes Quartal neu erzeugt.

**Schritt 1 — Seed-Begriffe (englisch)**

Entlang der drei Kernthemen aus `video-ideas`:

- Akquise ohne Personal: `AI SDR`, `AI cold outreach`, `automated lead generation`,
  `AI prospecting workflow`
- Entlastung bei ausgelastetem Personal: `AI agents for sales teams`,
  `sales automation without code`, `AI workflow automation business`
- Bestandskunden: `AI customer research`, `account intelligence AI`
- Plattform-nah: `Claude projects workflow`, `ChatGPT projects business`,
  `n8n automation business`, `AI agency workflow`

**Schritt 2 — Kandidaten sammeln**
Je Begriff die Top-Ergebnisse der letzten 12 Monate nach Views. Kanäle notieren,
die bei mehreren Begriffen auftauchen. Mehrfachnennung ist das erste Qualitätssignal.

**Schritt 3 — Kanalfilter**

| Kriterium | Schwelle | Warum |
|---|---|---|
| Abonnenten | 10.000 – 500.000 | Darunter zu wenig Signal, darüber anderes Spiel |
| Veröffentlichungen | ≥ 1 Video pro Monat | Tote Kanäle lehren nichts über heute |
| Thema | ≥ 60 % Umsetzung, nicht Nachrichten | "OpenAI hat X veröffentlicht" ist keine Mechanik |
| Format | erklärt an Beispielen | Talking-Head-Meinung liefert keine übertragbare Struktur |

Ziel: **15–25 qualifizierte Kanäle.** Mehr wird nicht ausgewertet.
Quartalsweise nachziehen, nicht wöchentlich.

**Schritt 4 — bereits gesetzter Anker**
Ben AI ist bereits Referenz: die vier Thumbnail-Muster in `mariana-thumbnail`
stammen von dort. Der Kanal gehört gesetzt in die Liste — die Muster sind schon
im Einsatz, jetzt kommen die Zahlen dazu.

Keine weiteren Namen an dieser Stelle. Abonnentenzahlen und Themenschwerpunkte
ändern sich; der erste Lauf liefert die geprüfte Liste mit aktuellen Werten,
statt eine aus dem Gedächtnis geratene.

---

## Was pro Outlier-Video erfasst wird

| Feld | Herkunft |
|---|---|
| Kanal, Abonnenten | API |
| Titel | API |
| Views, Median des Kanals, **Outlier-Ratio** | API, berechnet |
| Veröffentlichung, Länge | API |
| Thumbnail-Bild | API |
| **Thumbnail-Muster** | Auswertung: Gesicht ja/nein, Textmenge, Kontrast, Zahl im Bild, Blickrichtung |
| **Hook (erste 30 Sek)** | manuell diktiert |
| **Hook-Typ** | Auswertung: Frage, Behauptung, Zahl, Widerspruch, Vorher-Nachher |
| Description: Aufbau, erste Zeile, Links, CTA-Position | API |
| CTA im Video | manuell, aus dem Hook-Durchgang |
| Kapitel / Struktur | API (Description-Zeitmarken) |
| Top-Kommentare | API |

Die Top-Kommentare sind der unterschätzte Teil. Dort steht, was die Zuschauer
nicht verstanden haben — und das ist das nächste Video.

---

## Was der Agent ausgibt

Nicht eine Tabelle mit 200 Zeilen. Einmal pro Woche:

1. **Die 10–15 stärksten Outlier**, sortiert nach Ratio
2. **Muster statt Einzelfälle**: welcher Hook-Typ, welches Thumbnail-Muster,
   welche Videolänge diese Woche überdurchschnittlich lief
3. **Was davon auf den DACH-Mittelstand übertragbar ist** — und was nicht
4. **3–5 Themenvorschläge** in das Format der Datei „lose Video-Ideen"
   (Titel / Zielperson + Schmerz / Kernbotschaft / Angebotsbezug)

Punkt 4 ist die Schnittstelle: Der Recherche-Agent endet dort, wo `video-ideas`
anfängt. Er erfindet keine Konzepte, er liefert Kandidaten.

---

## Übertragungsregel Englisch → Deutsch

Übernommen wird die **Mechanik**, nicht die Aussage.

- Übertragbar: Hook-Typ, Thumbnail-Aufbau, Videolänge, Kapitelstruktur,
  CTA-Position, Aufbau der Description
- Nicht übertragbar: Zahlenversprechen, Hustle-Ton, "I made $50k with AI agents"
- Härtetest vor jeder Übernahme: Würde ein Geschäftsführer aus dem Mittelstand
  das anklicken, ohne sich fremdzuschämen?

Die englischen Kanäle bedienen Solo-Selbstständige. Der ICP ist ein anderer.
Formate reisen. Behauptungen nicht.

---

## Zu entscheiden

1. Fester Wochentag für den YouTube-Lauf und für den LinkedIn-Lauf —
   und die müssen auseinanderliegen, siehe Terminlage oben.
2. Startliste LinkedIn: 20–30 englischsprachige Accounts. Kommt aus dem ersten
   Lauf plus deiner eigenen Auswahl.
3. Ob `Muster` eine eigene Tabelle bleibt oder eine Ansicht auf `Beiträge` ist.
   Empfehlung: erst als Ansicht starten, Tabelle nur wenn die Bewertung
   ausufert.
