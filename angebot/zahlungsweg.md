# Zahlungsweg für den Workshop

Stand: 2026-08-27. Status: Vorschlag zur Entscheidung.

---

## Was der Weg können muss

| Anforderung | Woher |
|---|---|
| **Zahlung bei Buchung** | Marianas Vorgabe. Der Platz ist erst weg, wenn das Geld da ist |
| **Rechnung mit allen Pflichtangaben** | Käufer sind Firmen. Ohne Rechnung kein Vorsteuerabzug, ohne Vorsteuerabzug keine Freigabe |
| **19 % deutsche Umsatzsteuer** | Präsenzveranstaltung in Deutschland, siehe unten |
| **Rechnung auf die Firma, nicht auf die Person** | Der GF bucht, die Buchhaltung bezahlt |
| **Stornoregel** | Präsenz. Ein leerer Platz kostet Raum und Catering |

---

## Was ich prüfen konnte — und was nicht

**Geprüft, am Werkzeugbestand dieser Session:**
Es gibt **keinen Zahlungs-Connector**. Verbunden sind Airtable, Canva,
Descript, Gmail, Google Calendar, Google Drive, Granola, HubSpot,
Microsoft 365, Zoom, HyperFrames. Kein Stripe, kein Mollie, nichts
Vergleichbares. Das deckt sich mit `verifiziert.md`, wo der Zahlungsweg
seit Beginn als ungeklärt steht.

**Nur Websuche, ausdrücklich nicht am Dienst geprüft:**
Alles unten zu Gebühren, Funktionsumfang und Fristen. Die Anbieterseiten
sind aus diesem Container nicht erreichbar, ein Konto existiert nirgends.
Vor der Entscheidung ist jede Zahl beim Anbieter selbst nachzusehen.

**HubSpot ist verbunden** und kann Angebote. Ob HubSpot Payments in
Deutschland nutzbar ist, konnte ich nicht prüfen — nach meinem Kenntnisstand
ist es auf einzelne Länder beschränkt. **Ungeprüft.**

---

## Die Optionen

### 1 — Rechnung und Überweisung, Vorkasse

Rechnung bei Buchung, zahlbar sofort und vor dem Veranstaltungstag. Der
Platz wird erst mit Zahlungseingang verbindlich.

| | |
|---|---|
| Transaktionsgebühr | **0 €** |
| Werkzeugkosten | ein Buchhaltungstool, grob 15–30 € im Monat |
| Bei 36 Plätzen | **0 € Gebühren** |
| Aufwand | manuell: Rechnung raus, Eingang prüfen, nachfassen |
| Risiko | zwischen Buchung und Zahlung ist der Platz blockiert |

Das ist der Weg, den Ihre Käufer erwarten. Ein Geschäftsführer, der
2.356 € freigibt, zieht keine Kreditkarte — er leitet die Rechnung an
die Buchhaltung weiter.

### 2 — Zahlungsanbieter mit Rechnungsfunktion (Stripe oder Mollie)

Zahlungslink oder Kasse: Karte, SEPA-Lastschrift, PayPal. Die Rechnung
erzeugt der Anbieter mit.

| | Stripe | Mollie |
|---|---|---|
| Gebühr Karte (EU) | ~1,5 % + 0,25 € | ähnlich, teils günstiger |
| Gebühr SEPA | deutlich günstiger als Karte | dito |
| Rechnung mit USt | ja, über die Rechnungsfunktion | schwächer, oft externes Tool nötig |
| Bei 2.356 € je Karte | rund **35 €** | ähnlich |
| Bei 36 Plätzen, alles Karte | rund **1.300 €** | ähnlich |

**Alle Zahlen: Websuche und Kenntnisstand, nicht am Dienst geprüft.**

Vorteil: Die Zahlung passiert bei der Buchung, nicht danach. Genau die
Vorgabe. Nachteil: Gebühren, und ein Teil der Käufer will trotzdem eine
klassische Rechnung.

### 3 — Reseller-Plattformen: Digistore24, CopeCart, elopage

Die Plattform verkauft in eigenem Namen, stellt die Rechnung und führt
die Umsatzsteuer ab.

