from PageLinkExtractor import PageLinkExtractor
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

link_extractor = PageLinkExtractor()
for link in link_extractor.extract_links("https://www.cyberport.de/notebook-und-tablet/notebooks.html"):
    print(link)

request = requests.get("https://www.cyberport.de/notebook-und-tablet/notebooks.html")
page = BeautifulSoup(request.text, "html.parser")


def get_total_page_count():
    numbers = []
    for item in page.select(".paging"):
        numbers.append(item.text)

    a = numbers[0].split('\n')
    return a[20]