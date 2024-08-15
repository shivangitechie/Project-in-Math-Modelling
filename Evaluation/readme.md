# Model Evaluation: Deep Learning vs. Linear Regression

## Overview

This script compares the performance of two models:

1. A deep learning model (for multi-class classification)

2. A linear regression model (for points prediction)

The evaluations are printed in terms of:

Accuracy for the deep learning model.

Mean Squared Error (MSE) for the linear regression model.

File: evaluations.py

### Dependencies

Python 3.x

### Code Explanation

**Deep Learning Model Evaluation:**

dl_accuracy = test_accuracy

The accuracy of the deep learning model is stored in the variable dl_accuracy. This value is taken from the model trained earlier (likely from the previous script you shared).

**Linear Regression Model Evaluation:**

lr_mse = mse

The Mean Squared Error (MSE) of the linear regression model is stored in the variable lr_mse.

**Printing the Results:**

print(f"Deep Learning Model Accuracy: {dl_accuracy:.2f}")

print(f"Linear Regression Model MSE: {lr_mse:.2f}")

The script prints the evaluation metrics for both models in a user-friendly format.

**How to Run**

Ensure the accuracy and MSE values from the deep learning and linear regression models are available (from previous scripts).

**Run the script:**

python evaluations.py

### Output

Deep Learning Model Accuracy: 0.85

Linear Regression Model MSE: 12.34

**Interpretation of Results**

Deep Learning Model Accuracy: Measures how well the classification model predicts the correct labels. Higher accuracy indicates better performance.

Linear Regression Model MSE: Measures the average squared difference between actual and predicted points. Lower MSE indicates better performance.

### Next Steps

1. Perform hyperparameter tuning on both models to improve performance.
2. Consider using additional metrics like Precision, Recall, and R-squared for a more comprehensive evaluation.
