**README for fetch_and_save_receiving_stats.py**

**Overview**

This script fetches NFL player receiving statistics for the year 2023 from Pro Football Reference and saves the data into a CSV file named player_stats_rec.csv. The dataset includes player-specific receiving metrics such as targets, receptions, yards, touchdowns, and more.

**Requirements**

Python 3.x

Pandas library

**How to Use**

**Install required libraries:**

Make sure you have the Pandas library installed. You can install it using pip:

pip install pandas

**Running the script:**

Execute the script by running the following command in your Python environment:

*python fetch_and_save_receiving_stats.py*

**Output:**

The script fetches player receiving statistics for the 2023 NFL season from the specified URL.

It processes the first table found on the webpage as the receiving statistics table.

The data is saved into a CSV file named player_stats_rec.csv in the same directory as the script.

**Customization:**

To fetch data for a different year or from a different source, update the url_rec variable with the appropriate URL.

**Files**

*fetch_and_save_receiving_stats.py: The main script file.*

*player_stats_rec.csv: The output CSV file containing the fetched receiving statistics.*
