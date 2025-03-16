import os
from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


@app.route("/")
def home():
    return(render_template("main.html"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
