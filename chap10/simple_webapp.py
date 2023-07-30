from flask import Flask, session

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "シンプルなWebアプリケーションからこんにちは。"


def check_logged_in() -> bool:
    if "logged_in" in session:
        return True
    return False


@app.route("/login")
def do_login() -> str:
    session["logged_in"] = True

    return "現在ログインしています"


@app.route("/page1")
def page1() -> str:
    return "これはページ1です。"


@app.route("/page2")
def page2() -> str:
    return "これはページ2です。"


@app.route("/page3")
def page3() -> str:
    return "これはページ3です。"


@app.route("/logout")
def do_logout() -> str:
    session.pop("logged_in")

    return "現在ログアウトしています。"


@app.route("/status")
def check_status() -> str:
    if "logged_in" in session:
        return "現在ログインしています。"
    return "ログインしていません。"


app.secret_key = "**********"
if __name__ == "__main__":
    app.run(debug=True)