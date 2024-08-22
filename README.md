# **NFL Data Analysis and Modeling Project**

This project aims to analyze NFL data through a series of steps involving data gathering, preprocessing, labeling, and advanced modeling techniques. The workflow includes various stages: from collecting and preparing data to developing and evaluating models. This README provides an overview of each step, along with insights and practical details.

# 1. Data Gathering

**Objective**: Collect and consolidate various sources of NFL data to create a comprehensive dataset for analysis.

## Files:
**extract_injury_data.py**: Scrapes and saves injury data to nfl_injuries_2023_full.csv.

**fetch_and_save_game_stats.py**: Retrieves and saves game statistics to games_stats.csv.

**fetch_and_save_receiving_stats.py**: Collects and saves player receiving statistics to player_stats_rec.csv.

**fetch_and_save_rushing_stats.py**: Gathers and saves player rushing statistics to player_stats_rush.csv.

**scrape_espn_articles.py**: Extracts text data from ESPN articles, saved to espn_articles_2023/all_articles.txt.

**scrape_fantasy_usage_notes.py**: Retrieves and saves fantasy football usage notes to fantasy_usage_notes_2023/all_weeks_usage_notes.txt.

**scrape_glossary.py**: Scrapes and saves American football glossary terms to american_football_glossary.txt.


## Results:

![image](https://github.com/user-attachments/assets/da44615b-92dd-4a9a-b86b-6466b3f69fa1)

# 2. Data Preprocessing

**Objective**: Clean, transform, and structure raw data to prepare it for analysis and modeling.

## Files:

**game_stats_preprocessing.py**: Cleans and transforms game statistics data.

**injury_stats_preprocessing.py**: Standardizes and cleans injury data.

**player_stats_rec_preprocessing.py**: Processes receiving statistics data.

**player_stats_rush_preprocessing.py**: Processes rushing statistics data.

**unstructured_text_preprocessing.py**: Combines, cleans, and applies NER to unstructured text.

## Results:

![image](https://github.com/user-attachments/assets/a5166fdf-6717-4cd7-bec8-5211c4991329)

# 3. Data Labeling

**Objective**: Label the data to prepare it for supervised learning, creating categories or outcomes for model training.

## Files:

**data_labeling.py**: Applies labels to the dataset based on performance metrics and outcomes.


# 4. Named Entity Recognition (NER)

**Objective**: Extract and classify entities from unstructured text data to identify key components such as players, teams, and locations.

![image](https://github.com/user-attachments/assets/73ce942d-8ee2-4eb6-aa9f-501f9021cedd)


## Files:

**unstructured_text_preprocessing.py**: Utilizes SpaCy to perform NER and extract named entities.


# 5. Deep Learning Model

**Objective**:Develop a deep learning model to predict player performance or game outcomes based on preprocessed features.

## Files:

**deep_learning_model.py**: Defines and trains a neural network model.


# 6. Histogram of Deep Learning Model Accuracy

**Objective**: Visualize the distribution of model accuracy across different evaluation runs.

## Files:

**histogram_accuracy.py**: Generates a histogram of accuracy scores.

## Results:

![Classification_accuracy](https://github.com/user-attachments/assets/62c287f1-f97a-46c7-83ad-94d4ed586007)


# 7. Regression Model

**Objective**: Build and evaluate a regression model to predict continuous outcomes using numerical features.

## Files:

**regression_model.py**: Implements a regression model to predict player or game performance.


# 8. Model Evaluation

**Objective**: Compare the performance of different models (deep learning vs. regression) to determine the most effective approach.

## Files:

**model_evaluation.py**: Compares the performance of deep learning and regression models.


# 9. Player Comparison Radar Plot

**Objective**: Visually compare player performance metrics using radar charts.

## Files:

**radar_plot.py**: Generates radar charts for comparing player metrics.

## Results:

![comparison_plot](https://github.com/user-attachments/assets/ee327799-d6d9-4cc2-9e08-efd227753a7e)


![Boom_Bust_Percentage](https://github.com/user-attachments/assets/2ba5b928-0ca5-4b53-a1bf-00c2c98a0544)


# Detailed Analysis and Requirements

For a more in-depth understanding of each step, including detailed code explanations, requirements, and libraries used, please refer to the individual README files associated with each script:

**Data Gathering**: Detailed in extract_injury_data.py, fetch_and_save_game_stats.py, fetch_and_save_receiving_stats.py, fetch_and_save_rushing_stats.py, scrape_espn_articles.py, scrape_fantasy_usage_notes.py, and scrape_glossary.py.

**Data Preprocessing**: Detailed in game_stats_preprocessing.py, injury_stats_preprocessing.py, player_stats_rec_preprocessing.py, player_stats_rush_preprocessing.py, and unstructured_text_preprocessing.py.

**Data Labeling**: Detailed in data_labeling.py.

**Named Entity Recognition (NER)**: Detailed in unstructured_text_preprocessing.py.

**Deep Learning Model**: Detailed in deep_learning_model.py.

**Histogram of Deep Learning Model Accuracy**: Detailed in histogram_accuracy.py.

**Regression Model**: Detailed in regression_model.py.

**Model Evaluation**: Detailed in model_evaluation.py.

**Player Comparison Radar Plot**: Detailed in radar_plot.py.

These README files provide step-by-step instructions, explanations, and dependencies required for each part of the project.

# Practical Usage

This project can be utilized for:

**Performance Analysis**: Assessing player and team performance through various metrics.

**Predictive Modeling**: Predicting game outcomes or player statistics using machine learning models.

**Text Analysis**: Extracting insights from unstructured text data, such as articles and usage notes.

**Comparative Analysis**: Visualizing player statistics to identify strengths and weaknesses.

## Instructions for Use:

**Data Gathering**: Run the scripts to collect and save data.

**Data Preprocessing**: Apply preprocessing scripts to clean and transform the raw data.

**Data Labeling**: Label the data as required for training and testing.

**NER and Text Processing**: Perform NER and text cleaning to prepare text data.

**Model Development**: Train deep learning and regression models using the processed data.

**Evaluation**: Assess model performance and compare results.

**Visualization**: Generate radar plots and histograms to visualize and interpret results.

# Future Steps

To enhance the project further, consider the following:

**Model Optimization**: Explore hyperparameter tuning and advanced techniques to improve model accuracy and efficiency.

**Additional Data Sources**: Incorporate more diverse data sources to enrich analysis and modeling.

**Real-Time Analysis**: Implement real-time data processing and prediction for ongoing games or seasons.

**User Interface**: Develop a user-friendly interface or dashboard for easier interaction with the data and models.

**Advanced Text Analysis**: Apply more sophisticated NLP techniques, such as sentiment analysis or topic modeling.
