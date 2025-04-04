import os
from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


@app.route("/")
def home():
    return(render_template("main.html"))

@app.route("/pull", methods=["GET", "POST"])
def reload_website():
    print("request incomming !")
    reload = request.form.get("pull_and_reload", None)
    if reload:
        print("os.system('git pull')")
        os.system("git pull")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
