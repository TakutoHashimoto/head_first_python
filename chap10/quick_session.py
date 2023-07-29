from flask import Flask, session


app = Flask(__name__)

app.secret_key = "YouWillNeverGuess"

@app.route("/setuser/<user>")
def set_user(user: str) -> str:
    session["user"] = user

    return f"User値を設定: {session['user']}"


@app.route("/getuser")
def get_user() -> str:
    return f"User値の現在の設定: {session['user']}"


if __name__ == "__main__":
    app.run(debug=True)
