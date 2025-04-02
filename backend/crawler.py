import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import RatelimitException
import time

SEED_URLS = [
    "https://www.python.org",
    "https://www.djangoproject.com",
    "https://flask.palletsprojects.com",
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

def get_search_results(keyword, max_results=10):
    try:
        with DDGS() as ddgs:
            results = []
            for r in ddgs.text(keyword, region="wt-wt", safesearch="off"):
                results.append(r)
                if len(results) >= max_results:
                    break
            return results
    except RatelimitException:
        print("Rate limited. Returning empty result.")
        return []  # ← Instead of sleeping

    with DDGS(headers=headers) as ddgs:
        for r in ddgs.text(keyword, region="wt-wt", safesearch="off"):
            results.append(r)
            if len(results) >= max_results:
                break
    return results


def start_crawling(keyword):
    print(f"Searching web for '{keyword}'...")

    to_crawl = get_search_results(keyword, max_results=10)
    crawled = set()  # ← Add this here

    crawled_urls = []

    for url in to_crawl:
        if url["href"] in crawled:
            continue
        crawled.add(url["href"])  # ← And add this here

        print(f"Fetched: {url['href']}")
        crawled_urls.append(url["href"])

    print(f"Crawling complete. {len(crawled_urls)} pages fetched.")
    return "Crawling complete", crawled_urls

