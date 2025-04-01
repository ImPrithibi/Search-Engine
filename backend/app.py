from flask import Flask, request, jsonify
from flask_cors import CORS
import search 
import crawler

app = Flask(__name__)
CORS(app)

# This is doing health check
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
    return jsonify({"query": query, "results": results})

# Crawl endpoint
@app.route('/crawl')

def crawl_endpoint():
    status = crawler.start_crawling()
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
