import requests
from bs4 import BeautifulSoup


class PageLinkExtractor():
    def extract_links(self, url):
        r = requests.get(url)
        start_page = BeautifulSoup(r.text, "html.parser")

        for card in start_page.select(".productWrapper .head"):
            for link in card.find_all('a', href=True):
                yield link.get("href")

    def extract_names(self, url):
        r = requests.get(url)
        start_page = BeautifulSoup(r.text, "html.parser")

        for card in start_page.select(".productTitleName"):
            yield card.text
