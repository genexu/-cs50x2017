from flask import Flask, redirect, render_template, request, url_for
import os, sys
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)
    positive = 0
    negative = 0
    neutral = 0
    for tweet in tweets:
        result = analyzer.analyze(tweet)
        if result > 0:
            positive += 1
        if result < 0:
            negative += 1
        if result == 0:
            neutral += 1

    positive_percent, negative_percent, neutral_percent = positive / len(tweets) * 100, negative / len(tweets) * 100, neutral / len(tweets) * 100

    # generate chart
    chart = helpers.chart(positive_percent, negative_percent, neutral_percent)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
