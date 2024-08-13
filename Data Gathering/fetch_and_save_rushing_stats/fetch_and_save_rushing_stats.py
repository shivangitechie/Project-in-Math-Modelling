# Rushing Metrics

# URL for player statistics (e.g., NFL rushing leaders)
url_rush = 'https://www.pro-football-reference.com/years/2023/rushing.htm'

# Read the data into a pandas DataFrame
player_stats_df_rush = pd.read_html(url_rush, header=1)[0]

# Display the cleaned player statistics DataFrame
print(player_stats_df_rush.head())

player_stats_df_rush.to_csv("player_stats_rush.csv")
