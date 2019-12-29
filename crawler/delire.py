from datetime import datetime

from . import WordPressCrawler


class Crawler(WordPressCrawler):
    def __init__(self):
        super(Crawler, self).__init__()
        self.soup = None
        self.path = "data/delire/deliremadagascar"
        self.crawl_url_pattern = ''
        self.link_regex = r"(http\:\/\/www\.deliremadagascar\.com\/[a-zA-Z0-9/-]+\/)\#more"

        self.listfile_name = "deliremadagascar-pagelist.txt"

    def find_title(self):
        return self.soup.find('title').text

    def iterate_text(self):
        return self.soup.find_all('p')

    def fetch_today(self):
        today = datetime.now()
        self.crawl_url_pattern = "http://www.deliremadagascar.com/%04d/%02d" % (today.year, today.month)
        self.crawl_url_pattern += "/page/%d/"
        super(Crawler, self).list_pages(5)

    def list_pages(self, last_page_number=200):
        for year in range(2016, 2020):
            for month in range(1,13):
                self.crawl_url_pattern = "http://www.deliremadagascar.com/%04d/%02d" % (year,month)
                self.crawl_url_pattern += "/page/%d/"
                super(Crawler, self).list_pages(5)
