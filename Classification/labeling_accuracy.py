import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Predictions on the test set
y_pred = model.predict(X_test)
y_pred_labels = np.argmax(y_pred, axis=1)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred_labels)

# Plot histogram of accuracy
plt.hist([test_accuracy], bins=10, color='blue', alpha=0.7, label='Accuracy')
plt.title('Histogram of Model Accuracy')
plt.xlabel('Accuracy')
plt.ylabel('Frequency')
plt.legend()
plt.show()
