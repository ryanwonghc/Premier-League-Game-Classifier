import pandas as pd
import difflib
from teams_dict import team_list

df = pd.read_csv('EPL_Set.csv')

# Standardize Names
home_team = df['HomeTeam'].tolist()
away_team = df['AwayTeam'].tolist()

for index, name in enumerate(home_team):
    close = difflib.get_close_matches(name, team_list,n=2, cutoff=0.1)
    for x in close:
        if name[0] == x[0]:
            home_team[index] = x
            break

for index, name in enumerate(away_team):
    close = difflib.get_close_matches(name, team_list,n=2, cutoff=0.1)
    for x in close:
        if name[0] == x[0]:
            away_team[index] = x
            break

df['HomeTeam'] = home_team
df['AwayTeam'] = away_team

df.to_csv('EPL_Set_Clean.csv', index=False, encoding='utf-8')
