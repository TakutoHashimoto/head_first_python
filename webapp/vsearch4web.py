from flask import Flask, render_template, request
from vsearch import search4letters
from markupsafe import escape


app = Flask(__name__)


def log_request(req: str, res: str) -> None:
    """
    リクエストとレスポンスをログファイルに記録する
    """
    with open("log/vsearch.log", "a") as log:
        print(
            req.form,
            req.remote_addr,
            req.user_agent,
            res,
            file=log,
            sep=" | ")


@app.route("/")
@app.route("/entry")
def entry_page() -> str:
    return render_template(
        "entry.html",
        the_title="Web版のsearch4lettersにようこそ!"
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


@app.route("/viewlog")
def view_log() -> str:
    contents = []
    with open("log/vsearch.log") as log:
        for line in log:
            contents.append([])
            for item in line.split("|"):
                contents[-1].append(escape(item))

    return str(contents)


if __name__ == "__main__":
    app.run(debug=True)
