from flask import Flask, request, jsonify
from flask_cors import CORS
import crawler

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Search Engine Backend is running!"})

@app.route("/search", methods=["GET"])
def search_endpoint():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    status, crawled_urls = crawler.start_crawling(keyword=query)
    if not crawled_urls:
        return jsonify({"error": "Rate limited, try again later."}), 429

    return jsonify({"status": status, "results": crawled_urls})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
