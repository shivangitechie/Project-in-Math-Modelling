# Radar Plot for Player Comparison: Boom vs. Bust Percentages

## Overview

This script generates a radar chart to visually compare two players in terms of their "Boom" and "Bust" percentages based on the labeled data. The chart helps evaluate which player has a higher tendency to perform exceptionally well ("Boom") or poorly ("Bust").

File: radar_plot.py

### Dependencies

Python 3.x

matplotlib

numpy

pandas (required for data manipulation)

You can install the required libraries using:

pip install matplotlib numpy pandas

### Code Explanation

**Function to Calculate Boom and Bust Percentages:**

def calculate_boom_bust(player_stats_df, player_name):
    ...
    
This function calculates the percentage of games labeled as "Boom" or "Bust" for a specified player. The output is used to compare players.

**Radar Chart Function for Comparing Two Players:**

def compare_players_radar(player1, player2):
    ...
    
This function generates a radar chart for the two specified players. It retrieves their "Boom" and "Bust" percentages and then plots these metrics on a circular radar chart.

The labels on the chart include "Boom %" and "Bust %".

The players’ data is represented by two differently colored regions (e.g., blue and red), allowing for easy visual comparison.

**Usage** 

compare_players_radar('CeeDee Lamb', 'Tyreek Hill')

The script provides an example comparing the "Boom" and "Bust" percentages of two NFL players, CeeDee Lamb and Tyreek Hill.

**How to Run**

Ensure you have a dataset (player_stats_df_rec) loaded and processed with the appropriate player stats and labels.

**Run the script using:**

python radar_plot.py

The radar chart will be displayed in a new window.

### Output

The radar chart will display two regions:

Blue Region: Represents the first player (e.g., CeeDee Lamb).

Red Region: Represents the second player (e.g., Tyreek Hill).

The chart’s labels show:

Boom %: The percentage of games labeled as "Boom".

Bust %: The percentage of games labeled as "Bust".

**Interpretation of Results**

A larger "Boom %" region indicates a player is more likely to have high-performing games.

A larger "Bust %" region indicates a player is more likely to have low-performing games.

### Potential Extensions

You can expand the comparison by including additional metrics (e.g., "Play meaningful minutes" or "Play with injury").

You could modify the script to compare more than two players at once by introducing additional regions on the radar chart.
