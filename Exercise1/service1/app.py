from flask import Flask, request, Response
import os
import requests
import time
import subprocess
from datetime import datetime, timezone

app = Flask(__name__)

# Config
storage_url = "http://storage:8200/log"
service2_url = "http://service2:8201/status"
vstorage_file = "/vstorage"

def get_uptime():
    try:
        with open("/proc/uptime") as f:
            return f"{float(f.readline().split()[0])/3600:.2f}"
    except:
        return "uptime error"

def get_free_disk():
    try:
        out = subprocess.check_output(["df", "-m", "/"]).decode().splitlines()
        fields = out[1].split()
        return fields[3]
    except:
        return "disk error"

def create_record():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    uptime = get_uptime()
    disk = get_free_disk()
    return f"{timestamp}: uptime {uptime} hours, free disk in root: {disk} MBytes"

@app.route("/status", methods=["GET"])
def status():
    # Service1 record
    record1 = create_record()

    # Write to Storage
    try:
        requests.post(storage_url, data=record1)
    except:
        pass

    # Write to vStorage
    with open(vstorage_file, "a") as f:
        f.write(record1 + "\n")

    # Call Service2
    try:
        resp = requests.get(service2_url)
        record2 = resp.text.strip()
    except:
        record2 = "Service2 error"

    # Return combined
    combined = record1 + "\n" + record2
    return Response(combined, mimetype="text/plain")

@app.route("/log", methods=["GET"])
def get_log():
    try:
        resp = requests.get(storage_url)
        return Response(resp.text, mimetype="text/plain")
    except:
        return "Storage unreachable", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)
