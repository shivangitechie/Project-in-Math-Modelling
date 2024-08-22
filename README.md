# Table of Content
-[OVERVIEW](#overview)
-[Data Gathering](#data_gathering)

# **OVERVIEW**

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

![DATA PREPROCESSING](https://github.com/user-attachments/assets/08ebdb6e-7282-4edb-bee0-65180ff580c3)

## Files:

**game_stats_preprocessing.py**: Cleans and transforms game statistics data.

**injury_stats_preprocessing.py**: Standardizes and cleans injury data.

**player_stats_rec_preprocessing.py**: Processes receiving statistics data.

**player_stats_rush_preprocessing.py**: Processes rushing statistics data.

**unstructured_text_preprocessing.py**: Combines, cleans, and applies NER to unstructured text.

## Results:

![image](https://github.com/user-attachments/assets/a5166fdf-6717-4cd7-bec8-5211c4991329)

# 3. Data Labeling

## **Objective**: Label the data to prepare it for supervised learning, creating categories or outcomes for model training.

## **Labels:** 

**1. BOOM
2. BUST
3. PLAY MEANINGFUL MINUTES
4. PLAY WITH INJURY**

The labeling has been done using the following approach:

1. PLAY WITH INJURY and PLAY MEANINGFUL MINUTES: using injury statistics data
2. BOOM AND BUST: Using Sentiment Analysis and Statistical Data

The labels are then Encoded as numbers using **One-hot-encoding**.

## **One-Hot Encoding**: Each category is represented as a binary vector, where only one element is "1" (hot) and the rest are "0" (cold). 

"Boom" → [1, 0, 0, 0]

"Bust" → [0, 1, 0, 0]

"Play Meaningful Minutes" → [0, 0, 1, 0]

"Play with Injury" → [0, 0, 0, 1]

## Files:

**data_labeling.py**: Applies labels to the dataset based on performance metrics and outcomes.


# 4. Named Entity Recognition (NER) and Sentiment Analysis for Labeling

## NER

**Objective**: Extract and classify entities from unstructured text data to identify key components such as players, teams, and locations.

![image](https://github.com/user-attachments/assets/73ce942d-8ee2-4eb6-aa9f-501f9021cedd)

**A Named Entity Recognition (NER)** model is typically implemented as a sequence labeling model that takes a piece of text as input and classifies each word (or token) into predefined entity categories like "PERSON," "ORGANIZATION," "LOCATION," etc. For our Fantasy Football AI project, the NER model might be used to identify entities like player names, team names, injury mentions, and other relevant information from unstructured text data such as news articles, commentaries, or reports.

### **Architecture of an NER Model:**

**Input Layer:**

The input is typically a sequence of words or tokens. For example:

["Tom", "Brady", "threw", "3", "touchdowns", "for", "the", "Buccaneers"]

**Word Embeddings:**

The words are converted into numerical representations using word embeddings (e.g., Word2Vec, GloVe, or contextual embeddings like BERT).

For example:

["Tom" → [0.12, -0.45, ...], "Brady" → [0.34, 0.67, ...], ...]

**Sequence Model (Transformer):**

The sequence of word embeddings is processed using a model that captures contextual information. 

Each output vector is passed through a fully connected layer with a softmax activation function, which outputs a probability distribution over possible entity classes (e.g., "PLAYER_NAME," "TEAM_NAME," "O," etc.).

**Output Layer (Entity Tags):**

The final output is a sequence of entity tags corresponding to each input token:

["Tom" → "PLAYER_NAME", "Brady" → "PLAYER_NAME", "threw" → "O", "3" → "O", "touchdowns" → "O", "for" → "O", "the" → "O", "Buccaneers" → "TEAM_NAME"]

## Sentiment Analysis

Combining Named Entity Recognition (NER) with sentiment analysis can significantly enhance the understanding of context around the identified entities. In the Fantasy Football AI project, combining these techniques allows us to extract specific player mentions (through NER) and analyze the sentiment of the text associated with those mentions (through sentiment analysis). This approach helps determine not only which players are being discussed but also whether the discussion is positive, negative, or neutral—critical for predicting player performance.

**Workflow**: Combining NER with Sentiment Analysis

Use NER to identify relevant entities in the text, such as player names, teams, or injury mentions.

Text: "Tom Brady's performance last night was phenomenal!"

NER Output: [("Tom Brady", "PLAYER_NAME")]

**Sentiment Analysis:**

Perform sentiment analysis on the text to determine whether it conveys a positive, negative, or neutral sentiment.

Sentiment Output: Positive (Score: 0.92)

**Contextual Linking:**

Link the identified entities to the sentiment analysis results. This way, we know which sentiment corresponds to which player or team.

"Tom Brady" → Positive Sentiment (Score: 0.92)

The labels **BOOM** and **BUST** are assigned to players based on these sentiment analysis scores.

The entire data is the then combined together to be fed to the *Deep Learning Model* and *Linear Regression Model*.

## Files:

**unstructured_text_preprocessing.py**: Utilizes SpaCy to perform NER and extract named entities.


# 5. Deep Learning Model

**Objective**:Develop a deep learning model to predict player performance or game outcomes based on preprocessed features.

![image](https://github.com/user-attachments/assets/cadb47e1-07b5-4866-ad17-63bfa9a507a3)

## Input Layer:

The input layer is where the model receives data. Each neuron in this layer corresponds to a feature in the dataset (e.g., player stats, game scores).
It simply passes the data into the next layer for further processing.

## Hidden Layers:

Hidden layers are where the actual learning happens. These layers consist of multiple neurons, each performing computations on the input data.

**Activation Functions**: Neurons in hidden layers often use activation functions like ReLU, which introduce non-linearity, enabling the model to learn complex patterns.

**Purpose**: Each hidden layer extracts different levels of features or patterns from the input data. For instance, in our fantasy football model, one layer might learn patterns related to player performance, while another might capture correlations between injuries and game outcomes.

## Output Layer:

The output layer produces the final prediction or classification based on the processed information from hidden layers.

**Activation Function**: In classification tasks, the output layer usually uses a softmax function, which outputs probabilities for each class (e.g., predicting whether a player is a "Boom," "Bust," etc.).

## Dropout Layers (Optional):

Dropout layers are used to prevent overfitting by randomly disabling some neurons during training, encouraging the model to generalize better to new data.

## Files:

**deep_learning_model.py**: Defines and trains a neural network model.


# 6. Histogram of Deep Learning Model Accuracy

**Objective**: Visualize the distribution of model accuracy across the test data. 

## Files:

**histogram_accuracy.py**: Generates a histogram of accuracy scores.

## Results:

![Classification_accuracy](https://github.com/user-attachments/assets/62c287f1-f97a-46c7-83ad-94d4ed586007)


# 7. Regression Model

**Objective**: Build and evaluate a regression model to predict continuous outcomes using numerical features.

## Input Features:

The input features could include a variety of factors such as:

Player statistics (yards, touchdowns, completion percentage, etc.)

Injury status (whether a player is fully fit, slightly injured, etc.)

## Linear Relationship:

The Linear Regression model assumes that these input features have a linear relationship with the target variable (fantasy points). For instance, more touchdowns and better sentiment might linearly increase the predicted points.

## Model Training:

The model is trained on historical data. It learns the relationship between player statistics and the fantasy points they actually scored in past games. The model adjusts the weights for each feature to minimize the prediction error (e.g., using Mean Squared Error).

## Prediction:

Once trained, the model can predict the fantasy points a player might score in a future game, given new input data (like updated stats or sentiment).

## Evaluating the Model

In this project, we evaluate the Linear Regression model using the Mean Squared Error (MSE) metric, which measures the average squared difference between the actual points and the predicted points. A lower MSE indicates a better fit.


## Why Linear Regression?

Even though deep learning models are more sophisticated, Linear Regression serves as a baseline model. It provides a straightforward benchmark to compare how much value more complex models (like deep learning) bring. While Linear Regression is limited in capturing non-linear relationships, it’s simple and interpretable, making it useful for quick initial predictions.

![image](https://github.com/user-attachments/assets/7898364f-4262-4e56-ae85-8c6b12245385)

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
