# Premier League Game Recommender

[Project Github Repository](https://github.com/ryanwonghc/Premier-League-Game-Recommender)

Techniques/tools used:
- Data Scraping: BeautifulSoup
- Python: numpy, pandas, matplotlib, seaborn, scikit-learn

### Overview
I analyzed [this](https://www.kaggle.com/thefc17/epl-results-19932018) dataset of Premier League match statistics as well as data scraped from [this](https://www.fourfourtwo.com/us/100-best-premier-league-matches-ever) FourFourTwo article about the 100 best Premier League matches of all time in order to determine the factors that make a Premier League match "good" or "memorable". I then **built a tool to recommend a list of the best Premier League matches of the past to watch (matches prior to the 2010-2011 season, which is when I began following the Premier League)**. I tested three different classifier models on the data: logistic regression, random forest, and decision trees. I used F1 score to evaluate the precision and recall of the models and
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
This file contains data from [this](https://www.fourfourtwo.com/us/100-best-premier-league-matches-ever) FourFourTwo article about the 100 best Premier League matches of all time. I obtained this data through web scraping. I analyzed this the data from the EPL_Set.csv dataset corresponding to each game in this list in order to determine the factors that make a Premier League match "good" or "memorable". The relevant code is in the ["best_games_scraper.py"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/best_games_scraper.py) file.

3. teams.csv
This file contains a list of all teams that have played in the Premier League since its inception. I obtained this data by scraping [this](https://en.wikipedia.org/wiki/List_of_Premier_League_clubs) wikipedia page. The relevant code is in the ["team_scraper.py"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/team_scraper.py) file.

4. rivalries.csv
This file contains a list of all known Premier League rivalries. This is important because I later explored whether or not a rivalry game made a game more likely to be memorable. I obtained this data by scraping [this](https://en.wikipedia.org/wiki/List_of_sports_rivalries_in_the_United_Kingdom) wikipedia page. The relevant code is in the ["rival_scraper.py"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/rival_scraper.py) file.

5. points_history.csv
This file contains a list of the total Premier League points accumulated by each Premier League team since the inception of the Premier League. This is important because I used points accumulated as a metric to measure team success/popularity, then explored whether or not team popularity/success contributes to making a match memorable. I obtained this data by scraping [this](https://en.wikipedia.org/wiki/Premier_League_records_and_statistics) wikipedia page. The relevant code is in the ["total_points_scraper.py"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/total_points_scraper.py) file.

### Data Cleaning
In order to

1. Drop Data Prior to '95 - '96 Season
Data was incomplete prior to this season, so I could not use earlier data. Thus I removed the data from the dataset.

2. Drop "Div" Column
This column in the dataset indicated which division the game was played in. Since the games in this dataset are Premier League games, this column is irrelevant.

3. Standardize Team Names
As I collected data from several different sources, some team names were inconsistent. For example, "Queens Park Rangers" was named "QPR" and "Queens Park" in my data. To resolve this issue, I used the list of team names from the "teams.csv" file as the standard naming convention and used difflib library to find the closest name from the list of standard names to each name not in the list in the data. The relevant code can be found in the ["standardize_names.py"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/standardize_names.py) file.

4. Standardize Dates
There was some inconsistency in the collected data as some dates are recorded in the format DD/MM/YYYY, while some are in the format MM/DD/YYYY. Furthermore, some dates only have two digits to represent the year. This posed a problem when I was trying to compare dates of different matches. To resolve this issue, I converted all dates to DD/MM/YYYY format.

5. "Best Game" Column
I added a column to represent whether a game is in the list of "Best Games" (binary variable). This will be the column I try to predict with my classification models. A problem that I had with this was when comparing game information between the games in the dataset and the games in the "Best Games" set, I found that the two sets of data did not always have matching dates for the same game (sometimes the dates were +/- one day). To resolve this issue, I used datetime and timedelta objects to allow for dates that differed by at most one day.

After this stage, I ended up with a dataframe with 8740 entries and 9 features. The relevant code is in the ["Data Cleaning and Exploration.ipynb"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Data%20Cleaning%20and%20Exploration.ipynb) file.

### Data Exploration
In this section, I made 6 hypotheses regarding what constitutes a "Best Game" and added column features to the dataframe to test these hypotheses. The hypotheses are as follows:

A statistically significant portion of games in the "Best Games" set ...
1. Involve popular/successful teams
2. Are games played between rivals
3. Involve comeback wins
4. Are high scoring games
5. Are close games
6. Are played during the latter stages of the season

1. A statistically significant portion of games in the "Best Games" set involve popular/successful teams
To test this hypothesis, I first calculated the frequency at which each team appeared in the set of "Best Games". I then charted the data in a bar chart, shown below:
<p align="center">
  <img src="/images/fig1.png"/>
</p>
From the chart above, it seems as though the more popular/successful teams appear in the "best games" set more often, confirming my hypothesis. The three teams with the highest count - Manchester United, Arsenal, and Liverpool - are three of most successful teams in Premier League history. I believe that this makes sense for the following reasons:
1. More successful teams tend to play in more high-stake games (games that have a large impact on the outcome of that year's premier league title race).
2. More successful teams tend to have higher viewership numbers for their games (more neutrals/rivals watch their games, and they usually have larger fanbases) and thus their games are more likely to remain in the collective memories of football fans for longer.
3. More successful teams attract the most skillful players who produce the most highlight reel worthy moments, making their games more memorable.
4. More successful teams are more likely to have more years in the premier league (3 teams get relegated to lower league divisions every year) and thus they play more premier league games, increasing their odds of playing in a memorable game.

To quantify the "popularity" or "successfulness" of the teams in each game, I gave each team a "popularity score", and summed up the two team's popularity scores to derive the popularity score for each game. I made the assumption here that the most successful teams are the most popular, and the metric I used to determine the popularity score was the total number of points the team has earned in Premier League history (Teams earn 3 points for each match won, 1 for each draw, and 0 for losses). This data was scraped from [this](https://en.wikipedia.org/wiki/Premier_League_records_and_statistics) wikipedia page.

Charting the popularity scores for each game in the "Best Games" set versus the rest of the games, I found that the median popularity score for games in the "Best Games" set is much higher than games not in the set, proving that memorable games involve successful/popular teams more often than not. The chart is shown below:
<p align="center">
  <img src="/images/fig2.png"/>
</p>

**Verdict: Correct**

2. A statistically significant portion of games in the "Best Games" set are games played between rivals
Using collected data on a list of Premier League rivalries, I used pie charts to show the ratio of rival games to non-rival games in both the "Best Games" set and the rest of the games. The charts are shown below:
<p align="center">
  <img src="/images/fig3.png"/>
</p>
Statistics:
- Number of rival games in best games set:  26
- Number of non-rival games in best games set:  60
- Number of rival games in rest of data:  582
- Number of non-rival games in rest of data:  8072

As can be seen from the chart, the proportion of rival games in the "Best Games" set is much greater than the proportion of rival games in the rest of the data. This may be because there is extra emotional significance when it comes to games in which a team beats their fierce rivals, making the games more memorable. Rival games could possible also receive more media coverage, and higher viewership numbers mean that rival games are more likely to leave a greater impression on football audiences as a whole.

In terms of absolute numbers, there are a lot more rival games not in the 'Best Games' set than there are in the rest of the data. A possible reason for this may be because when teams play in rival games, there is a lot more to lose (more pride at stake). As a result, teams may play extra cautiously in order not to lose the game. Defensive football rarely results in highlights or memorable plays and as a result the game as a whole is not memorable and not worthy of the 'Best Games' title.

**Verdict: Correct**

3. A statistically significant portion of games in the "Best Games" set involve comeback wins
I defined a comeback a game in which the team losing at half time wins the game, even though this is not always the case (teams can turn around a deficit in the same half that they fell behind in), as it was the best I could do given the collected data. I hypothesize that comeback games are more memorable than regular games because of the emotional rollercoasters that fans go through when watching these games.

I again used pie charts to show the ratio of comeback to non-comeback games in both the "Best Games" set and the rest of the games. The charts are shown below:
<p align="center">
  <img src="/images/fig4.png"/>
</p>
Statistics:
- Number of comeback games in best games set:  18
- Number of non-comeback games in best games set:  68
- Number of comeback games in rest of data:  321
- Number of non-comeback games in rest of data:  8333

As shown in the chart above, comeback wins do appear in the "Best games" set at higher rates. However, it is important to note that the proportion of comeback games in the 'Best Games' set is quite small. A reason for this could be that comebacks are rare, and there are other more significant elements of a game that make it memorable. Furthermore, there is also variance between comebacks. A team is much more likely to come back from one goal down than they are to come back from three goals down (which would make the game much more memorable than a one goal comeback).

**Verdict: Correct, but statistically insignificant**

4. A statistically significant portion of games in the "Best Games" set are high scoring games
Football has traditionally been a low scoring game, especially in comparison to other popular sports such as basketball. As a result, high scoring games are often more memorable to fans. In order to test this hypothesis, I summed up the total number of goals for each game and charted this information for the "Best Games" set as well as the rest of the data in bar charts, shown below:
<p align="center">
  <img src="/images/fig5.png"/>
</p>

Statistics:
|   | 0  | 1  |  2 | 3  | 4  | 5  | 6  |  7 |  8 | 9  | 10  |  11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Best Games  | 2  |  5 |  1 |  10 | 7  |  21 | 8  | 11  | 11  |  5 | 4  | 1  |
| Rest of Data | 726 | 1598 | 2082 | 1843 | 1313 | 637 | 285 | 115 | 43 | 11  | 1  | 0  |

From the charts above, we can come to several conclusions:
- The 'Rest of Data' set is positively skewed while the 'Best Games' set is more normally distributed.
- Only a small portion of games (9%) in the 'Best Games' set involve low numbers of goals ([low defined as less than the average number of goals scored during a football match, which is 2.6](https://www.statista.com/statistics/269031/goals-scored-per-game-at-the-fifa-world-cup-since-1930/#:~:text=FIFA%20soccer%20World%20Cup%3A%20Average,scored%20per%20games%201930%2D2018&text=At%20the%20latest%20World%20Cup,of%202.6%20goals%20per%20game.)).
    - Only ~2% of games involve 0 goals.
- The mode of the 'Best Games' set (5) is much greater than the mode of the 'Rest of Data' set (2). This suggests that the 'Best Games' are typically high scoring. The mode is almost double the average number of goals scored in an football match.
- A larger proportion of total goals scored in the 'Best Games' set are in the higher end of the range, suggesting that more often than not, 'Best Games' are high scoring games
    - The absolute number of games in the 'Best Games' set with 10 or more goals is 5 compared to 1 in the rest of the data, even though the ratio of the number of games in the 'Best Games' set to the number of games in the rest of the data is 8654:86

**Verdict: Correct**

5. A statistically significant portion of games in the "Best Games" set are close games
Close games keep fans on the edge of their seats, and it can be more fun to see your favorite team come out on top after a close game as opposed to a one-sided game. In order to test this hypothesis, I calculated the goal difference of each game (goals scored by winner - goals scored by loser). Drawn games have a goal difference of 0. I then charted this information for the "Best Games" set as well as the rest of the data in bar charts, shown below:
<p align="center">
  <img src="/images/fig6.png"/>
</p>

Statistics:
|   | 0  | 1  |  2 | 3  | 4  | 5  | 6  |  7 |  8 |
|---|---|---|---|---|---|---|---|---|---|
| Best Games  | 18  |  41 |  11 |  6 | 1  |  5 | 1  | 1  | 2  |
| Rest of Data | 2252 | 3273 | 1825 | 807 | 333 | 117 | 37 | 7 | 3 |

Both graphs are positively skewed. The mode of the 'Best Games' set is 1 goal, which suggests that a large proportion of the 'Best Games' were close games (the winning team won by one goal). However, as can be seen from the rest of the data, the majority of the games have a goal difference of one so the large number of games with a goal diffrence of one in the 'Best Games' set could just be due to a large sample size. The proportion of games with a goal difference of one in the 'Best Games' set (48%) is greater than it's counterpart in the rest of the data (38%), which suggests that my hypothesis is correct to a degree, although the two factors (appearance in 'Best Games' set, small goal difference) may not be strongly correlated.

**Verdict: Correct, but not statistically significant**

6. A statistically significant portion of games in the "Best Games" set are played during the latter stages of the season
Some Premier League games matter more than others. Games played towards the end of the season can have a large impact on the league table because at the latter stages of the season, players become fatigued both mentally and physically, so results at this stage can have a large impact on the morale of players. These games are more high-stakes as a result and can be more memorable. Furthermore, results at this stage can mathematically confirm a team's place in the league table (confirmed as champions, confirmed spot in European competition, confirmed relegation, etc.) and the fate of their rivals or teams close to them in the table, which can have a major emotional and financial impact on all relevant teams. As a Manchester United fan, Manchester City's 3-2 win over QPR in the final game of the 2011-12 season to win the premier league comes to mind.

To test this hypothesis, I assigned each month a number from 0 (August) to 9 (May), as Premier league seasons are played from August to May. I then charted the number of games played in each month. The results are as follows:
<p align="center">
  <img src="/images/fig7.png"/>
</p>

Statistics:
|   | 0  | 1  |  2 | 3  | 4  | 5  | 6  |  7 |  8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Best Games  | 4  |  13 |  12 |  10 | 6  |  3 | 8  | 4  | 10  | 16 |
| Rest of Data | 762 | 805 | 790 | 876 | 1265 | 862 | 770 | 850 | 1083 | 591 |

The mode of the 'Best Games' data is 9 (May), suggesting that a large proportion of 'Best Games' (~19%) are played towards the end of the season. The data is distributed bimodally, suggesting that my hypothesis is not quite correct. It appears that the 'Best Games' are predominantly occur near the beginning and end of the season. This data surprises me a little as I would have expected more 'Best Games' to occur in December (4). This is because firstly, more games are played in December, and secondly, a lot of big games (games starring high profile rivals) are played during the festive season to capitalize on the fact that there are more viewers and thus more revenue potential. An explanation for this could be that since December has the most games played, perform below their best due to accumulated fatigue.

**Verdict: Disproved**
- 'Best Games' occur predominantly near the beginning and the end of the season


After this stage, I ended up with a dataframe with 8740 entries and 16 features. The relevant code is in the ["Data Cleaning and Exploration.ipynb"](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Data%20Cleaning%20and%20Exploration.ipynb) file.

### Model Building and Performance




## Limitations


### Future Work
1. Betting odds
I believe that another predictor of whether or not a game is considered a "Best Game" is whether or not the game involved an upset, which is when a team defies the odds to beat the team favored to win the game. Data for betting odds for each of the matches was only available going back to 2000 so the 1995-1999 seasons would have to have been excluded from the analysis. It would be interesting to test this hypothesis and analyze the effect of the magnitude of the upset (a team with winning odds of 15/1 winning a game would be a much larger upset than a team with winning odds of 2/1)

2. Ranking the order of games in terms of rewatchability
This project generates a list of recommended games to rewatch. What it does not do is differentiate between which games are more enjoyable to rewatch than others in the set of recommended games, which is important for people with limited time to rewatch games. A future project could involve ranking each game by rewatchability.
