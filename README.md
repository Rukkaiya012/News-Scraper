This project is a simple web scraper built using Python, requests, and BeautifulSoup libraries. 
The main goal is to automatically collect the top news headlines from a public news website and save them into a .txt file.
Using the requests module, the script sends a GET request to fetch the raw HTML content of the news homepage. 
Then, BeautifulSoup parses the HTML and extracts relevant text elements such as <h2>, <h3>, or <title> tags that commonly contain news headlines.
All the extracted headlines are stored in a clean and readable format inside a text file named headlines.txt.

🧰 Tools & Technologies Used:
Python
Requests (for sending HTTP requests)
BeautifulSoup (bs4) (for parsing HTML content)
VS Code or any Python IDE

⚙️ Features:
Fetches live news data directly from a website
Extracts only the text content (clean headlines)
Stores the headlines sequentially in a .txt file
Prevents duplicates and empty entries
Can be modified for any news site by adjusting URL and tags

✅ Outcome:
Demonstrates the use of Python for web scraping and automation.
Helps in understanding real-time data collection from web pages.
Produces a local .txt file with latest headlines—useful for research, news feeds, or personal projects.
