#!/usr/bin/env python3
"""
Belegt, warum die Ratio gegen zeitliche Nachbarn gerechnet wird und nicht
gegen einen Median ueber alle Videos.

Aufruf:  python3 agenten/scripts/test_nachbar_median.py
Braucht keinen API-Schluessel — rechnet mit erfundenen Daten.
"""
import importlib.util
import statistics
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "yo", Path(__file__).with_name("yt_outlier.py"))
yo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(yo)

# Ein Kanal, bei dem Views sich streng linear mit dem Alter ansammeln.
# Genau ein Video ist wirklich besser als seine Nachbarn: 5-fach, und jung.
ALTER = list(range(20, 200, 6))
VIEWS = [a * 500 for a in ALTER]
GEPFLANZT = 2
VIEWS[GEPFLANZT] *= 5


def main() -> int:
    med_alle = statistics.median(VIEWS)
    alt = sorted(((VIEWS[i] / med_alle, ALTER[i]) for i in range(len(VIEWS))),
                 reverse=True)
    neu = sorted(((VIEWS[i] / yo.nachbar_median(VIEWS, i, 8), ALTER[i])
                  for i in range(len(VIEWS))), reverse=True)

    print(f"30 Videos, Views = Alter x 500.")
    print(f"Ein echter Ausreisser: {ALTER[GEPFLANZT]} Tage alt, 5-fach.\n")
    for name, daten in (("ALT  Median ueber alle", alt),
                        ("NEU  Median der Nachbarn", neu)):
        print(f"{name} — hoechste Ratios:")
        for r, ag in daten[:3]:
            marke = "  <- der gepflanzte" if ag == ALTER[GEPFLANZT] else ""
            print(f"   {r:4.1f}x  {ag:>3}d{marke}")
        print()

    ok = neu[0][1] == ALTER[GEPFLANZT] and alt[0][1] != ALTER[GEPFLANZT]
    print("Erwartet: NEU findet den gepflanzten Ausreisser, ALT nicht.")
    print("Ergebnis:", "bestanden" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
