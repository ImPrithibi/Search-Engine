import requests
from bs4 import BeautifulSoup
import json
import os
from duckduckgo_search import DDGS

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

def get_search_results(keyword, max_results=5):
    """Search DuckDuckGo and get top URLs."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(keyword, region="wt-wt", safesearch="off", max_results=max_results):
            results.append(r["href"])
    return results

def start_crawling(keyword=None):
    crawled = {}
    to_crawl = []

    if keyword:
        print(f"Searching web for '{keyword}'...")
        to_crawl = get_search_results(keyword, max_results=10)
        print(f"Found {len(to_crawl)} links: {to_crawl}")
    else:
        to_crawl = list(SEED_URLS)

    count = 0
    crawled_urls = []

    while to_crawl and count < 10:
        url = to_crawl.pop(0)
        if url in crawled:
            continue

        print(f"Crawling: {url}")
        links, text = get_links(url)
        crawled[url] = {
            "url": url,
            "content": text
        }
        crawled_urls.append(url)
        count += 1

    # Save crawled data
    os.makedirs(DATA_DIR, exist_ok=True)

    # Merge with old data if exists
    if os.path.exists(PAGES_FILE):
        with open(PAGES_FILE, "r") as f:
            old_crawled = json.load(f)
    else:
        old_crawled = {}

    old_crawled.update(crawled)

    with open(PAGES_FILE, "w") as f:
        json.dump(old_crawled, f, indent=2)

    print(f"Crawling complete. {len(crawled)} pages saved.")
    return f"Crawled {len(crawled)} pages.", crawled_urls
