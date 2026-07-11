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

        "application": APP_NAME,

        "version": VERSION,

        "hostname": socket.gethostname()

    }


@app.route("/health")
def app_health():

    return health()


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

    app.run(

        host=HOST,

        port=PORT,

        debug=True

    )
