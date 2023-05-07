

import importlib


def run_scraper(scraper,args):
  

    try:
        scraper=importlib.import_module(f"scraping.{scraper}.main")
        entry_point= getattr(scraper,"defaught")
        results=entry_point(args)
        return  results
        
    except ModuleNotFoundError as e:
        print(f"scraper {scraper} not found !! {e}")