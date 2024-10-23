from flask import Flask, jsonify, render_template
from functions.web_scraping_GPU import get_price

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/gpu/price/<gpu>")
def gpu_price(gpu):
    items = get_price(gpu)
    return jsonify(items)
