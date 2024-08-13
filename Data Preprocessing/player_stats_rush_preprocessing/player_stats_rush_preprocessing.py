# Clean Player Names (remove special characters and extra spaces)
player_stats_df_rush['Player'] = player_stats_df_rush['Player'].str.replace('[*+]', '', regex=True).str.strip()

# Convert columns to appropriate data types with error handling
player_stats_df_rush['Age'] = pd.to_numeric(player_stats_df_rush['Age'], errors='coerce')
player_stats_df_rush['G'] = pd.to_numeric(player_stats_df_rush['G'], errors='coerce')
player_stats_df_rush['GS'] = pd.to_numeric(player_stats_df_rush['GS'], errors='coerce')
player_stats_df_rush['Att'] = pd.to_numeric(player_stats_df_rush['Att'], errors='coerce')
player_stats_df_rush['Yds'] = pd.to_numeric(player_stats_df_rush['Yds'], errors='coerce')
player_stats_df_rush['TD'] = pd.to_numeric(player_stats_df_rush['TD'], errors='coerce')
player_stats_df_rush['1D'] = pd.to_numeric(player_stats_df_rush['1D'], errors='coerce')

# Handle NaN values (e.g., fill with 0 or drop rows with NaN)
player_stats_df_rush.fillna({'Age': 0, 'G': 0, 'GS': 0, 'Att': 0, 'Yds': 0, 'TD': 0, '1D': 0}, inplace=True)

# Verify the results
print(player_stats_df_rush.dtypes)
player_stats_df_rush.tail()
