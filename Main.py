from PageLinkExtractor import PageLinkExtractor


link_extractor = PageLinkExtractor()
for link in link_extractor.extract_links("https://www.cyberport.de/notebook-und-tablet/notebooks.html"):
    print(link)