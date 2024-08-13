import requests
from bs4 import BeautifulSoup
import os

# Base URL for the weekly articles
base_url = "https://fftoday.com/articles/krueger/23_usage_notes_wk"

# Create a directory to save the file (if needed)
os.makedirs('fantasy_usage_notes_2023', exist_ok=True)

# Define the file path for the single combined file
combined_file_path = 'fantasy_usage_notes_2023/all_weeks_usage_notes.txt'

# Define the range of weeks
weeks = range(1, 19)

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Process each week's article
for week in weeks:
    url = f"{base_url}{week}.html"
    print(f"\nFetching Week {week} article: {url}")

    try:
        # Send a request to the article page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title
        title_tag = soup.find('title')
        title = title_tag.get_text(strip=True) if title_tag else f"Week {week} - No Title Found"

        # Extract the article content by looking for <h3> and <p> tags
        article_text = ''
        sections = soup.find_all(['h3', 'p'])

        for section in sections:
            article_text += section.get_text(strip=True) + '\n\n'  # Add some spacing for readability

        # Append the article content to the combined file
        with open(combined_file_path, 'a', encoding='utf-8') as file:
            file.write(f"Title: {title}\n")
            file.write(f"URL: {url}\n\n")
            file.write("Article Content:\n")
            file.write(article_text)
            file.write("\n" + "="*80 + "\n\n")  # Separator between weeks

        print(f"Saved: Week {week}")

    except requests.RequestException as e:
        print(f"Failed to retrieve article for Week {week}. Error: {e}")

print("\nAll articles processed.")

# Define the file path to the combined file
combined_file_path = 'fantasy_usage_notes_2023/all_weeks_usage_notes.txt'

# Check if the file exists
if os.path.exists(combined_file_path):
    # Open and read the file
    with open(combined_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Print the content of the file
    print(file_content)
else:
    print(f"The file {combined_file_path} does not exist.")
