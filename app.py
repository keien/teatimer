import flask
from flask import request
import requests
import time
import threading

app = flask.Flask(__name__)

@app.route("/tea", methods=["POST"])
def teatimer():
    duration = request.form.get("text")
    if duration.isdigit():
        url = request.form.get("response_url")
        name = request.form.get("user_name")
        duration = int(duration)*60
        t = threading.Timer(duration, _send_response, args=(url, name))
        t.start()
        print "starting {} second timer for {}".format(str(duration), name)
        return flask.Response("timer set for {} minutes".format(str(duration/60)))
    else:
        return flask.Respose("invalid time")

def _send_response(response_url, name):
    """send response"""
    data = {"text": "{}, your tea is ready!".format(name)}
    requests.post(response_url, json=data)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8001)
