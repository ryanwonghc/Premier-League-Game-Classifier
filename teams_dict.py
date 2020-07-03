import pandas as pd

df = pd.read_csv('teams.csv')

#print(df)

team_dict = {}
index = 0

for team in df['Team List']:
    team_dict[str(team)] = index
    index = index + 1

team_list = []
for key in team_dict:
    team_list.append(key)
