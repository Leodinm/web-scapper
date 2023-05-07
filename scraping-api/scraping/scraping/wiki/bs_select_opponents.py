from bs4 import BeautifulSoup


def get_opponents(html):
    soup = BeautifulSoup(html, 'html.parser')

    tables=soup.select('table[class="wikitable"]')
    # print(tables)
    matches=tables[0]
    trs= matches.select("tr")
    oppoonents =[]
    for tr in trs:
        opponent={}
        opponent_node=tr.select_one("td:nth-child(3)")
        # print('opponent_node',opponent_node)
        if not opponent_node :
            continue
        # oppoonents_nodes= tds[2]
        opponent_link=None
        opponent_name= opponent_node.string
        if opponent_name is  None:
           a= opponent_node.select_one("a")
           opponent_link=f"https://en.wikipedia.org{a['href']}"
           print(opponent_link)
           opponent_name=a.string
        opponent['name']=opponent_name.strip('\n')
        opponent['link']=opponent_link
        oppoonents.append(opponent)

    return oppoonents