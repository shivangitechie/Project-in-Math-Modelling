import pandas as pd

# Load player stats
player_stats_df_rec = pd.read_csv('player_stats_df_rec.csv')

# Define labeling function
def label_player(row):
    if row['Succ%'] >= 50 and row['TD'] > 5:
        return 'Boom'
    elif row['Succ%'] < 30 and row['TD'] < 2:
        return 'Bust'
    elif row['Succ%'] >= 30 and row['Succ%'] < 50 and row['TD'] >= 2 and row['TD'] <= 5:
        return 'Play meaningful minutes'
    else:
        return 'Play with injury'

# Apply labeling to the dataset
player_stats_df_rec['label'] = player_stats_df_rec.apply(label_player, axis=1)

# Display labeled data
print(player_stats_df_rec[['Player', 'Succ%', 'TD', 'label']].head())
