# Drop Columns
games_df.drop(columns=["Time","Unnamed: 5", "Unnamed: 7"], inplace =True)

# Rename columns
games_df.rename(columns={
    'Pts': 'WinnerPts',
    'Pts.1': 'LoserPts'
}, inplace=True)

# Convert Date to datetime, handling errors
games_df['Date'] = pd.to_datetime(games_df['Date'], errors='coerce', format='%Y-%m-%d')
games_df = games_df.dropna(subset=['Date'])

# Replacement dictionary for specific non-numeric values
replacement_dict = {
    'WildCard': 19,
    'Division': 20,
    'ConfChamp': 21,
    'SuperBowl': 22
}

# Replace values in the 'Week' column
games_df['Week'] = games_df['Week'].replace(replacement_dict)

# Convert 'Week' column to numeric, if not already
games_df['Week'] = pd.to_numeric(games_df['Week'], errors='coerce')

# Fill any remaining NaN values in 'Week' with a default value (if needed)
games_df['Week'].fillna(0, inplace=True)

# Convert 'Week' to integer
games_df['Week'] = games_df['Week'].astype(int)

# Step 5: Convert numeric columns
games_df['WinnerPts'] = pd.to_numeric(games_df['WinnerPts'], errors='coerce')
games_df['LoserPts'] = pd.to_numeric(games_df['LoserPts'], errors='coerce')
games_df['YdsW'] = pd.to_numeric(games_df['YdsW'], errors='coerce')
games_df['TOW'] = pd.to_numeric(games_df['TOW'], errors='coerce')
games_df['YdsL'] = pd.to_numeric(games_df['YdsL'], errors='coerce')
games_df['TOL'] = pd.to_numeric(games_df['TOL'], errors='coerce')

# Step 6: Handle missing values
games_df.fillna({'WinnerPts': 0, 'LoserPts': 0, 'YdsW': 0, 'TOW': 0, 'YdsL': 0, 'TOL': 0}, inplace=True)

# Print data types and first few rows to verify changes
print(games_df.dtypes)
games_df.head()
