# Tutorial, code from: https://www.youtube.com/watch?v=XQgXKtPSzUI&t=633s

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

my_url = 'https://en.wikipedia.org/wiki/List_of_Premier_League_clubs'

# Open connection to page, store html
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')
teams = page_soup.find('table',class_='wikitable sortable')

team_list = []

for team in teams.findAll('tr'):
    name = team.findAll('td')
    if len(name) == 12:
        team_list.append(name[0].find(text=True))


df = pd.DataFrame({'Team List':team_list})
df.to_csv('teams.csv', index=False, encoding='utf-8')
