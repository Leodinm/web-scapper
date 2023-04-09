import importlib
import sys
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/any/<scraper>")
def any_rout(scraper):
    
    try:
        
        scraper=importlib.import_module(f"scraping.{scraper}.main")
        entry_point= getattr(scraper,"defaught")
        print(entry_point)
        return entry_point(request.args.getlist('args'))
       
    except ModuleNotFoundError:
        return f"scraper {scraper} not found !!"
    except Exception:
       return[]