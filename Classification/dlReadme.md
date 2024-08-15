# Player Performance Classification Model

## Overview

This script builds and trains a deep learning model to classify player performance labels using selected statistical features. The model is designed to predict whether a player is likely to "Boom", "Bust", "Play meaningful minutes", or "Play with injury".

File: classification_model.py

**Dependencies**

Python 3.x

Pandas

Scikit-learn

TensorFlow (Keras)

**Installation**

Before running the script, ensure you have the required libraries installed:

pip install pandas scikit-learn tensorflow

**Input Data**

The script uses the labeled player statistics dataset generated in the previous script (labeling.py), which should have columns like:

**Y/R**: Yards per Reception.

**Y/Tgt**: Yards per Target.

**R/G**: Receptions per Game.

**TD**: Touchdowns.

**Fmb**: Fumbles.

**label**: Player performance label.

**Code Explanation**

**Feature and Label Selection:**

X = player_stats_df_rec[['Y/R', 'Y/Tgt', 'R/G', 'TD', 'Fmb']]

y = player_stats_df_rec['label']

The script selects relevant statistical features (Y/R, Y/Tgt, R/G, TD, Fmb) to use as inputs (X). The target variable (y) is the label column generated from the first script.


**Label Encoding:**

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

The labels are encoded into numeric values using LabelEncoder since the deep learning model requires numeric inputs.


**Data Splitting:**

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

The dataset is split into training (80%) and testing (20%) sets using train_test_split.

**Model Architecture:**

model = Sequential([

    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    
    Dropout(0.3),
    
    Dense(32, activation='relu'),
    
    Dropout(0.3),
    
    Dense(16, activation='relu'),
    
    Dropout(0.3),
    
    Dense(4, activation='softmax')  # 4 output classes
    
])

The deep learning model is a sequential neural network with:

Input layer: 64 neurons with ReLU activation.

Hidden layers: Two layers with 32 and 16 neurons, both with ReLU activation.

Dropout layers: Added after each dense layer to reduce overfitting (0.3 dropout rate).

Output layer: 4 neurons with softmax activation, corresponding to the four performance labels.

**Model Compilation:**

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

The model is compiled with:

Optimizer: Adam optimizer.

Loss Function: Sparse categorical cross-entropy (suitable for integer-labeled multi-class classification).

Metrics: Accuracy.

**Model Training:**

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

The model is trained for 50 epochs with a batch size of 32. A validation split of 20% is used for monitoring performance during training.

**Model Evaluation:**

test_loss, test_accuracy = model.evaluate(X_test, y_test)

print(f"Test Accuracy: {test_accuracy:.2f}")

The model is evaluated on the test set, and the test accuracy is printed.

**Output**

The script trains a classification model and evaluates it on unseen test data. The final test accuracy is displayed, which indicates how well the model performs in predicting player performance categories.

**How to Run**

Ensure you have run the labeling.py script and have a labeled dataset ready.

Place the dataset in the same directory as the script.

**Run the script:**

python classification_model.py

**Next Steps**

The model's performance can be further improved by tuning hyperparameters, experimenting with more complex architectures, or using advanced techniques like transfer learning.
