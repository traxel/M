# Tagesplan — "So bauen Sie sich Ihre Vertriebsagenten"

Präsenz. Ein Tag, 09:00–17:00. Hamburg · Köln · München, November 2026.
Stand: 2026-08-27. Status: Vorschlag zur Freigabe.

---

## Das Versprechen — und warum es kleiner ist als der Tag

Nach außen versprochen ist **ein** Agent: „Um 17:00 Uhr läuft Ihr erster
selbst programmierter Vertriebsagent."

Gebaut werden am Tag **fünf**. Der Unterschied ist Absicht.

Fünf Agenten für zwölf Leute in 235 Minuten sind erreichbar, aber nicht
garantierbar — es hängt daran, wie sauber die Kriterien sitzen und ob das
Netzwerk mitspielt. Ein Agent, geprüft am Platz, ist garantierbar. Und die
Garantie hängt genau an dem, was am Platz nachgeprüft wird.

**Folge für den Tag:** Der Kontrollpunkt aus Block 2 ist der Garantiepunkt.
Er sitzt vor der Mittagspause, nicht um 16:45. Wenn dort bei jemandem nichts
läuft, sind noch vier Stunden Zeit — und nicht fünfzehn Minuten.

**Folge für die Gruppengröße:** Zwölf ist die Zahl, bei der Mariana an einem
Tag an jeden Platz kommt. Ab dreizehn ist die Garantie eine Behauptung.
Deshalb steht die Zahl in jedem Text nach außen, mit genau dieser Begründung.

**Folge für die Sprache:** „Selbst programmiert" und „Sie müssen nicht
programmieren" dürfen nicht nebeneinanderstehen. Gesagt wird: eine
Programmiersprache braucht niemand, aber Auftrag, Prüflogik und
Abbruchregeln schreibt jeder selbst — und das läuft weiter, wenn der Rechner
zugeklappt ist.

---

## Die Zeitrechnung

| | Minuten |
|---|---|
| 09:00–17:00 | 480 |
| Frühstückspause | −30 |
| Mittagspause | −60 |
| Kaffeepause | −45 |
| **Lernzeit** | **345** |

Alles unten addiert sich auf genau diese 345 Minuten. Kein Block ist
gestreckt, um die Rechnung aufgehen zu lassen.

---

## Der Tag

Max. 12 Teilnehmer. Die Zahl ist nicht kosmetisch — sie ist die Bedingung
dafür, dass der Kontrollpunkt an jedem Platz stattfindet.

| Zeit | Dauer | Was |
|---|---|---|
| 08:45 | | Ankommen, Technik anstecken |
| **09:00** | **90** | **Block 1 — Grundlagen** |
| 10:30 | 30 | Frühstückspause |
| **11:00** | **105** | **Block 2 — Agent 1: Such- und Finde-Agent** |
| 12:45 | 60 | Mittagspause |
| **13:45** | **90** | **Block 3 — Agent 2 + Agent 3** |
| 15:15 | 45 | Kaffeepause |
| **16:00** | **60** | **Block 4 — Agent 4 + Agent 5 + Zusammenschalten** |
| 17:00 | | Ende |

**Warum der Bau schon um 11:00 anfängt und nicht erst nach dem Mittag:**
Fünf Agenten in den 150 Minuten nach der Mittagspause sind 30 Minuten pro
Agent. Das hält bei zwölf Leuten in einem fremden Raum nicht. So bekommen
die Agenten 235 Minuten statt 150 — und Skills, Connectoren und MCPs werden
nicht zweimal behandelt, sondern einmal am lebenden Objekt.

---

## Block 1 — Grundlagen · 90 Minuten

Überblick, kein Tiefgang. Der Tiefgang kommt in Block 2 am eigenen Agenten.

| Minuten | Thema | Worauf es hinausläuft |
|---|---|---|
| 15 | Was Code ist — und was ein Agent ist | Ein Agent ist kein Chatbot. Er hat einen Auftrag, Werkzeuge und eine Abbruchbedingung |
| 15 | Anthropic und OpenAI: Claude Code und Codex | Was welches ist, wofür man welches nimmt, was beide nicht können |
| 10 | Cowork und Work — wo Sie arbeiten | Der Unterschied zwischen "ich frage etwas" und "es arbeitet für mich" |
| 10 | Artefakte | Was am Ende in der Hand bleibt |
| 15 | Skills | Eine Skill ist eine Arbeitsanweisung, die wiederverwendbar ist. Ab hier bauen Sie |
| 25 | Connectoren, MCPs, APIs — die drei Ebenen | Womit ein Agent an Ihre Daten kommt. Die Ebene, an der es in der Praxis scheitert |

**Der Satz, der den Tag trägt, fällt in Block 1:**

> Kein Agent klickt auf Senden.