| | |
|---|---|
| Gebühr | grob 5–7 % |
| Bei 2.356 € | **120–165 € je Platz** |
| Bei 36 Plätzen | **4.300–6.000 €** |

**Nicht empfohlen**, aus zwei Gründen:
- Der Kunde bekommt eine Rechnung von einer Firma, die er nicht kennt, für
  einen Workshop, den er bei Sometra gebucht hat. Bei 2.356 € an einen
  Mittelständler ist das erklärungsbedürftig
- Umsatzsteuerlich wird eine Präsenzveranstaltung über einen Wiederverkäufer
  komplizierter, nicht einfacher (Leistungskommission)

Diese Plattformen sind für Online-Kurse an Selbstständige gebaut, nicht
für Präsenzseminare an Firmen.

### 4 — Ticket-Plattformen: Eventbrite, XING Events, ticket i/o

Können Teilnehmerverwaltung und Rechnung, kosten pro Ticket. Optik und
Ablauf sind auf Veranstaltungen mit vielen Gästen ausgelegt. Bei zwölf
Plätzen ist das mehr Apparat als Nutzen.

---

## Wenn sofort bezahlt werden soll: Stripe

Stand 27.08.: Mariana will, dass bei der Buchung sofort bezahlt wird — nicht
Rechnung mit sieben Tagen Frist. Damit fällt der Weg ohne Anbieter weg, und
die Frage ist nur noch, welcher.

**Antwort: Stripe.** Begründung sind die Gebühren und der Umstand, dass die
Rechnung im eigenen Namen bleibt.

### Was ein Platz an Gebühren kostet

Brutto je Platz: 2.356 € × 1,19 = **2.803,64 €**

| Weg | je Platz | 36 Plätze |
|---|---|---|
| **SEPA-Lastschrift über Stripe** | **0,35 €** | **13 €** |
| Stripe, EU-Karte (1,4 % + 0,25 €) | 39,50 € | 1.422 € |
| Mollie, EU-Karte (1,8 % + 0,25 €) | 50,72 € | 1.826 € |
| PayPal direkt (rund 2,99 % + 0,39 €) | 84,22 € | 3.032 € |
| Digistore24, Standard | 150,38 € | 5.414 € |

**Alle Sätze: Websuche, nicht am Dienst geprüft.** Vor der Einrichtung beim
Anbieter nachsehen.

Der Unterschied zwischen erster und letzter Zeile ist der Punkt: **SEPA-
Lastschrift kostet 0,35 € pauschal, unabhängig vom Betrag.** Bei einem
Ticket von 2.803,64 € ist jede prozentuale Gebühr teuer und jede
Pauschalgebühr geschenkt.

### Warum Stripe und nicht Mollie

- Günstiger bei Karte, gleich bei Lastschrift
- Rechnungsstellung im eigenen Namen ist eingebaut, kein Wiederverkäufer
- Zahlungslink ohne Website-Integration möglich — wichtig, solange die
  Landingpage noch nicht in sometra.de steckt

Mollie ist die brauchbare Alternative, falls Stripe für eine zypriotische
Gesellschaft Probleme macht. Beide ohne Monatsgebühr.

### Der Haken, den Mariana kennen muss

**Die Käufer haben überwiegend keine Firmenkreditkarte** — Marianas eigene
Einschätzung. Damit bleiben in der Praxis:

| Methode | Geht das im Firmenkontext? |
|---|---|
| **SEPA-Lastschrift** | Ja, ein Unternehmen kann ein Mandat erteilen. Günstigster Weg |
| **PayPal** | Viele Firmen haben ein Konto. Teuer, aber es geht sofort |
| **Karte** | Laut Marianas Einschätzung selten vorhanden |
| Sofortüberweisung / Onlinebanking | In Firmen oft nicht, weil Freigaben zu zweit laufen |

