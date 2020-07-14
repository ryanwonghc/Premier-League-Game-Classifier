# Premier-League-Game-Recommender

Techniques/tools used:
- Data Scraping: BeautifulSoup
- Python: numpy, pandas, matplotlib, seaborn, scikit-learn (Decision Trees, Random Forests, Linear Regression, Cross Validation, Pipeline), imblearn (SMOTE)

## Overview
I analyzed [this](https://www.kaggle.com/thefc17/epl-results-19932018) dataset of Premier League match statistics as well as data scraped from [this](https://www.fourfourtwo.com/us/100-best-premier-league-matches-ever) FourFourTwo article about the 100 best Premier League matches of all time in order to determine the factors that make a Premier League match "good" or "memorable". I then **built a tool to recommend a list of the best Premier League matches of the past to watch**. I performed feature engineering with a combination of the aforementioned dataset and additional data I scraped to find the strongest predictors regarding what makes a game memorable. I tested three different classifier models on the data: logistic regression, random forest, and decision trees. I used F1 score to evaluate the precision and recall of the models and concluded that a decision tree is the best model to use. I then fit a decision tree onto the entire dataset, performed hyperparameter tuning, and obtained an F1 score of 0.39 (recall score: 0.26, precision score: 0.81).

**An in depth description of this project can be found [here](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Premier-League-Game-Classifier.md).**

## Relevant Notebooks
The relevant jupyter notebooks can be found here:
- [Data Cleaning and Exploration](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Data%20Cleaning%20and%20Exploration.ipynb)
- [Model Building](https://github.com/ryanwonghc/Premier-League-Game-Recommender/blob/master/Model%20Building.ipynb)

## Results
A decision tree outperforms both the random forest classifier and the logistic regression classifier. The largest predictor of whether or not a game is a classified as a 'Best Game' (according to my model) is the total number of goals scored in the game, as all of the recommended games were high scoring (at least 5 goals scored). Ultimately, my final model (decision tree) obtained an F1 score of 0.39 (good precision score, let down by a bad recall score). The confusion matrix is below:

<p align="center">
  <img src="/images/conmat.png"/>
</p>

The list of recommended games are as follows:
| Date       | HomeTeam          | AwayTeam          |
| ---------- | ----------------- | ----------------- |
| 23/10/1999 | Chelsea           | Arsenal           |
| 12/2/00    | West Ham United   | Bradford City     |
| 25/02/2001 | Manchester United | Arsenal           |
| 29/09/2001 | Tottenham Hotspur | Manchester United |
| 19/11/2001 | Charlton Athletic | West Ham United   |
| 7/2/04     | Everton           | Manchester United |
| 9/4/04     | Arsenal           | Liverpool         |
| 22/01/2005 | Norwich City      | Middlesbrough     |
| 1/2/05     | Arsenal           | Manchester United |
| 28/04/2007 | Everton           | Manchester United |
| 29/09/2007 | Portsmouth        | Reading           |
| 29/12/2007 | Tottenham Hotspur | Reading           |
| 21/04/2009 | Liverpool         | Arsenal           |
| 25/04/2009 | Manchester United | Tottenham Hotspur |
| 20/09/2009 | Manchester United | Manchester City   |
| 22/11/2009 | Tottenham Hotspur | Wigan Athletic    |
| 20/11/2010 | Arsenal           | Tottenham Hotspur |
| 28/08/2011 | Manchester United | Arsenal           |
| 23/10/2011 | Manchester United | Manchester City   |
| 29/10/2011 | Chelsea           | Arsenal           |
| 26/02/2012 | Arsenal           | Tottenham Hotspur |
| 22/04/2012 | Manchester United | Everton           |
| 17/11/2012 | Arsenal           | Tottenham Hotspur |
| 19/05/2013 | West Bromwich     | Manchester United |
| 23/01/2016 | Norwich City      | Liverpool         |
| 14/08/2016 | Arsenal           | Liverpool         |
| 26/11/2016 | Swansea City      | Crystal Palace    |
