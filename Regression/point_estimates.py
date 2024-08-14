from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Use the same features but add a target (e.g., points scored)
X = player_stats_df_rec[['Y/R', 'Y/Tgt', 'R/G', 'TD', 'Fmb']]
y = player_stats_df_rec['Points']  # Assuming 'Points' column exists

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train linear regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = lr_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
