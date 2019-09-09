import requests
from bs4 import BeautifulSoup


class PageLinkExtractor():
    def extract_links(self, url):
        r = requests.get(url)
        start_page = BeautifulSoup(r.text, "html.parser")
        links = []
        for card in start_page.select(".productWrapper .head"):
            for link in card.find_all('a', href=True):
                links.append(link.get("href"))
        return links

    def extract_names(self, url):
        r = requests.get(url)
        start_page = BeautifulSoup(r.text, "html.parser")
        names = []
        for card in start_page.select(".productTitleName"):
            names.append(card.text)
        return names
