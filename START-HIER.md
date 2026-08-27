# Start hier

Stand: 2026-08-27, Abend. Frische Session — dieser Text ist das Gedächtnis.

**Aktueller Arbeitsstand liegt auf dem Branch `claude/schulungen-anbieten-a7pb77`.**
Lokal zuerst: `git fetch origin && git checkout claude/schulungen-anbieten-a7pb77`

---

## Das Produkt steht

**Workshop „So bauen Sie sich Ihre Vertriebsagenten"**
Präsenz, ein Tag, 09:00–17:00, max. 12 Teilnehmer.

| Stadt | Termin |
|---|---|
| Hamburg | Do **29.10.2026** — betahaus HafenCity |
| München | Mo **02.11.2026** — Ort offen |
| Köln | Do **05.11.2026** — Ort offen |

**Preis: 2.356 €** je Person, **Reverse-Charge** (Sometra ist zypriotisch).
USt-IdNr. des Kunden ist Pflichtfeld bei der Buchung.

**Versprochen ist ein Agent, nicht fünf:**
„Um 17:00 Uhr läuft Ihr erster selbst programmierter Agent."
**Garantie: 100 % Geld zurück**, geprüft am Platz vor Ende des Tages.

---

## Wo was liegt

| Datei | Inhalt |
|---|---|
| `landingpage/index.html` | Die Seite. **Nur auf Ansage ändern.** Als Artifact veröffentlicht |
| `schulung/tagesplan-f2f.md` | Tagesablauf 01–05, alle Blockzeiten nachgerechnet |
| `angebot/agb-und-storno.md` | AGB-Entwurf, 11 Paragrafen. Zur anwaltlichen Prüfung |
| `angebot/zahlungsweg.md` | Stripe, Gebührenvergleich, Reverse-Charge, E-Rechnung |
| `content/content-plan-november.md` | Fünf fertige LinkedIn-Beiträge, warten auf Freigabe |
| `entscheidungen/2026-08-27_f2f-drei-staedte.md` | Warum Präsenz, die Rechnung dahinter |
| `verifiziert.md` | Was geprüft ist. **Vor jedem Vorschlag lesen** |
| `funnel/` | Überholt, als Herleitung markiert. Nicht als Rahmen verwenden |
| `schulung/modul-1-recherche-agent.md` | Historisch, erste Fassung mit fünf Agenten |

---

## Das Dringendste

**Die Ankündigung muss Anfang September raus.** 63 Tage bis Hamburg, 36
Plätze zu füllen. Sechs Wochen Vorlauf sind bei diesem Preis die Untergrenze.
Der Content dafür liegt fertig da und wartet nur auf Freigabe.

| Wer | Was | Bis wann |
|---|---|---|
| Mari | Content-Plan freigeben | sofort |
| Mari | Stripe einrichten | Wochenende |
| Mari | DM-Versand starten | Wochenende |
| Mari | Räume München und Köln | 2 Wochen |
| Mari | AGB zum Anwalt — **Rechtswahl fehlt noch** | vor der ersten Buchung |
| Ich | Promo-Video: Skript und Sprechtext für MAIK | offen |
| Ich | Hamburg-Agent, angelehnt an den Versand-Agenten | offen |
| Ich | Oxygen-Fassung der Landingpage | auf Ansage |

---

## Offene Entscheidungen

1. **Rechtswahl in § 11 der AGB** — deutsches oder zypriotisches Recht?
   Der Entwurf ist auf deutschem Recht gebaut. Blockiert die Prüfung
2. **Gerichtsstand Zypern** ist eingetragen. Stadt fehlt noch
3. **Bonus-Werte** bestätigen (Summe steht auf 3.700 €)
4. **Räume** München und Köln

---

## Was geklärt ist — nicht neu aufmachen

| | |
|---|---|
| Zahlungsanbieter | **Stripe.** SEPA-Lastschrift 0,35 € pauschal statt 116 € bei Digistore |
| Umsatzsteuer | **Reverse-Charge.** Keine deutsche Registrierung nötig |
| Storno | **48 Stunden** ab Rechnung. Danach verbindlich. Ersatzteilnehmer kostenfrei |
| Absage durch Sometra | unter **sechs Anmeldungen**. Grund muss nicht genannt werden |
| Garantie | **100 % Geld**, kein Gutschein. Bewusst so entschieden |
| Landingpage-System | Hosteurope, WordPress, **Oxygen**. Impressum steht bereits |
| Gruppengröße | 12, mit Begründung: darüber kommt Mari nicht an jeden Platz |

---

## Zwei Umgebungen — das ist der Grund für viele „geht nicht"

**Marianas Mac hat den vollen Werkzeugkasten. Cloud-Sessions haben eine
Teilmenge.** Wer sagt „geht nicht", muss sagen, welche der beiden gemeint ist.

| Nur lokal auf dem Mac | Läuft auch in der Cloud |
|---|---|
| HeyGen-Avatar (MAIK) | Airtable, Drive, Descript, Gmail, Calendar, HubSpot, M365, Zoom, Canva |
| Kling und alle Fal-Modelle (`FAL_KEY`) | HyperFrames **nach Nachinstallation** |
| Thumbnail-Render | YouTube Data API, sobald ein Key da ist |
| Schlüsselbund | |
| Desktop-Erweiterungen: Apify, Control Chrome, Filesystem | |
| sometra.de aufrufen (aus der Cloud blockiert, 403) | |

**In der Cloud jedes Mal neu nötig**, der Container ist flüchtig:
```
npx skills add heygen-com/hyperframes
apt-get install -y ffmpeg
```

**Für Videoarbeit heißt das:** lokale Session starten. Für Dokumente,
Landingpage, Content und Agentenlogik ist die Cloud gleichwertig.

---

## Arbeitsregeln

- **Kurz antworten, in Bullets.** Ausnahmslos. Ausführliches ins Dokument
- **Landingpage nur auf Ansage ändern.** Keine eigenmächtigen Verbesserungen
- **Kein Vorschlag ohne Prüfung.** Reihenfolge: Dienst aufrufen →
  Werkzeug-Schema lesen → Umgebung prüfen → erst dann Websuche, und das dazusagen
- **Vor dem Ausschließen drei Fragen:** Ist es vorhanden? Läuft es von hier?
  Lässt es sich nachinstallieren?
