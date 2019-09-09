from urllib.parse import urljoin


class UrlProvider:
    def __init__(self, max_page_count):
        self.max_page_count = max_page_count

    def create_start_url(self, sort_type):
        if sort_type == "ascending":
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=price_asc&page="

        elif sort_type == "descending":
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=price_desc&page="

        elif sort_type == "topseller":
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=topseller&page="

        else:
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=popularity&page="

    def url_all_pages(self, sort_type, start, stop):
        url_list = []
        for i in range(start, stop):
            url_list.append(self.create_start_url(sort_type) + str(i))
        return url_list

    def build_article_url(self, reference_url):
        return urljoin("https://cyberport.de", reference_url)