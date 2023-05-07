import requests
import sys
# from bs_opponents import get_opponents
from scraping.wiki.wiki_fighters import get_opponents,get_fighter_info,get_opponents_with_info
# from bs_select_opponents import get_opponents
import json


def defaught(args):

   if len(args) ==0 :
      raise Exception("ooops you missing argv ")

   target = args[0]
   url = args[1]
   output = args[2]
   handler =None

   if target =='ops':
      handler=get_opponents
   elif target =='ops+info':
      handler=get_opponents_with_info
   elif target =='info':
      handler=get_fighter_info

   response =requests.get(url)

   results= handler(response.text)






   return results
      