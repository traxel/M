# Content-Agent — Aufbau

Datum: 2026-08-27. Status: Vorschlag, noch nicht gebaut.
Agent 5 im Workshop-Stack.

---

## Nicht vier Agenten

Vier Plattform-Agenten (LinkedIn, YouTube, Instagram, TikTok) heißt: vier Kopien
derselben Stimme, derselben Themenlogik, derselben Bewertung. Die driften
auseinander. Nach drei Monaten klingt TikTok anders als LinkedIn, und niemand
weiß mehr warum.

**Ein Kern, zwei Ausgabezweige.**

```
        Kern-Agent
   Themen finden · bewerten · Kernaussage · Stimme
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   Zweig Text               Zweig Video
   → LinkedIn               → YouTube (lang)
                            → Shorts / Reels / TikTok
```

Der Kern ist die Arbeit. Die Zweige sind Formatregeln.

---

## Kern-Agent

- Themen finden: was sich in den Plattformen bewegt, was die Zielgruppe fragt
- Bewerten: Relevanz für GF, Vertriebsleiter, Marketingleiter — nicht nach Aktualität
- Kernaussage festlegen: ein Satz, der ohne Format funktioniert
- Stimme anwenden: Ton-Regeln, Verbote, Perspektive

Grundlage vorhanden: `mariana-voice`, `mariana-dreamoutcome`, `humanizer-de`,
`content-learning-loop`.

## Zweig Text — LinkedIn

- Hook, Aufbau, Länge, Leser siezen, CTA
- Grundlage vorhanden aus den bisherigen Kunden-Skills, muss auf Sometra umgebaut werden

## Zweig Video — YouTube, Shorts, Reels, TikTok

Weitgehend vorhanden: `video-ideas`, `video-script`, `visual-regie`,
`mariana-thumbnail`.

Fehlt: die Kurzform-Ableitung. Aus einem Long-Video mehrere Shorts schneiden und
je Plattform anders aufziehen — TikTok braucht einen anderen Einstieg als ein
YouTube-Short, Reels einen anderen als beide.

---

## Reihenfolge

Erst das Produkt fertig, dann der Content-Agent, dann radialer Content.

Der Grund: radialer Content braucht einen Kern. Ohne fertiges Produkt ist der
Kern eine Meinung. Mit fertigem Produkt ist er ein Angebot.

---

## Radialer Content — was der Kern ist

| Kern | Ableitung |
|---|---|
| Der Workshop | Live-Session, Landingpage |
| Jeder der 5 Agenten | ein Long-Video, daraus 3–4 Shorts je Plattform |
| Der Pilot | Ergebnisse in Zahlen, Referenzen |
| Die Konstruktionsregel "kein Agent klickt auf Senden" | Haltungs-Content |

Fünf Agenten × je ein Long-Video = fünf Kerne. Daraus 15–20 Kurzformate.
Das ist der Content-Vorrat für ein Quartal, aus Material, das ohnehin entsteht.

---

## Zu entscheiden

1. Vier Plattformen gleichzeitig oder gestaffelt? Empfehlung: LinkedIn und
   YouTube zuerst — dort sitzt der ICP. Instagram und TikTok danach, aus
   demselben Material.
2. Wer ist das Publikum auf TikTok? Der ICP ist dort nicht. Entweder zweite
   Zielgruppe bewusst aufmachen oder TikTok als Reichweitenkanal ohne
   Verkaufserwartung führen.
