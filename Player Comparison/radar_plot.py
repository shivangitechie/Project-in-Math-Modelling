import matplotlib.pyplot as plt
import numpy as np

# Function to calculate Boom and Bust percentages
def calculate_boom_bust(player_stats_df, player_name):
    player_data = player_stats_df[player_stats_df['Player'] == player_name]
    if player_data.empty:
        return None, None
    total_games = len(player_data)
    boom_games = len(player_data[player_data['label'] == 'Boom'])
    bust_games = len(player_data[player_data['label'] == 'Bust'])
    boom_percentage = (boom_games / total_games) * 100
    bust_percentage = (bust_games / total_games) * 100
    return boom_percentage, bust_percentage

# Radar chart function for comparing two players
def compare_players_radar(player1, player2):
    p1_boom, p1_bust = calculate_boom_bust(player_stats_df_rec, player1)
    p2_boom, p2_bust = calculate_boom_bust(player_stats_df_rec, player2)

    if p1_boom is None or p2_boom is None:
        print("One of the players does not exist in the dataset.")
        return

    # Data for radar chart
    labels = ['Boom %', 'Bust %']
    p1_values = [p1_boom, p1_bust]
    p2_values = [p2_boom, p2_bust]

    # Complete the loop by repeating the first value
    p1_values += p1_values[:1]
    p2_values += p2_values[:1]

    # Angles for radar chart
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    # Create radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.fill(angles, p1_values, color='blue', alpha=0.25)
    ax.fill(angles, p2_values, color='red', alpha=0.25)

    ax.plot(angles, p1_values, color='blue', linewidth=2, linestyle='solid', label=player1)
    ax.plot(angles, p2_values, color='red', linewidth=2, linestyle='solid', label=player2)

    ax.set_yticklabels([])  # Hide the circular y-labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Add a legend and title
    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    ax.set_title('Player Comparison: Boom and Bust %')

    plt.show()

# Example comparison using radar chart
compare_players_radar('CeeDee Lamb', 'Tyreek Hill')
