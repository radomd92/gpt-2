from . import WordPressCrawler


class Crawler(WordPressCrawler):
    def __init__(self):
        super(Crawler, self).__init__()
        self.soup = None
        self.path = "data/aoraha/aoraha"
        self.crawl_url_pattern = ''
        self.link_regex = r"(https:\/\/aoraha\.mg\/[0-9]+\/[0-9]+\/[0-9]+\/[a-zA-Z0-9/-]+)\""

        self.listfile_name = "aoraha-pagelist.txt"

    def find_title(self):
        return self.soup.find('title').text

    def iterate_text(self):
        return self.soup.find_all('p')

    def fetch_today(self):
        categories = [
            ('tranga-samihafa', 2),
            ('raharaham-pirenena', 2),
            ('sosialy', 2),
            ('faritra', 2),
            ('fanatanjahantena', 2),
            ('samihafa', 2),
        ]
        for category, n_pages in categories:
            self.crawl_url_pattern = "https://aoraha.mg/cat/" + category + "/page/%d/"
            super(Crawler, self).list_pages(n_pages)


    def list_pages(self, last_page_number=200):
        categories = [
            ('tranga-samihafa', 276),
            ('raharaham-pirenena', 238),
            ('sosialy', 227),
            ('faritra', 17),
            ('fanatanjahantena', 142),
            ('samihafa', 55),
        ]
        for category, n_pages in categories:
            self.crawl_url_pattern = "https://aoraha.mg/cat/" + category + "/page/%d/"
            super(Crawler, self).list_pages(n_pages)
