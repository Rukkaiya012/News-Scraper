import requests
from bs4 import BeautifulSoup

# Target website (example: BBC News)
URL = 'https://www.bbc.com/news'

# Send a GET request to the website
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headline tags (h3 used by BBC, can change to h2/title if needed)
    headlines = soup.find_all(['h3', 'h2', 'title'])

    # Extract and clean headline text
    titles = []
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text and text not in titles:
            titles.append(text)

    # Save headlines to a text file
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for i, title in enumerate(titles, 1):
            file.write(f"{i}. {title}\n")

    print(f"{len(titles)} headlines saved to headlines.txt")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
