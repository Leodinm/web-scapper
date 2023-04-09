from bs4 import BeautifulSoup


def get_opponents(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables=soup.find_all('table',attrs={"class": "wikitable"})
    matches=tables[1]
    trs= matches.find_all("tr")
    oppoonents =[]
    for tr in trs:
        tds=tr.find_all("td")
        if not tds :
            continue
        oppoonents_nodes= tds[2]
        opponent_name= oppoonents_nodes.string
        if opponent_name is  None:
           opponent_name= oppoonents_nodes.a.string
        
        oppoonents.append(opponent_name.strip('\n'))

    return oppoonents