**Rückbuchungsrisiko bei SEPA-Lastschrift:** Bei der normalen
Basis-Lastschrift kann acht Wochen lang ohne Angabe von Gründen
zurückgebucht werden. Der Workshop liegt bei einer Buchung heute rund sechs
Wochen entfernt — jemand könnte also teilnehmen und danach zurückbuchen.
Zwei Wege dagegen: das **B2B-Firmenlastschriftmandat** (keine Rückgabe, aber
die Bank des Kunden muss es bestätigen), oder für späte Buchungen nur Karte
und PayPal anbieten. **Ungeprüft, ob Stripe das B2B-Mandat anbietet.**

Marianas Haltung dazu ist notiert: Wer nicht zahlen kann, klärt das mit
seiner Buchhaltung. Das ist eine Entscheidung, keine Lücke.

---

## Der Weg ohne Anbieter — überholt, aber dokumentiert

Stand 27.08.: Mariana hat online noch nie etwas verkauft. Digistore war
einmal im Einsatz und war zu teuer — was sich mit der Rechnung oben deckt:
bei 2.356 € sind das 120–165 € je Platz, über 36 Plätze 4.300–6.000 €.

**Daraus folgt nicht, dass ein Zahlungsanbieter her muss. Daraus folgt,
dass für diese Runde keiner gebraucht wird.**

Der Grund: Sometra verkauft längst. Retainer und Kundenprojekte werden
in Rechnung gestellt und überwiesen. Ein Workshopplatz ist dasselbe
Geschäft, nur öfter — 36 Rechnungen statt drei. Es gibt hier nichts neu zu
lernen, und „online verkaufen" ist bei diesem Käufer ohnehin das falsche
Bild: Ein Geschäftsführer, der 2.356 € freigibt, klickt nicht auf Kaufen.
Er leitet eine Rechnung an die Buchhaltung weiter.

### Der ganze Ablauf, ohne ein einziges neues Werkzeug

| Schritt | Womit |
|---|---|
| 1. Anfrage | Der Knopf auf der Landingpage öffnet eine Mail. Reicht für 36 Plätze |
| 2. Erfassen | Ein Formular oder eine Tabelle in Google, oder eine Airtable-Tabelle. Beides ist verbunden und geprüft |
| 3. Rechnung | Aus dem Werkzeug, mit dem heute schon Kunden abgerechnet werden |
| 4. Zahlung | Überweisung. Der Platz ist reserviert, verbindlich wird er mit dem Eingang |
| 5. Nachfassen | Ein Blick in die Tabelle, einmal die Woche |

Kosten: **0 €.** Aufwand: bei 36 Buchungen über zehn Wochen überschaubar.

### Was dabei fehlt — und ob es fehlt

- **Kartenzahlung.** Ihre Käufer wollen sie nicht. Sie wollen eine Rechnung
  mit ausgewiesener Umsatzsteuer
- **Sofortiger Zahlungseingang.** Stattdessen: Reservierung, die mit dem
  Geldeingang verbindlich wird. Steht so in der Bestätigungsmail
- **Automatik.** Bei 36 Buchungen ist Handarbeit billiger als jede Gebühr

### Wann ein Anbieter doch sinnvoll wird

Sobald etwas Günstigeres an Einzelpersonen verkauft wird — die
Aufzeichnung, ein kleines Produkt aus der Live-Session, die Community aus
Bonus 2. Da lohnt sich Automatik, weil viele kleine Beträge anfallen.
Nicht bei zwölf Firmenrechnungen je Stadt.

---

## Empfehlung, wenn es doch zweigleisig sein soll

**Standardweg — Rechnung.**
Bei Buchung geht eine Rechnung raus, zahlbar sofort, spätestens sieben Tage
vor dem Termin. Der Platz ist reserviert, verbindlich wird er mit dem
Zahlungseingang. Steht so auch in der Bestätigungsmail.

**Bequemweg — Zahlungslink auf der Rechnung.**
Für die, die sofort per Karte oder PayPal zahlen wollen. Über Stripe oder
Mollie. Kostet nur bei den Buchungen, die ihn nutzen.

**Die Rechnung selbst** aus einem deutschen Buchhaltungstool (sevdesk,
lexoffice oder vergleichbar). Grund: DATEV-Export für den Steuerberater,
und beide können ZUGFeRD — das wird ohnehin gebraucht, siehe unten.

