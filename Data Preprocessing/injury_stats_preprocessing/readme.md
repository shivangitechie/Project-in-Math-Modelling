# **README for injury_stats_preprocessing.py**

## **Overview**

This script preprocesses NFL injury data, focusing on standardizing column names, handling missing values, and cleaning text and date information for consistency and usability.

### **Functionality**

**Standardize Column Names:**

Converts column names to lowercase and replaces spaces with underscores to ensure consistency and ease of access.

**Handle Missing Values:**

Fills missing values in the 'injury' column with 'None' and replaces empty 'game_status' entries with 'Not Available'.

**Clean Text Data:**

Converts all text data to lowercase and removes leading/trailing whitespace to maintain uniformity.

**Handle Special Cases:**

Removes suffixes (e.g., "st", "nd", "rd", "th") from date strings to correct date formatting issues.

Ensures that dates are properly formatted before conversion to datetime, addressing potential formatting errors.

**Convert Dates:**

Converts cleaned date strings to datetime objects using a specific format, assuming all dates follow the pattern '%A, %B %d'.

**Error Handling:**

Catches and reports errors during datetime conversion, including problematic entries for manual inspection if necessary.

### **Requirements**

Python 3.x

pandas library

### **Installation**

Install the required library using pip:

*pip install pandas*

### **Usage**

Load the injuries_df DataFrame with NFL injury data before running this script. The script will preprocess the data, standardizing and cleaning it for further analysis.
