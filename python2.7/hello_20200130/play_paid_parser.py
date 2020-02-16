# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from jjutils.Game import Game
#from Game import Game


url ="https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfcGFpZF9HQU1FEAcYAw%3D%3D:S:ANO1ljLtt38&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljJCqyI"
#url = "https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c"
#url = "https://www.naver.com"

res = requests.get(url)
print(res.encoding)

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.ZmHEEd')
#print(">>>>>>>>>>>>>>", len(card_list), card_list[0].get('class'))

#print(">>>>>>>>>>>>>>", card_list.find_all('class'))

games = []
for i in card_list:
    cards = i.select('.ImZGtf')
    #print(">>>>>>>>>>>>>>", len(cards), cards)
    for c in cards:
        games.append(Game(c))
        #title = c.select('div.WsMG1c')[0].text
        #title = c.select('div.WsMG1c')[0].get('title')
        #comp = c.select('div.KoLSrc')[0].text        
        #link = c.select('a[href]')[0].text
        #print(">>", len(cards), c.get('class'), [comp, title])

for i in games:
    print(i)

# 


    
