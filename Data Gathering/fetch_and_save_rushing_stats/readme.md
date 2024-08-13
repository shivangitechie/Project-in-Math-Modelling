**README for fetch_and_save_rushing_stats.py**

**Overview**

This script fetches NFL player rushing statistics for the year 2023 from Pro Football Reference and saves the data into a CSV file named player_stats_rush.csv. The data includes player-specific rushing metrics such as attempts, yards, touchdowns, and more.

**Requirements**

Python 3.x

Pandas library

**How to Use**

**Install required libraries:**

Ensure you have the Pandas library installed. You can install it using pip:

pip install pandas

**Running the script:**

To execute the script, run the following command in your Python environment:

python fetch_and_save_rushing_stats.py

**Output:**

The script fetches player rushing statistics for the 2023 NFL season from the specified URL.

It processes the first table found on the webpage as the rushing statistics table.

The data is saved into a CSV file named player_stats_rush.csv in the same directory as the script.

**Customization:**

If you need to fetch data for a different year or from a different source, update the url_rush variable accordingly.

**Files**

fetch_and_save_rushing_stats.py: The main script file.

player_stats_rush.csv: The output CSV file containing the fetched rushing statistics.
