from . import WordPressCrawler


class Crawler(WordPressCrawler):
    def __init__(self):
        super(Crawler, self).__init__()
        self.soup = None
        self.path = "data/MidiMadagasikara/MidiMadagasikara"
        self.crawl_url_pattern = "http://www.midi-madagasikara.mg/category/faits-divers/page/%d/"
        self.link_regex = r"(http:\/\/www\.midi\-madagasikara\.mg\/faits-divers\/[0-9]+\/[0-9]+\/[0-9]+\/[a-zA-Z0-9/-]+)\""

        self.listfile_name = "midi-madagasikara-pagelist.txt"

    def find_title(self):
        return self.soup.find('title').text

    def iterate_text(self):
        return self.soup.find_all('p')
