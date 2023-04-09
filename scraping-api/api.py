from asyncio import run
import importlib
import sys
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/any/<scraper>")
def any_rout(scraper):
    results=run.run_scraper(scraper,request.args.getlist('args'))


def start():
    app.run()