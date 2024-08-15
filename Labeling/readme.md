# Player Labeling Script
## Overview
This script labels player performance based on specific criteria using the player stats dataset. The labels provide insights into whether a player is likely to "Boom", "Bust", "Play meaningful minutes", or "Play with injury" based on their statistics.

**File**: *labeling.py*

**Dependencies**

Python 3.x

Pandas

**Installation**

Before running the script, ensure you have the required libraries installed:

pip install pandas

**Input Data**

player_stats_df_rec.csv: A CSV file containing player statistics. The key columns used for labeling are:

Player: Name of the player.

Succ%: Success percentage, which represents the effectiveness of the player’s performance.

TD: Number of touchdowns.

**Code Explanation**

**Loading the Dataset:**

player_stats_df_rec = pd.read_csv('player_stats_df_rec.csv')

The script loads player statistics from the CSV file.

**Defining the Labeling Function:**

def label_player(row):

    if row['Succ%'] >= 50 and row['TD'] > 5:
    
        return 'Boom'
        
    elif row['Succ%'] < 30 and row['TD'] < 2:
    
        return 'Bust'
        
    elif row['Succ%'] >= 30 and row['Succ%'] < 50 and row['TD'] >= 2 and row['TD'] <= 5:
    
        return 'Play meaningful minutes'
    
    else:
    
        return 'Play with injury'
        
The function label_player(row) takes a row of player data as input and labels it according to predefined criteria:

**Boom**: Players with a success percentage ≥ 50% and touchdowns > 5.

**Bust**: Players with a success percentage < 30% and touchdowns < 2.

**Play meaningful minutes**: Players with a success percentage between 30% and 50% and touchdowns between 2 and 5.

**Play with injury**: All other players.

Applying the Labeling Function:

player_stats_df_rec['label'] = player_stats_df_rec.apply(label_player, axis=1)

The labeling function is applied to each row of the dataset to generate a new label column.

**Displaying the Results:**

print(player_stats_df_rec[['Player', 'Succ%', 'TD', 'label']].head())

The labeled data is displayed, showing the player name, success percentage, touchdowns, and the assigned label.

**Output**

The script outputs a labeled dataset where each player is classified into one of four categories: "Boom", "Bust", "Play meaningful minutes", or "Play with injury". A sample of the labeled data is printed to the console.

**How to Run**

Place the player_stats_df_rec.csv file in the same directory as the script.

**Run the script:**

python labeling.py
