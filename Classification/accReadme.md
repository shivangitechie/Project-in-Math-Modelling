# Model Evaluation and Visualization

## Overview

This script evaluates the performance of the trained deep learning model on the test dataset and visualizes the accuracy using a histogram.

File: model_evaluation.py

**Dependencies**

Python 3.x

Matplotlib

Scikit-learn

NumPy (implicitly required)

**Installation**

Before running the script, ensure you have the required libraries installed:

pip install matplotlib scikit-learn numpy

**Code Explanation**

Prediction on Test Data:

y_pred = model.predict(X_test)

y_pred_labels = np.argmax(y_pred, axis=1)

The trained model is used to predict the labels for the test dataset (X_test). Since the output layer uses softmax, the predictions are probabilities across the four classes. The np.argmax() function is used to select the class with the highest probability for each prediction.

**Calculate Accuracy:**

accuracy = accuracy_score(y_test, y_pred_labels)

The accuracy_score() function from scikit-learn is used to calculate the accuracy of the model's predictions by comparing the predicted labels (y_pred_labels) with the true labels (y_test).


**Plotting a Histogram:**

plt.hist([test_accuracy], bins=10, color='blue', alpha=0.7, label='Accuracy')

plt.title('Histogram of Model Accuracy')

plt.xlabel('Accuracy')

plt.ylabel('Frequency')

plt.legend()

plt.show()

The accuracy score is visualized using a histogram:

bins=10: The range of accuracy scores is divided into 10 intervals.

color='blue' and alpha=0.7: Customize the appearance of the histogram bars.

The plot is labeled with a title, axis labels, and a legend.

**Displaying the Plot:**

The plt.show() function is used to display the histogram.

**Output**

The script generates a histogram that visualizes the distribution of the model's accuracy, providing an intuitive understanding of its performance.

**How to Run**

Ensure you have run the classification_model.py script and trained the model.

**Run the script:**

python model_evaluation.py

**Next Steps**

You can further extend the evaluation by including metrics like precision, recall, and F1-score, or by plotting confusion matrices.