Damit: keine Gebühren auf dem Standardweg, keine fremde Firma auf der
Rechnung, und die Vorgabe „Zahlung bei Buchung" bleibt bestehen.

---

## Umsatzsteuer: Reverse-Charge — entschieden am 27.08.

Sometra ist zypriotisch. Mariana hat entschieden: **Reverse-Charge, keine
Umsatzsteuer auf der Rechnung.** Der Workshop wird damit als sonstige
Leistung nach der B2B-Grundregel behandelt (Art. 44 MwStSystRL), nicht als
Eintrittsberechtigung zu einer Veranstaltung.

Ich hatte die Gegenmöglichkeit einmal benannt — Art. 53 MwStSystRL, bei dem
ein offenes Seminar am Veranstaltungsort besteuert würde und eine deutsche
Registrierung nötig wäre. Die Entscheidung ist gefallen, hier steht sie als
Grundlage. **Keine Steuerberatung.**

### Was daraus folgt — und was jetzt zu tun ist

**Die gute Nachricht:** Keine umsatzsteuerliche Registrierung in
Deutschland. Das hätte Wochen gedauert, und die Termine liegen in neun.

**Drei Dinge, die dranhängen:**

| Was | Warum |
|---|---|
| **USt-IdNr. des Kunden ist Pflichtfeld bei der Buchung** | Reverse-Charge greift nur gegenüber einem Unternehmer mit gültiger Umsatzsteuer-Identifikationsnummer. Ohne gültige Nummer trägt Sometra die Steuer selbst |
| **Nummer vor der Rechnung prüfen** | Über das MIAS-/VIES-Verfahren der EU. Eine ungültige oder erloschene Nummer fällt sonst erst bei der Prüfung auf, und dann zahlt Sometra |
| **Pflichthinweis auf der Rechnung** | „Steuerschuldnerschaft des Leistungsempfängers" bzw. „Reverse charge". Fehlt der Hinweis, ist die Rechnung unvollständig |

Dazu die **Zusammenfassende Meldung** in Zypern für die
innergemeinschaftlichen Dienstleistungen. Rhythmus und Form klärt der
zypriotische Steuerberater.

### Was das für die Landingpage bedeutet

Dort steht heute: **„2.356 € netto, zzgl. USt."** und **„je Person · netto,
zzgl. USt."**

Das stimmt bei Reverse-Charge nicht mehr — der deutsche Firmenkunde zahlt
2.356 € an Sometra und führt die Steuer selbst ab. Richtig wäre:

> **2.356 €** · zzgl. USt. im Reverse-Charge-Verfahren
> Steuerschuldnerschaft des Leistungsempfängers. Angebot nur für Unternehmen
> mit gültiger USt-IdNr.

**Nicht geändert — die Landingpage wird nur auf Ansage angefasst.**

Nebenwirkung, die zur Sache passt: Der Satz „Angebot nur für Unternehmen mit
gültiger USt-IdNr." erledigt gleichzeitig § 1 Absatz 2 der AGB, der
Verbraucher ausschließt. Ohne diesen Ausschluss gäbe es ein
14-tägiges Widerrufsrecht, und die 48-Stunden-Regel wäre wertlos.

---

## E-Rechnung — was jetzt schon gilt

| Wann | Was |
|---|---|
| **seit 01.01.2025** | Jedes deutsche Unternehmen muss E-Rechnungen **empfangen** können. Gilt für Sometra bereits |
| **ab 01.01.2027** | **Ausstellen** Pflicht bei Vorjahresumsatz über 800.000 € |
| **ab 01.01.2028** | Ausstellen Pflicht für alle |

Zulässig sind nur strukturierte Formate nach EN 16931, also XRechnung oder
ZUGFeRD. **Eine PDF-Rechnung reicht dafür nicht.**

**Für Sometra vermutlich gegenstandslos.** Die deutsche E-Rechnungspflicht
knüpft an die Ansässigkeit im Inland an. Eine zypriotische Gesellschaft ohne
deutsche Betriebsstätte fällt nicht darunter. Mit der Reverse-Charge-
Entscheidung entfällt auch die deutsche Registrierung, die daran etwas
hätte ändern können. Die Fristen unten stehen nur noch der Vollständigkeit
halber da.

