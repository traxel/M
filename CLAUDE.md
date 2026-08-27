# Kontext & Gedächtnis

Persistente Notizen für die Zusammenarbeit mit Mariana (Sometra).

## Kunden

- **GKK PARTNERS ist kein Kunde mehr** (Stand: 2026-08-17). Keine GKK-Content-Skills
  (`gkk-content-create`, `gkk-content-research`, `gkk-personal-linkedin-posts`,
  `gkk-status-sync`) mehr proaktiv verwenden, außer Mariana bittet ausdrücklich darum.

## Positionierung

- **Sometra verkauft Schulung + Umsetzungsbegleitung — keine Plattform, kein
  eigenes Produkt, kein Agenten-Abo** (Stand: 2026-08-26). Die LinkedIn-Agenten
  sind Eigengebrauch, Lehrinhalt und Retainer-Arbeit beim Kunden — nicht
  Verkaufsgegenstand. Begründung und Angebotsleiter:
  `entscheidungen/2026-08-26_schulung-statt-plattform.md`, Funnel und Preise:
  `funnel/funnel.md`.

## Zusammenarbeit

- **Kurz antworten, in Bullets** (Stand: 2026-08-27). Keine langen Fließtexte,
  keine Wiederholung dessen, was schon in den Dokumenten steht. Ergebnis,
  Zahlen, offene Entscheidung — mehr nicht. Ausführliches gehört ins Dokument,
  nicht in die Antwort. **Gilt ausnahmslos, auch bei großen Lieferungen.**
- **Landingpage nur auf Ansage ändern** (Stand: 2026-08-27). Die Seite liegt in
  `landingpage/index.html` und ist als Artifact veröffentlicht. Mariana nennt die
  Änderung, ich setze um und veröffentliche neu. Keine eigenmächtigen
  Verbesserungen, keine ungefragten Textvorschläge.

## Arbeitsweise

- **Kein Vorschlag ohne vorherige Prüfung** (Stand: 2026-08-27). Bevor etwas
  vorgeschlagen wird, ist zu belegen, dass es technisch geht — bevorzugt durch
  den Aufruf des Werkzeugs selbst, sonst durch die Doku des Anbieters. Ist
  eine Prüfung nicht möglich, wird die Annahme ausdrücklich als ungeprüft
  benannt. Stand der Prüfungen und offene Annahmen: `verifiziert.md`.
- Prüfreihenfolge: (1) Dienst aufrufen, (2) Werkzeug-Schema des verbundenen
  Connectors lesen, (3) Umgebung prüfen (`ListConnectors`, `ListSkills`,
  Dateisystem, curl), (4) Websuche. Nur wenn 1–3 nichts hergeben, zählt 4 —
  und dann wird dazugesagt, dass es nur Websuche war.
- **Drei Fragen, bevor etwas ausgeschlossen wird:** Ist es vorhanden? Läuft es
  von hier? **Lässt es sich hier nachinstallieren?** Die dritte wird am
  leichtesten vergessen — HyperFrames war so ein Fall.
- **HyperFrames/HeyGen läuft in Remote-Sessions** nach
  `npx skills add heygen-com/hyperframes` und `apt-get install -y ffmpeg`
  (ffprobe wird gebraucht, Playwright-ffmpeg reicht nicht). End-to-end
  geprüft am 2026-08-27. Beides ist pro Container neu nötig.
- **Kosten bei HyperFrames/HeyGen:** Erstellen und **lokal** rendern kosten kein
  Geld (kein HeyGen-Konto nötig, geprüft). Geld kostet nur `cloud render`
  (pro Credit) sowie `lambda`/`cloudrun` über AWS bzw. GCP. Für `publish`
  ist es ungeklärt. Token und Geld laufen gegenläufig: Schreiben kostet
  Token, lokal rendern kostet nichts, Cloud kostet Geld statt Token.
  Also: **so oft lokal iterieren wie nötig.**
- **Drei Werkzeug-Ebenen unterscheiden:** claude.ai-Connectoren (erreichen
  Remote-Sessions), Desktop-Erweiterungen `.mcpb`/`.dxt` (nur Mac,
  Desktop-App — dort liegen Apify, Control Chrome, Filesystem), lokale
  Skills/CLI (teils per `npx` nachinstallierbar).
- **Connectoren haben zwei Schalter:** `connected` (Konto-Ebene) und
  `enabledInChat` (dieser Chat). Beides muss an sein, sonst fehlen die
  Werkzeuge trotz erfolgreicher Verbindung. Mit `ListConnectors` prüfen,
  bevor „ist nicht verbunden" behauptet wird.
- **Connectoren laufen nicht über den Container-Egress.** Airtable ist per
  Connector nutzbar, obwohl `airtable.com` per curl nicht erreichbar ist.
  „curl kommt nicht durch" heißt also nicht „Connector geht nicht".
- **Zwei Umgebungen unterscheiden.** Remote-Cloud-Sessions haben nur eine
  gesyncte Teilmenge der Skills. HyperFrames-Engine und Thumbnail-Render
  laufen lokal auf dem Mac. „Geht nicht" heißt oft „geht nicht von hier" —
  das ist zu unterscheiden, bevor etwas ausgeschlossen wird.
