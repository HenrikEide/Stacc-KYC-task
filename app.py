from flask import Flask, request
from flask.templating import render_template
from kycRequests import pep_check

app = Flask(__name__)

@app.route("/api/name")
def test():
    page = request.args.get("name")
    result = pep_check(page)
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return pep_check(request.args.get("name"))