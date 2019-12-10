from . import WordPressCrawler


class Crawler(WordPressCrawler):
    def __init__(self):
        super(Crawler, self).__init__()
        self.soup = None
        self.path = "data/newsmada/newsmada"
        self.crawl_url_pattern = 'https://www.newsmada.com/rubriques/faits-divers/page/%d/'
        self.link_regex = r"(https:\/\/www.newsmada.com\/[0-9]+\/[0-9]+\/[0-9]+\/[a-zA-Z0-9/-]+)\""

        self.listfile_name = "newsmada-pagelist.txt"

    def find_title(self):
        return self.soup.find('title').text

    def iterate_text(self):
        return self.soup.find_all('p')

