# Premier League Game Recommender

[Project Github Repository](https://github.com/ryanwonghc/Premier-League-Game-Recommender)

Techniques/tools used:
- Data Scraping: BeautifulSoup
- Python: numpy, pandas, matplotlib, seaborn, scikit-learn

### Overview
I analyzed [this](https://www.kaggle.com/thefc17/epl-results-19932018) dataset of Premier League match statistics as well as data scraped from [this](https://www.fourfourtwo.com/us/100-best-premier-league-matches-ever) FourFourTwo article about the 100 best Premier League matches of all time in order to determine the factors that make a Premier League match 'good' or 'memorable'. I then **built a tool to recommend a list of the best Premier League matches of the past to watch (matches prior to the 2010-2011 season, which is when I began following the Premier League)**. I tested three different classifier models on the data: logistic regression, random forest, and decision trees. I used F1 score to evaluate the precision and recall of the models and
**need to finish, write results**

### Motivation
Football (soccer) has always been a passion of mine. I grew up a Manchester United fan and idolized players such as Cristiano Ronaldo and Wayne Rooney, hoping to one day fulfill my dreams of playing in the Premier League. I fell well short of my lofty childhood ambitions but my love for the sport never faded and I follow the [Premier League](https://www.premierleague.com/) religiously to this day. I began following the Premier League during the 2010-2011 season, and I became used to watching games every week. During the COVID-19 pandemic, all Premier League games were postponed, and, craving my weekly football fix, I decided to build a tool to recommend past matches (prior to 2010-2011) to watch.

### Methodology
To complete this project, I took the following steps:
1. Data Collection
2. Data Cleaning
3. Data Exploration
4. Model Building

### Data Collection
In this section, I describe the data that I obtained and the csv files they are stored in (accessible via [Github Repository](https://github.com/ryanwonghc/Premier-League-Game-Recommender))

1. EPL_Set.csv
[This](https://www.kaggle.com/thefc17/epl-results-19932018) kaggle dataset contains information from all Premier League games played since its inception (1992-1993). The information is only complete from the '95 - '96 season onwards and thus I discarded all data before this season. I stored this data in the file EPL_Set.csv.

2. best_games.csv
This file contains data from [this](https://www.fourfourtwo.com/us/100-best-premier-league-matches-ever) FourFourTwo article about the 100 best Premier League matches of all time. I obtained this data through web scraping. I analyzed this the data from the EPL_Set.csv dataset corresponding to each game in this list in order to determine the factors that make a Premier League match 'good' or 'memorable'. The relevant code is in the ['best_games_scraper.py'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/best_games_scraper.py) file.

3. teams.csv
This file contains a list of all teams that have played in the Premier League since its inception. I obtained this data by scraping [this](https://en.wikipedia.org/wiki/List_of_Premier_League_clubs) wikipedia page. The relevant code is in the ['team_scraper.py'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/team_scraper.py) file.

4. rivalries.csv
This file contains a list of all known Premier League rivalries. This is important because I later explored whether or not a rivalry game made a game more likely to be memorable. I obtained this data by scraping [this](https://en.wikipedia.org/wiki/List_of_sports_rivalries_in_the_United_Kingdom) wikipedia page. The relevant code is in the ['rival_scraper.py'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/rival_scraper.py) file.

5. points_history.csv
This file contains a list of the total Premier League points accumulated by each Premier League team since the inception of the Premier League. This is important because I used points accumulated as a metric to measure team success/popularity, then explored whether or not team popularity/success contributes to making a match memorable. I obtained this data by scraping [this](https://en.wikipedia.org/wiki/Premier_League_records_and_statistics) wikipedia page. The relevant code is in the ['total_points_scraper.py'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/total_points_scraper.py) file.

### Data Cleaning
In order to

1. Drop Data Prior to '95 - '96 Season
Data was incomplete prior to this season, so I could not use earlier data. Thus I removed the data from the dataset.

2. Drop 'Div' Column
This column in the dataset indicated which division the game was played in. Since the games in this dataset are Premier League games, this column is irrelevant.

3. Standardize Team Names
As I collected data from several different sources, some team names were inconsistent. For example, 'Queens Park Rangers' was named 'QPR' and 'Queens Park' in my data. To resolve this issue, I used the list of team names from the 'teams.csv' file as the standard naming convention and used difflib library to find the closest name from the list of standard names to each name not in the list in the data. The relevant code can be found in the ['standardize_names.py'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/standardize_names.py) file.

4. Standardize Dates
There was some inconsistency in the collected data as some dates are recorded in the format DD/MM/YYYY, while some are in the format MM/DD/YYYY. Furthermore, some dates only have two digits to represent the year. This posed a problem when I was trying to compare dates of different matches. To resolve this issue, I converted all dates to DD/MM/YYYY format.

5. 'Best Game' Column
I added a column to represent whether a game is in the list of 'Best Games' (binary variable). This will be the column I try to predict with my classification models. A problem that I had with this was when comparing game information between the games in the dataset and the games in the 'Best Games' set, I found that the two sets of data did not always have matching dates for the same game (sometimes the dates were +/- one day). To resolve this issue, I used datetime and timedelta objects to allow for dates that differed by at most one day.

After this stage, I ended up with a dataframe with 8740 entries and 9 features. The relevant code is in the ['Data Cleaning and Exploration.ipynb'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Data%20Cleaning%20and%20Exploration.ipynb) file.

### Data Exploration
In this section, I made 6 hypotheses regarding what constitutes a 'Best Game' and added column features to the dataframe to test these hypotheses. The hypotheses are as follows:

A statistically significant portion of games in the 'Best Games' set ...
1. Involve popular/successful teams
2. Are games played between rivals
3. Involve comeback wins
4. Are high scoring games
5. Are close games
6. Are played during the latter stages of the season

1. A statistically significant portion of games in the 'Best Games' set involve popular/successful teams
To test this hypothesis, I first calculated the frequency at which each team appeared in the set of 'Best Games'. I then graphed the data in a bar chart, shown below:
<p align="center">
  <img src="/images/fig1.png"/>
</p>
![Team Frequency](/images/fig1.png)

**Verdict: Correct**
2. A statistically significant portion of games in the 'Best Games' set are games played between rivals
3. A statistically significant portion of games in the 'Best Games' set involve comeback wins
4. A statistically significant portion of games in the 'Best Games' set are high scoring games
5. A statistically significant portion of games in the 'Best Games' set are close games
6. A statistically significant portion of games in the 'Best Games' set are played during the latter stages of the season

After this stage, I ended up with a dataframe with 8740 entries and 16 features. The relevant code is in the ['Data Cleaning and Exploration.ipynb'](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Data%20Cleaning%20and%20Exploration.ipynb) file.

### Model Building and Performance


1. Web scraping - rivalries, team performance, list of all premier league teams (BeautifulSoup)
2. Standardize team names
3. Data exploration
- find that most successful teams appear more often

## Limitations
### Future Work
future: betting odds (upset)
rank the games from best to worst (rn it is logistic)
