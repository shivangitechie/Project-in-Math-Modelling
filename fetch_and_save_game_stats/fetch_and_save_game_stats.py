import requests
import pandas as pd

# Example of fetching data from Pro Football Reference
url_team_stats = 'https://www.pro-football-reference.com/years/2023/games.htm'
tables = pd.read_html(url_team_stats)

# Assuming the first table is the game stats table
games_df = tables[0]

# Display the first few rows
print(games_df.head())

games_df.to_csv("games_stats.csv")
