from flask import *
from time import sleep

app = Flask(__name__)
messages = {}


@app.route("/<channel>", methods=["POST", "GET"])
def index(channel):
    if request.method == "GET":
        if channel not in messages:
            messages[channel] = []
        return render_template("index.html", channel=channel, messages=messages[channel])
    if request.method == "POST":
        if channel not in messages:
            messages[channel] = []
        messages[channel].append({"user": request.form["user"], "message": request.form["message"]})
        return redirect(f"/{channel}")
    while True:
        dict_check = messages
        sleep(0.1)
        if messages != dict_check:
            return redirect(f"/{channel}")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")