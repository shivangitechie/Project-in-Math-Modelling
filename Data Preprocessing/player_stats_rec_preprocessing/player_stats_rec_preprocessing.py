# Clean Player Names (remove special characters and extra spaces)
player_stats_df_rec['Player'] = player_stats_df_rec['Player'].str.replace('[*+]', '', regex=True).str.strip()

# Identify and handle non-numeric values in 'Ctch%'
# Replace non-numeric entries with NaN
player_stats_df_rec['Ctch%'] = pd.to_numeric(player_stats_df_rec['Ctch%'].str.rstrip('%').replace('Ctch', pd.NA), errors='coerce')

# Convert other percentage columns
player_stats_df_rec['Succ%'] = pd.to_numeric(player_stats_df_rec['Succ%'], errors='coerce')
player_stats_df_rec['Y/R'] = pd.to_numeric(player_stats_df_rec['Y/R'], errors='coerce')
player_stats_df_rec['Y/Tgt'] = pd.to_numeric(player_stats_df_rec['Y/Tgt'], errors='coerce')
player_stats_df_rec['R/G'] = pd.to_numeric(player_stats_df_rec['R/G'], errors='coerce')
player_stats_df_rec['Y/G'] = pd.to_numeric(player_stats_df_rec['Y/G'], errors='coerce')

# Convert integer columns with error handling
player_stats_df_rec['Age'] = pd.to_numeric(player_stats_df_rec['Age'], errors='coerce')
player_stats_df_rec['G'] = pd.to_numeric(player_stats_df_rec['G'], errors='coerce')
player_stats_df_rec['GS'] = pd.to_numeric(player_stats_df_rec['GS'], errors='coerce')
player_stats_df_rec['Tgt'] = pd.to_numeric(player_stats_df_rec['Tgt'], errors='coerce')
player_stats_df_rec['Rec'] = pd.to_numeric(player_stats_df_rec['Rec'], errors='coerce')
player_stats_df_rec['Yds'] = pd.to_numeric(player_stats_df_rec['Yds'], errors='coerce')
player_stats_df_rec['TD'] = pd.to_numeric(player_stats_df_rec['TD'], errors='coerce')
player_stats_df_rec['1D'] = pd.to_numeric(player_stats_df_rec['1D'], errors='coerce')
player_stats_df_rec['Lng'] = pd.to_numeric(player_stats_df_rec['Lng'], errors='coerce')
player_stats_df_rec['Fmb'] = pd.to_numeric(player_stats_df_rec['Fmb'], errors='coerce')

# Handle NaN values (e.g., fill with 0 or drop rows with NaN)
player_stats_df_rec.fillna({
    'Age': 0, 'G': 0, 'GS': 0, 'Tgt': 0, 'Rec': 0, 'Yds': 0,
    'TD': 0, '1D': 0, 'Succ%': 0, 'Lng': 0, 'Y/R': 0, 'Y/Tgt': 0,
    'R/G': 0, 'Y/G': 0, 'Fmb': 0
}, inplace=True)

# Verify the results
print(player_stats_df_rec.dtypes)
player_stats_df_rec.head()
