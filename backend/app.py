from flask import Flask, request, jsonify
from flask_cors import CORS
import search 
import crawler
import indexer

app = Flask(__name__)
CORS(app)

# Health check
@app.route('/')
def home():
    return jsonify({"message": "Search Engine Backend is running!"})

# Search endpoint
@app.route('/search')
def search_endpoint():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = search.search_query(query)

    if not results:
        print(f"No results found for '{query}'. Crawling now...")
        status = crawler.start_crawling(keyword=query)
        indexer.build_index()
        results = search.search_query(query)

        return jsonify({
            "query": query,
            "status": f"Crawled '{query}'. Index updated.",
            "results": results
        })

    return jsonify({
        "query": query,
        "status": "Results fetched from existing index.",
        "results": results
    })


# Crawl endpoint
@app.route('/crawl')
def crawl_endpoint():
    status = crawler.start_crawling()
    return jsonify({"status": status})

# Index endpoint
@app.route('/index')
def index_endpoint():
    status = indexer.build_index()
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)