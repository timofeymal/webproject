from flask import *


app = Flask(__name__)
messages = {}


# Выбор канала
@app.route("/", methods=["POST", "GET"])
def load_channel_picker():
    if request.method == "GET":
        return render_template("pick.html")
    if request.method == "POST":
        return redirect(f"/{request.form['channel']}")


# Канал
@app.route("/<channel>", methods=["POST", "GET"])
def load_channel(channel):
    if channel not in messages:
        messages[channel] = []
    if request.method == "GET":
        return render_template("index.html", channel=channel, messages=messages[channel])
    if request.method == "POST":
        messages[channel].append({"user": request.form["user"], "message": request.form["message"]})
        return redirect(f"/{channel}")


# Список сообщений
@app.route("/messages/<channel>")
def load_messages(channel):
    if channel not in messages:
        messages[channel] = []
    return render_template("messages.html", channel=channel, messages=messages[channel])


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")