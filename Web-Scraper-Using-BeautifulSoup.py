from bs4 import BeautifulSoup
import requests

def scrape_website(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))

        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.get_text())
    else:
        print(f"Failed to retrieve webpage: {url}")

if __name__ == "__main__":
    url = 'https://example.com'  # Replace with your target URL
    scrape_website(url)

