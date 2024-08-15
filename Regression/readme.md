# Player Points Prediction using Linear Regression

## Overview

This script builds a linear regression model to predict the number of points scored by players based on selected features (e.g., yards per reception, touchdowns, fumbles, etc.).

File: point_estimates.py

### Dependencies

Python 3.x

Scikit-learn (scikit-learn)

Pandas (pandas)

### Installation

Before running the script, make sure the necessary libraries are installed:

pip install scikit-learn pandas

### Code Explanation

**Selecting Features and Target Variable:**

X = player_stats_df_rec[['Y/R', 'Y/Tgt', 'R/G', 'TD', 'Fmb']]
y = player_stats_df_rec['Points']  # Assuming 'Points' column exists

The script selects features related to player performance (e.g., yards per reception, touchdowns) and uses the Points column as the target variable.

**Splitting the Data into Training and Test Sets:**

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

The data is split into 80% training and 20% test sets to ensure the model can be evaluated on unseen data. The random_state ensures reproducibility.

**Building and Training the Linear Regression Model:**

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

The script uses scikit-learn’s LinearRegression model to learn a relationship between the selected features and the points scored.

**Making Predictions and Evaluating the Model:**

y_pred = lr_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")

The model makes predictions on the test set, and the performance is evaluated using Mean Squared Error (MSE), a common regression metric that quantifies the average squared difference between actual and predicted values.

**How to Run**

Ensure your dataset includes a column labeled Points for the target variable.

**Run the script:**

python point_estimates.py

This script is useful for predicting the points a player might score based on their performance metrics. It can be a valuable tool in fantasy football for estimating player value.

### Next Steps
Fine-tune the model by adding more features or using more sophisticated regression techniques like Ridge or Lasso regression.

Analyze the model's predictions and adjust hyperparameters to improve performance.
