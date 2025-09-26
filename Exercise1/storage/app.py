from flask import Flask, request, Response
import os

app = Flask(__name__)
log_file = "/vstorage"

@app.route("/log", methods=["POST"])
def append_log():
    data = request.get_data(as_text=True)
    with open(log_file, "a") as f:
        f.write(data + "\n")
    return "OK", 200

@app.route("/log", methods=["GET"])
def get_log():
    with open(log_file, "r") as f:
        content = f.read()
    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200)
