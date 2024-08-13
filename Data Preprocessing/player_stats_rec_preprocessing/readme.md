**README for player_stats_rec_preprocessing.py**

**Overview**

This script processes NFL receiving player statistics, preparing the data for analysis or modeling. It focuses on cleaning data, handling non-numeric values, and ensuring data consistency.

**Functionality**

**Clean Player Names:**

Removes special characters and extra spaces from player names to standardize the data.

**Handle Non-Numeric Values in Percentages:**

Converts percentage columns from string format to numeric, replacing non-numeric entries with NaN and handling these appropriately.

**Convert Percentage and Integer Columns:**

Converts various percentage and integer columns to numeric values with error handling for non-numeric data.

**Handle Missing Values:**

Fills missing values in key columns with zeros to ensure completeness of the dataset.

**Verify Results:**

Prints data types and a preview of the DataFrame to confirm that the transformations have been applied correctly.

**Requirements**

Python 3.x

pandas library

**Installation**

Install the required library using pip:

*pip install pandas*

**Usage**

Ensure that the player_stats_df_rec DataFrame containing receiving player statistics is loaded before running this script. The script will preprocess the data, making it ready for further analysis.
