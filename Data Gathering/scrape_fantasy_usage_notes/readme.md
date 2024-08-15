# **README for scrape_fantasy_usage_notes.py**

## **Overview**

This script scrapes weekly fantasy football usage notes from FFToday and saves them to a single text file. It processes articles for each week of the 2023 season, combining them into one comprehensive file.

### **Requirements**

Python 3.x

Requests

BeautifulSoup4

### **How to Use**

**Install Required Libraries:**

Ensure that you have the following Python libraries installed. Install them using pip if they are not already installed:

*pip install requests beautifulsoup4*

**Running the Script:**

Execute the script to fetch and save the usage notes:

*python scrape_fantasy_usage_notes.py*

### **Output:**

The script retrieves weekly fantasy football usage notes from the FFToday website.

It saves the notes to a text file named all_weeks_usage_notes.txt within the fantasy_usage_notes_2023 directory.

### **File Structure:**

*scrape_fantasy_usage_notes.py*: The main script file.

*fantasy_usage_notes_2023/*: Directory containing the output file.

*fantasy_usage_notes_2023/all_weeks_usage_notes.txt*: The output text file containing all weekly articles.

### **Customization:**

Modify the base_url if the URL structure changes or if you need to scrape a different source.

Update the weeks range if you want to adjust the range of weeks processed.

### **Error Handling:**

The script includes basic error handling for network issues.

It logs errors if any weekly article fails to be retrieved.

### **Additional Information:**

The script appends each week’s article to the combined file and separates them with a line of equal signs for readability.

After processing, it prints the content of the combined file to the console for verification.
