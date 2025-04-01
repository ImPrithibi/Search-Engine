import json
import os

DATA_DIR = "data"
INDEX_FILE = os.path.join(DATA_DIR, "index.json")

def load_index():
    """Load the inverted index from file."""
    if not os.path.exists(INDEX_FILE):
        print("No index found. Please run /index first.")
        return {}

    with open(INDEX_FILE, "r") as f:
        index = json.load(f)

    return index

def search_query(query):
    """Search for query and return matching URLs."""
    index = load_index()
    keywords = query.lower().split()

    result_urls = set()
    for word in keywords:
        if word in index:
            result_urls.update(index[word])

    return list(result_urls)
