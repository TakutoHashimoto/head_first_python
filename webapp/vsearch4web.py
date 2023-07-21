from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Hello world from Flask!"


@app.route("/search4", methods=["POST"])
def do_search() -> str:
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    return str(search4letters(phrase, letters))


@app.route("/entry")
def entry_page() -> str:
    return render_template(
        "entry.html",
        the_title="Web版のsearch4lettersにようこそ!"
    )

app.run(debug=True)
