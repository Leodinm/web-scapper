from parsel import Selector
import requests
import re

def get_opponents_with_info(html):
    opoonents =get_opponents(html)
    
    for o in opoonents :
        if link := o.get('link')  :
           response =requests.get(link)
           o['info'] =  get_fighter_info(response.text)

    return opoonents


def get_opponents(html):
    selector = Selector(text=html)

    matches=selector.xpath('//table[@class="wikitable"]')[0]
    # print(tables)
    trs= matches.xpath(".//tr")
    oppoonents =[]
    for tr in trs[1:]:
        opponent={
            'link':None,
            'name':None,
            'outcome':None
        }
        opponent['outcome']= tr.xpath("./td[1]/text()").get().strip('\n')
        opponent_node=tr.xpath("./td[3]")
        anchors =opponent_node.xpath('a')
        if len(anchors) ==1 :
           a =anchors[0]
           href= a.xpath("@href").get()
           opponent['link']=f"https://en.wikipedia.org{href}"
           opponent_name=a.xpath("text()").get()
        else:
            opponent_name=opponent_node.xpath("text()").get()

        opponent['name']=opponent_name.strip('\n')
        oppoonents.append(opponent)   

    return oppoonents

def get_fighter_info(html):
    selector = Selector(text=html)
    trs=selector.xpath('//table[@class="infobox vcard"]/tbody/tr')
    fighter_info={
        'name':None,
        'image':None,
        'nickname':None,
        'nationality':None,
        'height':None,
        'weight':None,
    }
    
    fighter_info['name']=trs[0].xpath('.//span/text()').get()
    image = trs[1].xpath('.//a/@href').get()
    fighter_info['image']= f"https://en.wikipedia.org{image}"
    for tr in trs[2:] :
        key : str= tr.xpath('./th/text()').get()
        value=tr.xpath('./td/text()').get()
        
        if key is None or value is None :
            continue
        if key.startswith('Nickname'):
            fighter_info['nickname']=value
        elif key.startswith('Nationality') :
             fighter_info['nationality']=value
        elif key.startswith('Height') :
             match= re.search('(?P<imperial>\d.ft \d{1,2}.in) \((?P<metric>[\d.]+.c?m)\)',value)
             if match is None:
                 print("match failed height",value)
                 continue
             fighter_info['height']= {
                 'imperial' :match.group('imperial'),
                 'metric' : match.group('metric'),
             }
        elif key.startswith('Weight') :
             match= re.search('(?P<imperial>\d{1,3}.lb) \((?P<metric>\d{1,3}.kg); (?P<eng>[\d.]+.st(?: \d+.lb)?)\)',value)
             if match is None:
                 print("match failed height",value)
                 continue
             fighter_info['weight']= {
                 'imperial' :match.group('imperial'),
                 'metric' : match.group('metric'),
                 'eng' : match.group('eng')
             }
             
         

    return  fighter_info   
