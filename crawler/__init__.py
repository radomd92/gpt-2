import re
import time
import requests
import bs4

proxies = {
 "http": "http://jenkinzz:asdlkajemnf@hq-proxynossl:80",
 "https": "http://jenkinzz:asdlkajemsdsdfnf@hq-proxynossl:80",
}

proxies = {}


def retry_on_fail(exceptions, retries=5, time_between_retries=1):
    def _retry_on_fail(f):
        def wrapper(*args, **kwargs):
            m_retries = 0
            try:
                return f(*args, **kwargs)
            except tuple(exceptions) as e:
                if m_retries <= retries:
                    m_retries += 1
                    print('Error:', e, '%d' % m_retries)
                    time.sleep(time_between_retries)
                else:
                    raise e

        return wrapper
    return _retry_on_fail


requests.get = retry_on_fail([Exception], time_between_retries=15, retries=10)(requests.get)


class WordPressCrawler(object):
    def __init__(self):
        self.soup = None
        self.path = ""
        self.crawl_url_pattern = ""
        self.listfile_name = "pagelist"
        self.link_regex = r''

    def find_title(self):
        raise NotImplementedError()

    def iterate_text(self):
        raise NotImplementedError()

    def parse(self):
        f = open(self.listfile_name, 'r')
        count = 0
        for url in f.readlines():
            print(url)
            page = requests.get(url, proxies=proxies)
            self.soup = bs4.BeautifulSoup(page.text)
            content = bytes()
            title = self.find_title()
            content += (title.upper() + '\n\n').encode('utf-8')
            for paragraph in self.iterate_text():
                for line in paragraph.text.split('\n'):
                    if len(line) > 20:
                        txt = (line)
                        counter = 0
                        for word in txt.split():
                            if counter >= 80:
                                content += '\n'.encode('utf-8')
                                counter = 0
                            else:
                                content += (word + ' ').encode('utf-8')
                                counter += len(word)

                content += '\n\n'.encode('utf-8')

            sane_title = ''
            for char in title.lower():
                if char in 'abcdefghijklmnopqrstuvwyz0123456789-_':
                    sane_title += char
            with open(self.path + '.%s.txt' % sane_title[:min(len(sane_title), 50)], 'wb') as f:
                print(str(content))
                f.write(content)

            count += 1

    def list_pages(self, last_page_number=100):
        with open(self.listfile_name, 'a') as pagelist:
            for page_no in range(1, last_page_number):
                print('-'*20 + str(page_no) + '-'*20)
                page = requests.get(self.crawl_url_pattern % page_no, proxies=proxies)
                for link in re.findall(self.link_regex, page.text):
                    print(link)
                    pagelist.write(link)
                    pagelist.write('\n')
