from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv
import difflib
from teams_dict import team_list

teamA = []
teamB = []
teamAGoals = []
teamBGoals = []
date = []

for x in range(10):
    if x == 0:
        my_url = 'https://www.fourfourtwo.com/features/ranked-10-best-premier-league-matches-ever'
    else:
        order = str((x+1)*10) + '-' + str(x*10+1)
        my_url = 'https://www.fourfourtwo.com/features/fourfourtwos-best-100-premier-league-matches-ever-' + order

    # Open connection to page, store html
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, 'html.parser')
    best_games = page_soup.findAll('p')

    for bg in best_games:
        if bg.text[0:1].isdigit() and (bg.text[0:6] != '100-91'):
            desc = bg.text
            split0 = desc.split('. ')
            desc = split0[1] # Remove ranking
            split1 = desc.split(', ')
            if len(split1) < 2:
                break
            date_of_game = split1[1]
            date.append(date_of_game)
            result = split1[0]
            split2 = result.split(' ')

            #handle team names with 2 words vs 1 word
            team_name = ''
            for x in split2:
                team_name = str(team_name + ' ' + x)
                if(x[0].isdigit()):
                    scoreboard = x
                    team_name = team_name[:-3]
                    team_name = team_name.strip()
                    teamA.append(team_name)
                    team_name = ''
            team_name = team_name.strip()
            teamB.append(team_name)


            score = scoreboard.split('-')
            teamAGoals.append(score[0])
            teamBGoals.append(score[1])



df = pd.DataFrame({'teamA':teamA,'teamB':teamB,'teamAGoals':teamAGoals, 'teamBGoals':teamBGoals, 'date':date})

# Standardize Names
team_a = df['teamA'].tolist()
team_b = df['teamB'].tolist()

for index, name in enumerate(team_a):
    close = difflib.get_close_matches(name, team_list,n=2, cutoff=0.1)
    for x in close:
        if name[0] == x[0]:
            team_a[index] = x
            break

for index, name in enumerate(team_b):
    close = difflib.get_close_matches(name, team_list,n=2, cutoff=0.1)
    for x in close:
        if name[0] == x[0]:
            team_b[index] = x
            break

df['teamA'] = team_a
df['teamB'] = team_b

df.to_csv('best_games.csv', index=False, encoding='utf-8')
