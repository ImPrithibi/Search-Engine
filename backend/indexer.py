import json
import os
import re
from collections import defaultdict
import nltk

nltk.download('punkt')

DATA_DIR = "data"
PAGES_FILE = os.path.join(DATA_DIR, "pages.json")
INDEX_FILE = os.path.join(DATA_DIR, "index.json")


def tokenize(text):
    """Tokenize text into clean lowercase words."""
    return re.findall(r'\b\w+\b', text.lower())


def build_index():
    """Build inverted index from crawled pages."""
    if not os.path.exists(PAGES_FILE):
        print("No pages.json found. Please crawl first.")
        return "No pages found."

    with open(PAGES_FILE, "r") as f:
        pages = json.load(f)

    index = defaultdict(list)

    for url, data in pages.items():
        words = tokenize(data["content"])
        unique_words = set(words)
        for word in unique_words:
            index[word].append(url)

    # Save index to file
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

    print(f"Inverted index built. {len(index)} unique words indexed.")
    return f"Indexed {len(index)} unique words."