Jeder Agent recherchiert, bewertet, bereitet vor und legt vor. Der Mensch
prüft und löst aus. Zwei Gründe, beide werden genannt: Netzwerke beschränken
Konten, die automatisiert bedient werden. Und eine Nachricht, die ungeprüft
rausgeht, ist irgendwann die falsche Nachricht an den falschen Kunden.

---

## Block 2 — Agent 1: Such- und Finde-Agent · 105 Minuten

Der teuerste Block des Tages, und der einzige, der so lang sein muss.
Hier wird nicht nur ein Agent gebaut, hier wird das Muster gebaut, das die
anderen vier wiederverwenden.

| Minuten | Schritt |
|---|---|
| 10 | **Vorführung.** Mariana zeigt ihren laufenden Agenten: ein Durchgang von der Suche bis zum Datensatz. Gezeigt wird zuerst ein Fund, der **durchfällt** |
| 10 | **Zielbild.** Ein Satz auf Papier: Ich suche [Rolle] in [Region] in [Branche], weil [Grund] |
| 10 | **Rollen-Liste.** Fünf bis acht Titel, so geschrieben wie sie im Profil stehen. Harte Obergrenze acht |
| 15 | **Die fünf Pflichtkriterien** auf das eigene Geschäft übertragen |
| 20 | **Steuerung anlegen** — Airtable oder Excel. Beide Wege werden gezeigt, jeder nimmt einen |
| 25 | **Agent zusammensetzen.** Vorlage mit Platzhaltern: Rollen, Filter, Kriterien, Ablage, Tagesziel, Abbruchbedingungen |
| 10 | **Erster Lauf** und Kontrollpunkt |
| 5 | Puffer |

**Airtable oder Excel — der Unterschied, offen gesagt**

| | Airtable | Excel |
|---|---|---|
| Anbindung | über Connector, der Agent schreibt direkt hinein | über Datei, der Agent schreibt eine Tabelle, die Sie ablegen |
| Aufwand am Tag | Konto anlegen, 10 Minuten | keiner, ist da |
| Später | Agent 2 bis 5 setzen direkt darauf auf | funktioniert, ein Zwischenschritt mehr |

Wer heute nichts entscheiden will, nimmt Excel. Umsteigen geht später,
umgekehrt auch.

**Kontrollpunkt Block 2 — das ist der Garantiepunkt des Tages.**
Von außen prüfbar, zweiteilig:
- **a)** mindestens drei Datensätze in der eigenen Ablage, alle Pflichtfelder
  befüllt, jeder mit Vermerk, welche Rolle und welche Seite ihn geliefert haben
- **b)** mindestens ein protokollierter Ausschluss mit genanntem Kriterium

(b) ist nicht Beiwerk. Ein Such-Agent, der alles durchwinkt, ist kaputt und
fällt erst in vier Wochen auf.

---

## Block 3 — Agent 2 und Agent 3 · 90 Minuten

### Agent 2 — Prüf-Agent · 30 Minuten

Sortiert aus, bevor jemand angeschrieben wird: Dubletten, unpassende Rollen,
Firmen, die nicht ins Profil passen.

Der unscheinbarste Agent und der, der am meisten Zeit spart. Er ist schnell
gebaut, weil er auf derselben Ablage arbeitet wie Agent 1 — nur lesend und
markierend.

| Minuten | Schritt |
|---|---|
| 5 | Vorführung: was ein ungefilterter Bestand nach vier Wochen anrichtet |
| 15 | Ausschlussregeln definieren und einsetzen |
| 10 | Lauf über den eigenen Bestand aus Block 2 |

**Kontrollpunkt:** Der Agent hat mindestens einen eigenen Datensatz aus
Block 2 markiert und den Grund hingeschrieben.

### Agent 3 — DM-Schreibe-Agent · 60 Minuten

Der Block, den die Teilnehmer im Kopf behalten. Schreibt die erste Nachricht
individuell — aus dem Profil heraus, nicht aus einer Vorlage.

Hier wird der wichtigste Teil des Tages gelernt: **wie man einem Agenten
Tonalität beibringt.** Nicht "schreib freundlich", sondern drei eigene Texte
als Maßstab, an denen der Agent gemessen wird.

| Minuten | Schritt |
|---|---|
| 10 | Vorführung: dieselbe Person, zwei Nachrichten — eine aus der Vorlage, eine aus dem Profil |
| 15 | Drei eigene Nachrichten mitbringen oder schreiben. Das ist der Maßstab |
| 20 | Agent bauen: Anlass finden, Nachricht entwerfen, **zur Freigabe vorlegen** |
| 10 | Lauf über drei eigene Kontakte aus Block 2 |
| 5 | Puffer |

**Kontrollpunkt:** Drei Entwürfe liegen zur Freigabe vor. Jeder nennt einen
Anlass, der aus dem Profil stammt und nicht auf jeden zweiten passt.
Keiner ist verschickt.

