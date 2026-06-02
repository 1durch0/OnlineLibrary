from flask import Flask, render_template, request, jsonify
import json
import subprocess
from main import search_book


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=["POST"])
def search():
    data = request.json
    result = search_book(data["query"])
    return jsonify({"output": result})
if __name__ == "__main__":
    app.run()
