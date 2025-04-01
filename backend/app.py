from flask import Flask, request, jsonify
from flask_cors import CORS
import crawler

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Search Engine Backend is running!"})

@app.route('/search')
def search_endpoint():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Always crawl fresh
    print(f"Searching web for '{query}'...")
    status, crawled_urls = crawler.start_crawling(keyword=query)

    return jsonify({
        "query": query,
        "status": "Crawling done. Showing fresh results.",
        "crawled": crawled_urls,
        "results": crawled_urls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
