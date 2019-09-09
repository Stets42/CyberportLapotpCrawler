import requests
from bs4 import BeautifulSoup


class ArticleInfoExtractor():
    def extract_info(self, url):
        req = requests.get(url)
        page = BeautifulSoup(req.text, "html parser")