**Für Sometra konkret** (Stand 27.08.: Jahresumsatz unter 60.000 €):

- **Ausstellen erst ab 01.01.2028.** Die 800.000-€-Grenze ist weit weg,
  die Stufe 2027 betrifft Sie nicht. Für diesen Workshop reicht die
  Rechnung, die Sie heute schon schreiben
- **Empfangen gilt trotzdem seit 2025** — unabhängig vom Umsatz. Wenn ein
  Lieferant Ihnen eine XRechnung schickt, müssen Sie sie lesen und
  aufbewahren können
- Bei der nächsten Werkzeugwahl auf ZUGFeRD achten, aber nichts deswegen
  jetzt wechseln

**Websuche.**

---

## Was der Workshop mit dem Umsatz macht

Bei vollen Terminen: **36 × 2.356 € = 84.816 €** in sechs Wochen. Auf einen
Jahresumsatz unter 60.000 € gerechnet ist das mehr als eine Verdopplung.

Drei Folgen, die vor dem ersten Verkauf mit dem Steuerberater zu klären sind:

- **Umsatzsteuer-Voranmeldung.** Der Rhythmus hängt an der Zahllast des
  Vorjahres. Bei diesem Sprung kann er sich für 2027 ändern
- **Einkommensteuer-Vorauszahlungen.** Die laufen auf der alten Zahl.
  Was 2026 nicht vorausgezahlt wird, kommt 2027 in einer Summe
- **Kleinunternehmerregelung**, falls sie in Anspruch genommen wird: Seit
  2025 endet der Status sofort mit dem Umsatz, der die 100.000-€-Grenze
  reißt — nicht erst im Folgejahr. Bei 60.000 € plus 84.816 € wäre das
  mitten in der Workshop-Reihe. **Ungeprüft, ob das überhaupt zutrifft** —
  die Landingpage weist Nettopreise zzgl. USt. aus, was auf Regelbesteuerung
  hindeutet

Das ist keine Steuerberatung. Es ist die Liste, mit der Sie ins Gespräch
gehen.

---

## Offen — von Mariana zu klären

| Punkt | Warum |
|---|---|
| **Welches Buchhaltungstool läuft heute?** | Unbekannt. Es muss eines geben, weil Kundenrechnungen laufen. Damit ist die Entscheidung für die erste Runde erledigt |
| **AGB und Stornoregel** | Bei B2B gibt es kein Widerrufsrecht — das gilt nur für Verbraucher. Dafür braucht es eine eigene Regel, was bei Absage passiert. Fehlt bisher komplett |
| **Stornoregel** | Bis wann kostenfrei, danach welcher Anteil? Bei Präsenz mit Catering nötig |
| **Anzahlung oder voller Betrag?** | Bei 2.356 € ist eine Anzahlung ein Kompromiss, wenn jemand nicht sofort voll zahlen will |
| **Steuerberater bestätigen lassen** | Umsatzsteuer und Rechnungspflichtangaben, vor der ersten Rechnung |

---

## Quellen

- [E-Rechnungspflicht 2027 — Grant Thornton](https://www.grantthornton.de/themen/2026/e-rechnungspflicht-2027-die-wichtigsten-fragen-und-antworten-zur-e-rechnung/)
- [E-Rechnungspflicht ab 2025 — IHK Frankfurt](https://www.frankfurt-main.ihk.de/recht/uebersicht-alle-rechtsthemen/steuerrecht/umsatzsteuer-national/e-rechnungspflicht-ab-2025-6055774)
- [E-Rechnung B2B: Fristen 2027/2028 — rickert.law](https://rickert.law/e-rechnung-b2b-2027/)
- [Umsatzsteuer bei Online-Veranstaltungen — ICON](https://www.icon.at/news/detail/umsatzsteuer-online-veranstaltungen-in-oesterreich-und-deutschland)
- [Umsatzsteuer bei Online-Seminaren — orgamax](https://blog.orgamax.de/unternehmer-news/umsatzsteuer-bei-online-seminaren-und-anderen-online-events)
