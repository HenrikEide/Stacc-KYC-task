from flask import Flask, request

app = Flask(__name__)

@app.route("/api/name")
def test():
    page = request.args.get("name")
    return f"please work {page}"