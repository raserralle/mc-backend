import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Root endpoint to confirm backend is running
@app.route("/")
def home():
    return "Minecraft Scanner Backend Running"

# Serve the web UI
@app.route("/web")
def web():
    return send_from_directory("web", "index.html")

# Endpoint for scanner to submit results
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No JSON received"}), 400

    print("Received:", data)  # This will show in Railway logs

    return jsonify({"status": "ok"}), 200

# Required for Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
