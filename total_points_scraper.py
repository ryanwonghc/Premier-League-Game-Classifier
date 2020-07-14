from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import difflib
from teams_dict import team_list

my_url = 'https://en.wikipedia.org/wiki/Premier_League_records_and_statistics'

# Open connection to page, store html
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')
tables = page_soup.findAll('table',class_='wikitable sortable')

# Lists to store appropriate information
teams = []
total_points = []

# Store scraped information in appropriate list
for table in tables:
    rows = table.findAll('tr')
    for row in rows:
        entry = row.findAll('td')
        if len(entry) == 17 and entry[10].text[0].isdigit():
            teams.append(entry[1].find(text=True))
            points = entry[10].find(text=True)
            points_int = int(points.replace(',',''))
            total_points.append(points_int)

# Standardize Team Names
for index, name in enumerate(teams):
    close = difflib.get_close_matches(name, team_list,n=2, cutoff=0.1)
    for x in close:
        if name[0] == x[0]:
            teams[index] = x
            break

# Build dataframe with the 2 lists
df = pd.DataFrame({'Teams':teams, 'Total Points':total_points})

# Export
df.to_csv('points_history.csv', index=False, encoding='utf-8')
