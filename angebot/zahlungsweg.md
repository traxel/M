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

## Empfehlung: zweigleisig

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

## Umsatzsteuer — die gute Nachricht

Der Workshop ist eine **Präsenzveranstaltung in Deutschland**. Für die
Eintrittsberechtigung zu einer Veranstaltung ist der Leistungsort der
Veranstaltungsort. Damit gilt für alle drei Städte **19 % deutsche
Umsatzsteuer** — auch dann, wenn ein Teilnehmer aus dem EU-Ausland kommt.
Kein Reverse-Charge, keine Sonderfälle.

Das ist der einfache Fall. Bei einem Online-Seminar an einen EU-Firmenkunden
wäre es umgekehrt gewesen.

**Websuche, keine Steuerberatung.** Vor der ersten Rechnung mit dem
Steuerberater bestätigen.

---

## E-Rechnung — was jetzt schon gilt

| Wann | Was |
|---|---|
| **seit 01.01.2025** | Jedes deutsche Unternehmen muss E-Rechnungen **empfangen** können. Gilt für Sometra bereits |
| **ab 01.01.2027** | **Ausstellen** Pflicht bei Vorjahresumsatz über 800.000 € |
| **ab 01.01.2028** | Ausstellen Pflicht für alle |

Zulässig sind nur strukturierte Formate nach EN 16931, also XRechnung oder
ZUGFeRD. **Eine PDF-Rechnung reicht dafür nicht.**

Für diesen Workshop heißt das: 2026 ist PDF noch in Ordnung. Aber das
Werkzeug, das jetzt ausgewählt wird, sollte ZUGFeRD können — sonst wird in
zwei Jahren ein zweites Mal umgestellt.

**Websuche.**

---

## Offen — von Mariana zu klären

| Punkt | Warum |
|---|---|
| **Welches Buchhaltungstool läuft heute?** | Unbekannt. Wenn schon eines da ist, entfällt die halbe Entscheidung |
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