---

## Block 4 — Agent 4, Agent 5, Zusammenschalten · 60 Minuten

Beide Agenten sind Varianten dessen, was schon steht. Deshalb reichen 20
Minuten — nicht, weil sie unwichtig wären.

### Agent 4 — Follow-up-Agent · 20 Minuten
Erkennt, wer wartet, und schreibt die Folgenachricht aus dem bisherigen
Verlauf. Kein Pitch, bevor ein Gespräch da ist.
Baut auf Agent 3 auf: gleiche Tonalitätsregeln, anderer Auslöser.

**Kontrollpunkt:** Ein Folgeentwurf liegt vor, der auf den vorherigen Verlauf
Bezug nimmt.

### Agent 5 — Content-Agent · 20 Minuten
Recherchiert Themen, bewertet sie nach Relevanz und gibt sie plattformgerecht
aus. Ein Kern, zwei Ausgabezweige — nicht vier Agenten für vier Plattformen.
Baut auf dem Muster aus Agent 1 auf: suchen, bewerten, ablegen.

**Kontrollpunkt:** Drei bewertete Themen liegen in der eigenen Ablage.

### Zusammenschalten · 20 Minuten
- Die fünf als ein Ablauf: finden → prüfen → ansprechen → nachfassen → sichtbar bleiben
- **Was in den ersten zwei Wochen kaputtgeht** — bevor es kaputtgeht
- Ein konkreter nächster Schritt pro Person, aufgeschrieben, nicht gesagt

Dieser Teil wird nicht gekürzt. Wenn der Tag klemmt, wird Agent 5 gekürzt.

---

## Was schiefgeht — und wie es abgefangen wird

| Was | Wie es abgefangen wird |
|---|---|
| **Zugänge fehlen am Morgen.** Bei zwölf Leuten gleichzeitig kostet das 45 Minuten | Technik-Check per Mail drei Tage vorher, mit Bestätigung zurück. Ohne Bestätigung Anruf |
| **Die Rollen-Liste ist zu breit.** "Geschäftsführer" liefert vom Drei-Mann-Betrieb bis zum Konzern | Obergrenze acht Titel, jeder Titel wird gegen den Satz aus dem Zielbild gehalten |
| **Das Netzwerk unterbricht mitten im Lauf** — Login, Zwei-Faktor, Sicherheitscheck. Bei zwölf Leuten passiert das fast sicher bei einem | Die Abbruchregel steht von Anfang an in der Vorlage. Und der Kontrollpunkt lässt sich an einer festen Prüfliste erbringen, damit niemand am Login hängen bleibt |
| **Jemand will Agent 3 scharf schalten** und automatisch senden lassen | Wird in Block 1 begründet, nicht in Block 3 verteidigt |
| **Das WLAN im Tagungsraum** | Eigener Hotspot als Rückfallebene, vorher getestet. Bei Präsenz die häufigste vermeidbare Störung |

---

## Material — je Teilnehmer

| Was | Für |
|---|---|
| Kriterienblatt, eine Seite zum Ausfüllen | Block 2 |
| Rollen-Listen-Vorlage mit Abgrenzungsbeispielen | Block 2 |
| Agent-Vorlage mit Platzhaltern und festen Abbruchbedingungen | alle Blöcke |
| Ablage-Vorlage — einmal Airtable, einmal Excel | Block 2 |
| Prüfliste "10 Kandidaten" | Rückfallebene und Selbsttest danach |
| Tonalitäts-Blatt: drei eigene Nachrichten als Maßstab | Block 3 |

Bei Mariana: Abhak-Liste für die Kontrollpunkte. Zwölf Zeilen, fünf Spalten.
**Diese Liste ist der Beleg für die Garantie.** Ohne sie steht am Ende des
Tages Aussage gegen Aussage.

---

## Voraussetzungen — gehören auf die Landingpage

- Eigener Laptop. Kein Firmenrechner, auf dem nichts installiert werden darf
- Aktives, bezahltes Konto bei Claude oder ChatGPT, **vor** dem Workshop eingerichtet
- LinkedIn-Konto, eingeloggt
- Airtable-Konto (kostenlos) oder Excel
- Eine Vorstellung davon, welche Kunden Sie suchen

---

## Nach dem Workshop

Innerhalb von zwei Werktagen an alle Teilnehmer: was jeder gebaut hat, die
Anleitungen zum Nachbauen und Erweitern, ein konkreter nächster Schritt pro
Person.

Vier Wochen später eine Nachfrage: Was läuft noch? Was ist eingeschlafen?

Das ist keine Freundlichkeit. Das ist die Stelle, an der die Begleitung
entsteht — und die einzige Möglichkeit, jemals Ergebnisse in Zahlen zu haben.
