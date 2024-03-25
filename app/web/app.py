"Этот файл нужен для того чтобы вместе с нашим ботом зупускался веб сервер, с которым мы могли бы общаться и узнавать статистику и жизненый цикл бота"

import flask

app = flask.Flask(__name__)


@app.route("/ping")
def ping():
    return {"status": True}


def run_app():
    app.run(host="0.0.0.0", port=8000)
