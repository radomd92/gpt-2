import requests
import re
from html.parser import HTMLParser
import bs4

proxies = {
 "http": "http://jenkinzz:asdlkajemnf@hq-proxynossl:80",
 "https": "http://jenkinzz:asdlkajemsdsdfnf@hq-proxynossl:80",
}


class MLStripper(HTMLParser):
    def __init__(self):
        super(MLStripper, self).__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def get_all_pages():
    ids = open('page_ids.txt', 'w')
    for page_number in range(1,245):
        print('-'*20 + str(page_number) + '-'*20)
        page = requests.get("http://www.lagazette-dgi.com/?cat=5&paged=%d" % page_number, stream=True, proxies=proxies)
        for link in re.findall(r"(http://www\.lagazette-dgi\.com/\?p=[0-9]+)", page.text):
            ids.write(link)
            ids.write('\n')
            print(link)


def parse_articles():
    count = 0
    with open('page_ids.txt', 'r') as f:
        for url in f.readlines():
            print('-'*20 + str(url.strip('\n')) + '-'*20)
            page = requests.get(url, stream=True, proxies=proxies)
            soup = bs4.BeautifulSoup(page.text)
            outstr = bytes()
            for p in soup.find_all('p'):
                txt = strip_tags(p.text)                    nv
                outstr += txt.encode('utf8')

            print(type(outstr))
            with open('dataset/gazetinnynosy/%d.txt' % count, 'wb') as outf:
                outf.write(outstr)
                count += 1


parse_articles()