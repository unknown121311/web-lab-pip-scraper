
import requests
import time
from bs4 import BeautifulSoup
"""
sites = [
    "https://sekol.ninja",
    "https://www.mahoningctc.com",
    "https://www.python.org",
    "https://httpbin.org/status/404",
    "https://this-site-is-fake-xyz123.com",
    "https://www.github.com",
    "https://www.youtube.com",
]
for url in sites:
    started = time.perf_counter()
    try:
        r = requests.get(url, timeout=5)
        secs = r.elapsed.total_seconds()
        status = "UP " if r.ok else "DOWN"
        print(f"[{status}] {url}, Response time: {secs:.2f} seconds -> {r.status_code}")
    except requests.exceptions.RequestException:
        secs = time.perf_counter() - started
        print(f"[DOWN] {url} Response time: {secs:.2f} seconds -> could not connect")

url = "https://sekol.ninja/articles/"
try:
    r = requests.get(url, timeout=10, headers={"Accept-Encoding": "identity"})
except requests.exceptions.RequestException as exc:
    print(f"\nCould not fetch {url}: {exc}")
else:
    if not r.ok:
        print(f"\nCould not scrape {url}: HTTP {r.status_code}")
    else:
        soup = BeautifulSoup(r.text, "html.parser")

        print("\ntitle:", soup.title.get_text(strip=True) if soup.title else "(no title)")

        h1 = soup.find("h1")
        print("h1:", h1.get_text(strip=True) if h1 else "(no h1)")

        print("\nsection headings:")
        for h2 in soup.find_all("h2"):
            print(" -", h2.get_text(strip=True))

        print("\nlinks:")
        seen = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "sekol.ninja" in href and href not in seen:
                seen.add(href)
                print(" -", a.get_text(strip=True), "->", href)
"""
import re

url = "https://sekol.ninja/about-me/"
try:
    r = requests.get(url, timeout=10, headers={"Accept-Encoding": "identity"})
    r.raise_for_status()
except requests.exceptions.RequestException as exc:
    print(f"\nCould not fetch {url}: {exc}")
else:
    soup = BeautifulSoup(r.text, "html.parser")

    found = set()

    for a in soup.find_all("a", href=True):
        if a["href"].startswith("mailto:"):
            found.add(a["href"].replace("mailto:", ""))

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    for match in re.findall(pattern, soup.get_text()):
        found.add(match)

    print(f"Found {len(found)} email address(es) on {url}:")
    for email in sorted(found):
        print(" -", email)