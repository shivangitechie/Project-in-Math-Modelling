import os
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Glossary_of_American_football_terms"

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a request to the Wikipedia page
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the glossary section (assuming it's in a div with 'mw-parser-output' class)
    glossary = soup.find_all('div', class_='mw-parser-output')[0]

    # Extract terms and definitions
    glossary_terms = []
    for term in glossary.find_all('dt'):
        # Extract the term
        term_text = term.get_text(strip=True)
        # Find the definition
        definition = term.find_next_sibling('dd')
        if definition:
            definition_text = definition.get_text(strip=True)
            glossary_terms.append((term_text, definition_text))

    # Define the file path to save the glossary
    file_path = '/content/american_football_glossary.txt'

    # Write the glossary to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Glossary of American Football Terms\n")
        file.write("="*40 + "\n\n")

        for term, definition in glossary_terms:
            file.write(f"Term: {term}\n")
            file.write(f"Definition: {definition}\n")
            file.write("\n" + "-"*40 + "\n\n")

    print(f"Glossary terms saved to {file_path}")

else:
    print(f"Failed to retrieve the Wikipedia page. Status code: {response.status_code}")
