import pandas as pd
import difflib
from teams_dict import team_list

# Read in file, store in dataframe
df = pd.read_csv('EPL_Set.csv')

# Standardize Names
# Save all team names in lists (both away teams and home teams for each game)
home_team = df['HomeTeam'].tolist()
away_team = df['AwayTeam'].tolist()

# Use difflib library to find the closest word to each team name in the two lists above from the team list (imported)
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

# Replace original columns with the update columns with new team names
df['HomeTeam'] = home_team
df['AwayTeam'] = away_team

# Export
df.to_csv('EPL_Set_Clean.csv', index=False, encoding='utf-8')
