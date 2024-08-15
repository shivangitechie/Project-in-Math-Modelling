# **README for scrape_glossary.py**

## **Overview**

This script scrapes American football terms and their definitions from a Wikipedia page and saves them to a text file. It is designed to extract and organize glossary terms for easy reference.

### **Requirements**

Python 3.x

Requests

BeautifulSoup4

### **How to Use**

**Install Required Libraries:**

Ensure that you have the following Python libraries installed. Install them using pip if they are not already installed:

*pip install requests beautifulsoup4*

### **Running the Script:**

Execute the script to fetch and save the glossary terms:

*python scrape_glossary.py*

### **Output:**

The script retrieves the glossary terms from the Wikipedia page.

It saves the terms and their definitions to a text file named american_football_glossary.txt in the current directory.

### **File Structure:**

*scrape_glossary.py*: The main script file.

*american_football_glossary.txt*: The output text file containing the glossary terms and definitions.

### **Customization:**

You can update the url variable if you want to scrape a different Wikipedia page or glossary.

If needed, modify the headers dictionary to match the User-Agent for different scraping requirements.

### **Error Handling:**

The script checks if the request was successful and handles cases where the page could not be retrieved.

Any issues are reported with an error message indicating the status code.
