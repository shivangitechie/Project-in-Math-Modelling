# Receiving Metrics
# URL for player statistics (e.g., NFL receiving leaders)
url_rec = 'https://www.pro-football-reference.com/years/2023/receiving.htm'

# Read the data into a pandas DataFrame
player_stats_df_rec = pd.read_html(url_rec, header=0)[0]


# Display the cleaned player statistics DataFrame
print(player_stats_df_rec.head())

player_stats_df_rec.to_csv("player_stats_rec.csv")
