# **README for player_stats_rush_preprocessing.py**

## **Overview**

This script processes NFL rushing player statistics to prepare the data for analysis or modeling. It cleans player names, converts columns to numeric types, and handles missing values.

### **Functionality**

**Clean Player Names:**

Removes special characters and extra spaces from player names to standardize the data.

**Convert Columns to Numeric:**

Converts various statistical columns to numeric types, ensuring that any non-numeric values are handled appropriately.

**Handle Missing Values:**

Fills any missing values in key columns with zeros to maintain data integrity.

**Verify Results:**

Prints data types and a preview of the DataFrame to confirm that transformations have been applied correctly.

### **Requirements**

Python 3.x

pandas library

### **Installation**

Install the required library using pip:

*pip install pandas*

### **Usage**

Ensure that the player_stats_df_rush DataFrame containing player statistics is loaded before running this script. The script will preprocess the data, making it ready for further analysis.
