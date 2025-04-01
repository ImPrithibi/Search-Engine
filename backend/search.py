import json
import os
import re

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
    index = load_index()
    keywords = re.findall(r'\w+', query.lower())

    # 👇 Add this block
    if len(keywords) == 1 and ('donald' in keywords[0] and 'trump' in keywords[0]):
        keywords = ['donald', 'trump']

    scores = {}

    for word in keywords:
        if word in index:
            for url in index[word]:
                if url not in scores:
                    scores[url] = 0
                scores[url] += 1

    ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [url for url, score in ranked_results]
