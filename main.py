from flask import Flask, jsonify, render_template, request
from functions.web_scraping_GPU import get_price

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def home():
    if request.method == "POST":
        search_term = request.form["term"]
        results = get_price(search_term)
        return render_template("home.html", results=results)
    else:
        results=[]
        return render_template("home.html", results=results)

@app.route("/api/gpu/price/<gpu>")
def gpu_price(gpu):
    items = get_price(gpu)
    return jsonify(items)
