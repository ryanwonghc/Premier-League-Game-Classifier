from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
from teams_dict import team_dict

my_url = 'https://en.wikipedia.org/wiki/List_of_sports_rivalries_in_the_United_Kingdom#Association_football'

# Open connection to page, store html
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')
rivalries = page_soup.findAll('ul')
football_rivalries = rivalries[9:19]

rivalry_list = []

for rivalry in football_rivalries:
    r = rivalry.findAll('li')
    for i in r:
        temp = []
        a = i.findAll('a')
        for j in a:
            team_name = j.findAll(text=True)
            for teams in team_name:
                if teams[0] != '[' and teams in team_dict: # Make sure team is in premier league, ignore [#] (wikipedia citing sources)
                    temp.append(teams)
        if len(temp) > 1:
            rivalry_list.append(temp)

# Export
with open('rivalries.csv', mode='w') as riv_file:
    riv_write = csv.writer(riv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in rivalry_list:
        riv_write.writerow(row)
