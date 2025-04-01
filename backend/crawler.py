import requests
from bs4 import BeautifulSoup
import json
import os

DATA_DIR = "data"
PAGES_FILE = os.path.join(DATA_DIR, "pages.json")

# List of websites you want to crawl

SEED_URLS = [
    "https://www.python.org",
    "https://www.djangoproject.com",
    "https://flask.palletsprojects.com",
    # Can add more websites here
]

MAX_PAGES = 100  # Limit so it doesn't go to infinite

def get_links(url):
    """Extract all links from a webpage."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return [], ""

        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for a in soup.find_all("a", href=True):
            link = a["href"]
            if link.startswith("http"):
                links.add(link)
        text = soup.get_text(separator=" ", strip=True)
        return list(links), text

    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return [], ""

def start_crawling(keyword=None):
    crawled = {}
    to_crawl = []

    if keyword:
        query_url = f"https://www.google.com/search?q={keyword}"
        to_crawl.append(query_url)
    else:
        to_crawl = list(SEED_URLS)

    count = 0

    while to_crawl and count < MAX_PAGES:
        url = to_crawl.pop(0)
        if url in crawled:
            continue

        print(f"Crawling: {url}")
        links, text = get_links(url)
        crawled[url] = {
            "url": url,
            "content": text
        }
        to_crawl.extend(links)
        count += 1

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(PAGES_FILE, "w") as f:
        json.dump(crawled, f, indent=2)

    print(f"Crawling complete. {len(crawled)} pages saved.")
    return f"Crawled {len(crawled)} pages."