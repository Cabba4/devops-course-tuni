from flask import Flask, request, Response
import os

app = Flask(__name__)
internal_file = "/internal-storage/log.txt"

os.makedirs("/storage", exist_ok=True)
if not os.path.exists(internal_file):
    open(internal_file, "a").close()

@app.route("/log", methods=["POST"])
def append_log():
    data = request.get_data(as_text=True)
    # write to internal storage
    with open(internal_file, "a") as f:
        f.write(data.rstrip("\n") + "\n")
    return "OK", 200

@app.route("/log", methods=["GET"])
def get_log():
    with open(internal_file, "r") as f:
        content = f.read()
    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200)
