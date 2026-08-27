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
