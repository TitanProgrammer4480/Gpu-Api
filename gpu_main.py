from flask import Flask, jsonify
from web_scraping_GPU import get_price

app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

@app.route("/api/gpu/price/<gpu>")
def gpu_price(gpu):
    items = get_price(gpu)
    return jsonify(items)