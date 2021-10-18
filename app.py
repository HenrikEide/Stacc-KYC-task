from flask import Flask, request
from flask.templating import render_template
from kycRequests import pep_check, pep_check_company

app = Flask(__name__)

@app.route("/api/name")
def pepName():
    page = request.args.get("name")
    return pep_check(page)
    

@app.route("/api/company")
def pepCompany():
    page = request.args.get("orgNr")
    return pep_check_company(page)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return pep_check(request.args.get("name"))