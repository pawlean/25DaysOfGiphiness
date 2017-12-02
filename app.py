from flask import Flask, render_template

from giphy_api import get_gifs

app = Flask(__name__)

@app.route("/")
def index():
    giphy_res = get_gifs()
    return render_template("index.html", gifs=giphy_res, enumerate=enumerate)

app.run(debug=True)
