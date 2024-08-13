# Step 1: Standardize column names
injuries_df.columns = injuries_df.columns.str.lower().str.replace(" ", "_")

# Step 2: Handle missing values
# Fill missing 'Injury' and 'Game Status' with 'None' or appropriate label
injuries_df['injury'].fillna('None', inplace=True)
injuries_df['game_status'].replace('', 'Not Available', inplace=True)

# Step 3: Clean text data
# Convert all string data to lowercase and remove leading/trailing whitespace
for col in ['week', 'match_title', 'match_date', 'team', 'player', 'position', 'injury', 'practice_status', 'game_status']:
    injuries_df[col] = injuries_df[col].str.lower().str.strip()

# Step 4: Handle special cases
# Correctly remove suffixes like "th" from the dates
injuries_df['match_date'] = injuries_df['match_date'].str.replace(r'(\d+)(st|nd|rd|th)', r'\1', regex=True)

# Ensure all date strings are correctly formatted before conversion
# Example fix: Assume dates are always the same and correct if needed
# Note: If the issue persists, you may need to manually inspect or handle edge cases

# Remove any potential leading or trailing characters from the match_date
injuries_df['match_date'] = injuries_df['match_date'].str.strip()

# Convert to datetime, assuming all dates are in the format '%A, %B %d'
# Since the dates are all "THURSDAY, SEPTEMBER 7", convert them directly
try:
    injuries_df['match_date'] = pd.to_datetime(injuries_df['match_date'], format='%A, %B %d')
except ValueError as e:
    print(f"Error during datetime conversion: {e}")
    # Print out problematic date entries
    print(injuries_df['match_date'])

# Show the cleaned DataFrame
injuries_df.head()
