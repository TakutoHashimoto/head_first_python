from flask import Flask, render_template, request, escape, session
from vsearch import search4letters
from markupsafe import escape
from database_connector import UseDatabase
from checker import check_logged_in


app = Flask(__name__)

app.config["dbconfig"] = {
        "host": "127.0.0.1",
        "user": "vsearch",
        "password": "vsearchpasswd",
        "database": "vsearchlogDB"
    }

@app.route("/login")
def do_login() -> str:
    session["logged_in"] = True

    return "現在ログインしています。"


@app.route("/logout")
def do_logout() -> str:
    session.pop("logged_in")

    return "現在ログアウトしています。"


def log_request(req: 'flask_request', res: str) -> None:
    """
    Webリクエストの詳細と結果をロギングする
    """

    with UseDatabase(app.config["dbconfig"]) as cursor:
        _SQL = """
                INSERT INTO log
                (phrase, letters, ip, browser_string, results)
                VALUES
                (%s, %s, %s, %s, %s)
                """

        cursor.execute(
        _SQL, (req.form["phrase"],
                req.form["letters"],
                req.remote_addr,
                req.user_agent.browser or "",
                res)
        )


@app.route("/search4", methods=["POST"])
def do_search() -> str:
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "検索結果"
    results = str(search4letters(phrase, letters))

    log_request(request, results)

    return render_template(
        "results.html",
        the_phrase=phrase,
        the_letters=letters,
        the_title=title,
        the_results=results
    )


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry.html",
        the_title="Web版のsearch4lettersにようこそ!"
    )


@app.route("/viewlog")
@check_logged_in
def view_log() -> str:
    """
    ログファイルの内容をHTMLテーブルとして表示する。
    """

    with UseDatabase(app.config["dbconfig"]) as cursor:
        _SQL =  """
                SELECT 
                    phrase,
                    letters,
                    ip,
                    browser_string,
                    results
                FROM
                    log
                """

        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ("フレーズ", "検索文字", "リモートアドレス", "ユーザーエージェント", "結果")

    return render_template(
        "viewlog.html",
        the_title="ログの閲覧",
        the_row_titles=titles,
        the_data=contents
    )


app.secret_key = "**********"


if __name__ == "__main__":
    app.run(debug=True)
