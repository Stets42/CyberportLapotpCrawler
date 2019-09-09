from PageLinkExtractor import PageLinkExtractor
import requests
from bs4 import BeautifulSoup
from UrlProvider import UrlProvider

request = requests.get("https://www.cyberport.de/notebook-und-tablet/notebooks.html")
page = BeautifulSoup(request.text, "html.parser")


def get_total_page_count():
    numbers = []
    for item in page.select(".paging"):
        numbers.append(item.text)

    a = numbers[0].split('\n')
    return a[20]


url_provider = UrlProvider(get_total_page_count())
urls = url_provider.url_all_pages("descending", 1, 5)
print(urls)
