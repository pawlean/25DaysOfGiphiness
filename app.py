import os
from datetime import date

from flask import Flask, render_template

from giphy_api import get_gifs
from graphiql_request import get_profiles

app = Flask(__name__)

@app.route("/")
def index():
    giphy_res = get_gifs()
    print(f"today's day: {date.today().day}", type(date.today().day))
    return render_template("index.html", gifs=giphy_res, enumerate=enumerate, this_day=date.today().day)

@app.route("/about")
def about():
    profiles = get_profiles()
    return render_template("about.html", members=profiles, enumerate=enumerate)

if 'PORT' in os.environ:
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
    app.run(debug=True)
