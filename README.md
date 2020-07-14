# Premier-League-Game-Recommender

Techniques/tools used:
- Data Scraping: BeautifulSoup
- Python: numpy, pandas, matplotlib, seaborn, scikit-learn (Decision Trees, Random Forests, Linear Regression, Cross Validation, Pipeline), imblearn (SMOTE)

## Overview
I analyzed [this](https://www.kaggle.com/thefc17/epl-results-19932018) dataset of Premier League match statistics as well as data scraped from [this](https://www.fourfourtwo.com/us/100-best-premier-league-matches-ever) FourFourTwo article about the 100 best Premier League matches of all time in order to determine the factors that make a Premier League match "good" or "memorable". I then **built a tool to recommend a list of the best Premier League matches of the past to watch**. I tested three different classifier models on the data: logistic regression, random forest, and decision trees. I used F1 score to evaluate the precision and recall of the models and concluded that a decision tree is the best model to use. I then fit a decision tree onto the entire dataset, performed hyperparameter tuning, and obtained an F1 score of 0.39 (recall score: 0.26, precision score: 0.81).

The relevant jupyter notebooks can be found here:
- [Data Cleaning and Exploration]()
