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
    """Search for query and return matching URLs with basic ranking."""
    index = load_index()
    keywords = query.lower().split()

    scores = {}

    for word in keywords:
        if word in index:
            for url in index[word]:
                if url not in scores:
                    scores[url] = 0
                scores[url] += 1  # +1 score for each matching word

    # Sort URLs by score (descending)
    ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Return only URLs
    return [url for url, score in ranked_results]
