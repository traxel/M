#!/usr/bin/env python3
"""
Outlier-Ratio fuer YouTube-Kanaele.

Ratio = Views des Videos / Median der letzten N Videos desselben Kanals.
Nur die Ratio ist ueber Kanalgroessen hinweg vergleichbar — eine absolute
View-Schwelle ist es nicht.

Aufruf:
    YT_API_KEY=... python3 yt_outlier.py UCxxxx            # Kanal-ID
    YT_API_KEY=... python3 yt_outlier.py @handle           # Handle
    YT_API_KEY=... python3 yt_outlier.py @a @b --min 2.0

Der Schluessel kommt aus YT_API_KEY oder aus ~/.yt_api_key.
Er wird nie ausgegeben und nie protokolliert.

Kontingent je Kanal: 2-3 Einheiten bei Kanal-ID, +100 wenn ein Handle
ueber die Suche aufgeloest werden muss. Tagesbudget: 10.000.
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://www.googleapis.com/youtube/v3/"
QUOTA = {"used": 0}


def key() -> str:
    k = os.environ.get("YT_API_KEY")
    if not k:
        p = os.path.expanduser("~/.yt_api_key")
        if os.path.exists(p):
            k = open(p).read().strip()
    if not k:
        sys.exit("YT_API_KEY nicht gesetzt und ~/.yt_api_key nicht vorhanden.")
    return k


def call(endpoint: str, cost: int, **params) -> dict:
    params["key"] = key()
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            QUOTA["used"] += cost
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        # Schluessel steht in der URL, deshalb nur den Fehlertext zeigen
        try:
            msg = json.loads(body)["error"]["message"]
        except Exception:
            msg = body[:300]
        sys.exit(f"API-Fehler {e.code} bei {endpoint}: {msg}")


def resolve(channel: str) -> tuple[str, str, int, str]:
    """Gibt (channel_id, uploads_playlist_id, abonnenten, titel) zurueck."""
    if channel.startswith("UC") and len(channel) == 24:
        d = call("channels", 1, part="contentDetails,statistics,snippet", id=channel)
    else:
        handle = channel if channel.startswith("@") else "@" + channel
        d = call("channels", 1, part="contentDetails,statistics,snippet", forHandle=handle)
        if not d.get("items"):
            # Rueckfall: Suche kostet 100 Einheiten
            s = call("search", 100, part="snippet", q=handle.lstrip("@"),
                     type="channel", maxResults=1)
            if not s.get("items"):
                sys.exit(f"Kanal nicht gefunden: {channel}")
            cid = s["items"][0]["snippet"]["channelId"]
            d = call("channels", 1, part="contentDetails,statistics,snippet", id=cid)
    if not d.get("items"):
        sys.exit(f"Kanal nicht gefunden: {channel}")
    it = d["items"][0]
    return (it["id"],
            it["contentDetails"]["relatedPlaylists"]["uploads"],
            int(it["statistics"].get("subscriberCount", 0)),
            it["snippet"]["title"])


def videos(uploads: str, want: int) -> list[dict]:
    ids, token = [], None
    while len(ids) < want:
        p = dict(part="contentDetails", playlistId=uploads, maxResults=50)
        if token:
            p["pageToken"] = token
        d = call("playlistItems", 1, **p)
        ids += [i["contentDetails"]["videoId"] for i in d.get("items", [])]
        token = d.get("nextPageToken")
        if not token:
            break
    out = []
    for i in range(0, len(ids[:want]), 50):
        d = call("videos", 1, part="snippet,statistics,contentDetails",
                 id=",".join(ids[i:i + 50]))
        out += d.get("items", [])
    return out


def de(n: float) -> str:
    """Tausenderpunkte, deutsche Schreibweise."""
    return f"{int(n):,}".replace(",", ".")


def iso_seconds(dur: str) -> int:
    import re
    m = re.match(r"P(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", dur or "")
    if not m:
        return 0
    d, h, mi, s = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("channels", nargs="+")
    ap.add_argument("--sample", type=int, default=30, help="Videos fuer den Median")
    ap.add_argument("--min", type=float, default=2.0, help="Ratio ab der ausgegeben wird")
    ap.add_argument("--min-age", type=int, default=14, help="Tage, bevor ein Video zaehlt")
    ap.add_argument("--max-age", type=int, default=365)
    ap.add_argument("--shorts", action="store_true", help="Shorts mitzaehlen")
    a = ap.parse_args()

    now = datetime.now(timezone.utc)
    rows = []

    for ch in a.channels:
        cid, uploads, subs, title = resolve(ch)
        vids = videos(uploads, a.sample)
        if not vids:
            print(f"  {title}: keine Videos gefunden")
            continue

        clean = []
        for v in vids:
            secs = iso_seconds(v.get("contentDetails", {}).get("duration"))
            if not a.shorts and secs and secs <= 60:
                continue
            clean.append(v)
        if not clean:
            continue

        views = [int(v["statistics"].get("viewCount", 0)) for v in clean]
        med = statistics.median(views) or 1

        print(f"\n{title}  —  {de(subs)} Abonnenten"
              f"  ·  Median {de(med)} Views  ·  {len(clean)} Videos")

        for v in clean:
            pub = datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z", "+00:00"))
            age = (now - pub).days
            if not (a.min_age <= age <= a.max_age):
                continue
            vw = int(v["statistics"].get("viewCount", 0))
            ratio = vw / med
            if ratio >= a.min:
                rows.append((ratio, title, v["snippet"]["title"], vw, age,
                             f"https://youtu.be/{v['id']}"))

    print("\n" + "=" * 78)
    if not rows:
        print("Keine Outlier ueber der Schwelle gefunden.")
    else:
        print(f"{len(rows)} Outlier ab Ratio {a.min}:\n")
        for ratio, ch, t, vw, age, url in sorted(rows, reverse=True):
            print(f"  {ratio:5.1f}x  {de(vw):>11}  {age:>3}d  {t[:58]}")
            print(f"          {ch}  ·  {url}")
    print(f"\nKontingent verbraucht: {QUOTA['used']} von 10.000 Einheiten am Tag.")


if __name__ == "__main__":
    main()
