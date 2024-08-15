# README for extract_injury_data.py

## **Overview**

This script scrapes NFL injury data for the 2023 season from the NFL website. It processes the injury reports for all regular-season weeks (1-18) and the Wildcard week, extracting details such as player injuries, practice status, and game status. The data is then saved into a CSV file named nfl_injuries_2023_full.csv.

### **Requirements**

Python 3.x

BeautifulSoup4

Requests

Pandas

### **How to Use**

**Install Required Libraries:**

Ensure that the following Python libraries are installed. You can install them using pip:

*pip install beautifulsoup4 requests pandas*

**Running the Script:**

Execute the script to scrape and save the NFL injury data:

*python extract_injury_data.py*

### **Output:**

The script scrapes injury data for each week in the NFL 2023 season.

The extracted data includes week number, match title, match date, team name, player name, position, injury, practice status, and game status.

The data is saved to a CSV file named *nfl_injuries_2023_full.csv*.

### **Customization:**

To scrape injury data for different weeks or a different season, modify the base_url_regular and base_url_post variables accordingly.

### **Error Handling:**

The script includes a time.sleep(1) command between requests to avoid overwhelming the server. Adjust this delay if necessary.

### **Files**

*extract_injury_data.py*: The main script file.

*nfl_injuries_2023_full.csv*: The output CSV file containing the scraped injury data.
