from flask import Flask, url_for, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from flask import json
from myform import loginForm
app = Flask(__name__)
app.secret_key = "jlskflsfgsdkfdsflasf"
# app.config["SECRET_KEY"] = "jlskflsfgsdkfdsflasf"


@app.route("/home")
def home():
    username = None
    if session.get("username"):
        username = session.get("username")
    return render_template("home.html", username=username)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username']
        session["username"] = username
        return username


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

