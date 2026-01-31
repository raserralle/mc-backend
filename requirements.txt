from flask import Flask, request, jsonify

app = Flask(__name__)

# Stores all Minecraft server results sent from your scanner
servers = {}

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    ip = data.get("ip")

    if not ip:
        return {"error": "Missing IP"}, 400

    servers[ip] = data
    return {"status": "ok"}

@app.route("/results")
def results():
    return jsonify(servers)

@app.route("/")
def home():
    return "Minecraft Scanner Backend Running"

@app.route("/web")
def web():
    return open("web/index.html").read()
