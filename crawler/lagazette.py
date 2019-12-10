from . import WordPressCrawler


class Crawler(WordPressCrawler):
    def __init__(self):
        super(Crawler, self).__init__()
        self.soup = None
        self.path = "data/gns/gazety-nosy"
        self.crawl_url_pattern = "http://www.lagazette-dgi.com/?cat=5&paged=%s"
        self.link_regex = r"(http://www\.lagazette-dgi\.com/\?p=[0-9]+)"

        self.listfile_name = "lgdgi-list.txt"

    def find_title(self):
        return self.soup.find('h1', attrs={'style': 'margin-bottom: 0'}).text

    def iterate_text(self):
        for p in self.soup.find_all('p'):
            yield p


