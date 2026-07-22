from flask import Flask
from health import health
from metrics import metrics
from config import *

import os
import socket
import time

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def home():

    return {

        "application": os.getenv("APP_NAME", "reliability-platform"),
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "Running",
        "hostname": socket.gethostname(),
        "database": os.getenv("DB_USER")
    }


@app.route("/health")
def app_health():
    return {
        "status": "UP"
    }


@app.route("/metrics")
def app_metrics():
    return metrics()


@app.route("/cpu")
def cpu():
    return {
        "cpu": metrics()["cpu_percent"]
    }


@app.route("/memory")
def memory():
    return {
        "memory": metrics()["memory_percent"]
    }


@app.route("/disk")
def disk():
    return {
        "disk": metrics()["disk_percent"]
    }


@app.route("/uptime")
def uptime():
    return {
        "seconds": round(time.time() - START_TIME)
    }


@app.route("/slow")
def slow():
    time.sleep(15)
    return {
        "message": "Slow API completed"
    }


@app.route("/crash")
def crash():

    os._exit(1)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)
