import pandas as pd

df = pd.read_csv('teams.csv')

team_dict = {}
index = 0

# Build dictionary mapping premier league team to a number (sorted in alphabetical order)
for team in df['Team List']:
    team_dict[str(team)] = index
    index = index + 1

# Build list of all premier league teams
team_list = []
for key in team_dict:
    team_list.append(key)
