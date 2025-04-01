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
    """Convert text into list of lowercase words."""
    tokens = nltk.word_tokenize(text)
    return [word.lower() for word in tokens if word.isalnum()]


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
