from bs4 import BeautifulSoup
import time

# Function to extract injury data from a given URL
def extract_injury_data(url, week):
    print(f'Processing {url}')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all date sections
    date_sections = soup.find_all('h2', class_='d3-o-section-title')

    for date_section in date_sections:
        match_date = date_section.text.strip()

        # Find all match sections under the date section
        match_sections = date_section.find_all_next('a', class_='nfl-c-matchup-strip__team-fullname', limit=2)

        for i in range(0, len(match_sections), 2):
            team1_name = match_sections[i].text.strip()
            team2_name = match_sections[i+1].text.strip()
            match_title = f"{team1_name} vs {team2_name}"

            # Extract team 1 injury data
            team1_injuries = match_sections[i].find_next('span', text=team1_name).find_next('table')
            extract_team_injury_data(week, match_title, match_date, team1_name, team1_injuries)

            # Extract team 2 injury data
            team2_injuries = match_sections[i+1].find_next('span', text=team2_name).find_next('table')
            extract_team_injury_data(week, match_title, match_date, team2_name, team2_injuries)

def extract_team_injury_data(week, match_title, match_date, team_name, injury_table):
    if injury_table:
        rows = injury_table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cols = row.find_all('td')
            player = cols[0].text.strip()
            position = cols[1].text.strip()
            injury = cols[2].text.strip()
            practice_status = cols[3].text.strip()
            game_status = cols[4].text.strip()

            # Append data to the list
            all_data.append([week, match_title, match_date, team_name, player, position, injury, practice_status, game_status])

# Base URLs for regular season and wildcard week
base_url_regular = 'https://www.nfl.com/injuries/league/2023/REG'
base_url_post = 'https://www.nfl.com/injuries/league/2023/POST1'

# Initialize lists to store the extracted data
all_data = []

# Process regular season weeks 1 to 18
for week in range(1, 19):
    url = f'{base_url_regular}{week}'
    extract_injury_data(url, f'Week {week}')
    time.sleep(1)  # To avoid overwhelming the server

# Process wildcard week
extract_injury_data(base_url_post, 'Wildcard')

# Create a DataFrame from the data
columns = ['Week', 'Match Title', 'Match Date', 'Team', 'Player', 'Position', 'Injury', 'Practice Status', 'Game Status']
df_injuries = pd.DataFrame(all_data, columns=columns)

# Save to CSV
df_injuries.to_csv('nfl_injuries_2023_full.csv', index=False)
