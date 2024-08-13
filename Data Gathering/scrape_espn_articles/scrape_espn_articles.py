import os
import requests
from bs4 import BeautifulSoup

# List of article URLs
urls = [
    "https://www.espn.com/nfl/draft2023/insider/story/_/id/35564109/nfl-draft-2023-standouts-east-west-shrine-bowl-practices-10-rising-prospects-zay-flowers-dorian-thompson-robinson",
    "https://www.espn.com/nfl/story/_/id/35564912/super-bowl-57-eagles-defense-haason-reddick",
    "https://www.espn.com/nfl/story/_/id/35565338/what-expect-sean-payton-deal-saints-broncos",
    "https://www.espn.com/college-football/story/_/id/35565187/nfl-teams-line-see-better-version-hendon-hooker",
    "https://www.espn.com/nfl/story/_/id/35564183/sources-texans-hire-49ers-dc-demeco-ryans-head-coach"
]

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Create directory to save the file (if needed)
os.makedirs('espn_articles_2023', exist_ok=True)

# File path for the single combined file
combined_file_path = 'espn_articles_2023/all_articles.txt'

# Process each URL
for idx, url in enumerate(urls, 1):
    print(f"Fetching article {idx}: {url}")

    try:
        # Send a request to the article page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article's title
        title_tag = soup.find('h1')
        title = title_tag.get_text().strip() if title_tag else "No Title Found"

        # Extract the article content
        article_body = soup.find_all('div', class_='article-body') or soup.find_all('article')
        article_text = ''
        for section in article_body:
            paragraphs = section.find_all('p')
            for p in paragraphs:
                article_text += p.get_text() + '\n'

        # Save the article content to the combined file
        with open(combined_file_path, 'a', encoding='utf-8') as file:
            file.write(f"Title: {title}\n")
            file.write(f"URL: {url}\n\n")
            file.write("Article Content:\n")
            file.write(article_text)
            file.write("\n" + "="*80 + "\n\n")  # Separator between articles

        print(f"Saved: {title}")

    except requests.RequestException as e:
        print(f"Failed to retrieve article at {url}. Error: {e}")

print("All articles processed.")
