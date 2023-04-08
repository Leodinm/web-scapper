import requests
import sys
# from bs_opponents import get_opponents
from scraping.wiki.wiki_fighters import get_opponents,get_fighter_info,get_opponents_with_info
# from bs_select_opponents import get_opponents
import json


def defaught():

   if len(sys.argv) ==1 :
      raise Exception("ooops you missing argv ")

   target = sys.argv[1]
   url = sys.argv[2]
   output = sys.argv[3]
   handler =None

   if target =='ops':
      handler=get_opponents
   elif target =='ops+info':
      handler=get_opponents_with_info
   elif target =='info':
      handler=get_fighter_info

   response =requests.get(url)

   results= handler(response.text)






   opponents_json= json.dumps(results,ensure_ascii=False)
   # print(len(tables))
   # print(response.text)
   with open(f'{output}.json','w',encoding='utf-8') as f:
      f.write(opponents_json.encode('ascii','ignore').decode('utf-8'))
      