from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = "guestbook.json"

def load_entries():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_entries(entries):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

@app.route("/")
def home():
    guestbook = load_entries()
    return render_template("index.html", guestbook=guestbook)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/add", methods=["POST"])
def add_entry():
    name = request.form["name"]
    message = request.form["message"]
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entries = load_entries()
    entries.append({"name": name, "message": message, "time": time})
    save_entries(entries)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
