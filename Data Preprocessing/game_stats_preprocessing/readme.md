**README for game_stats_preprocessing.py**

**Overview**

This script preprocesses NFL game data by performing various data cleaning and transformation steps. It processes a DataFrame containing game statistics, including dropping irrelevant columns, renaming columns, converting data types, and handling missing values.

**Requirements**

Python 3.x

pandas (for data manipulation)

**Installation**

**Install Required Libraries:**

Ensure you have pandas installed. You can install it using pip:

*pip install pandas*

Script Details

**Drop Columns:**

Objective: Remove unnecessary columns from the DataFrame.

Implementation:

games_df.drop(columns=["Time","Unnamed: 5", "Unnamed: 7"], inplace=True)

**Rename Columns:**

Objective: Rename columns for clarity and consistency.

Implementation:

games_df.rename(columns={
    'Pts': 'WinnerPts',
    'Pts.1': 'LoserPts'
}, inplace=True)

**Convert Date Column:**

Objective: Convert the 'Date' column to datetime format, handling errors and missing values.

Implementation:

games_df['Date'] = pd.to_datetime(games_df['Date'], errors='coerce', format='%Y-%m-%d')

games_df = games_df.dropna(subset=['Date'])

**Replace Week Values:**

Objective: Replace specific non-numeric values in the 'Week' column with numeric codes.

Implementation:

replacement_dict = {
    'WildCard': 19,
    'Division': 20,
    'ConfChamp': 21,
    'SuperBowl': 22
}

games_df['Week'] = games_df['Week'].replace(replacement_dict)

**Convert and Clean Week Column:**

Objective: Convert the 'Week' column to numeric, fill missing values, and change to integer type.

Implementation:

games_df['Week'] = pd.to_numeric(games_df['Week'], errors='coerce')

games_df['Week'].fillna(0, inplace=True)

games_df['Week'] = games_df['Week'].astype(int)

**Convert Numeric Columns:**

Objective: Convert relevant columns to numeric types and handle errors.

Implementation:

games_df['WinnerPts'] = pd.to_numeric(games_df['WinnerPts'], errors='coerce')

games_df['LoserPts'] = pd.to_numeric(games_df['LoserPts'], errors='coerce')

games_df['YdsW'] = pd.to_numeric(games_df['YdsW'], errors='coerce')

games_df['TOW'] = pd.to_numeric(games_df['TOW'], errors='coerce')

games_df['YdsL'] = pd.to_numeric(games_df['YdsL'], errors='coerce')

games_df['TOL'] = pd.to_numeric(games_df['TOL'], errors='coerce')

**Handle Missing Values:**


Objective: Fill missing values in specific columns with default values.

Implementation:

games_df.fillna({'WinnerPts': 0, 'LoserPts': 0, 'YdsW': 0, 'TOW': 0, 'YdsL': 0, 'TOL': 0}, inplace=True)

**Verification:**

Objective: Print data types and preview the DataFrame to ensure transformations are correct.

Implementation:

print(games_df.dtypes)

games_df.head()

**Note**: Ensure the games_df DataFrame is loaded or defined before running this script.
