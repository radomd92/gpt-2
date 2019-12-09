import re
import requests
import bs4

class GazetteGrandeIle(object):
    @staticmethod
    def parse():
        f = open('pagelist', 'r')
        count = 0
        for url in f.readlines():
            print(url)
            page = requests.get(url)
            soup = bs4.BeautifulSoup(page.text)
            content = bytes()
            #soup = soup.find('div', {'class': 'full-article'})
            title = soup.find('h1', attrs={'style': 'margin-bottom: 0'}).text
            content += (title.upper() + '\n\n').encode('utf-8')
            for paragraph in soup.find_all('p', attrs={'style': "font-weight: 400; text-align: justify;"}):
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

            with open('data/gns/gazety-nosy.%d.txt' % count, 'wb') as f:
                print(str(content))
                f.write(content)

            count += 1

    @staticmethod
    def list_pages():
        url = "http://www.lagazette-dgi.com/?cat=5&paged=%s"
        with open('pagelist', 'w') as pagelist:
            for page_no in range(1, 245):
                print('-'*20 + str(page_no) + '-'*20)
                page = requests.get(url % page_no)
                for link in re.findall(r"(http://www\.lagazette-dgi\.com/\?p=[0-9]+)", page.text):
                    print(link)
                    pagelist.write(link)
                    pagelist.write('\n')


class AoRaha(object):
    @staticmethod
    def parse():
        f = open('aoraha-pagelist', 'r')
        count = 0
        for url in f.readlines():
            print(url)
            page = requests.get(url)
            soup = bs4.BeautifulSoup(page.text)
            content = bytes()
            #soup = soup.find('div', {'class': 'full-article'})
            title = soup.find('title').text
            content += (title.upper() + '\n\n').encode('utf-8')
            for paragraph in soup.find_all('p'):
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

            with open('data/aoraha/aoraha-.%d.txt' % count, 'wb') as f:
                print(str(content))
                f.write(content)

            count += 1

    @staticmethod
    def list_pages():
        with open('aoraha-pagelist', 'w') as pagelist:
            for cat in [
                'raharaham-pirenena',
                'sosialy',
                'fanatanjahantena',
                'samihafa'
            ]:
                url = "https://aoraha.mg/cat/" + cat + "/page/%d/"
                for page_no in range(1, 200):
                    print('-'*20 + str(page_no) + '-'*20)
                    page = requests.get(url % page_no)
                    links = set()
                    for link in re.findall(r"(https:\/\/aoraha\.mg\/[0-9]+\/[0-9]+\/[0-9]+\/[a-zA-Z0-9/-]+)\"", page.text):
                        links.add(link)

                    for link in links:
                        print(link)
                        pagelist.write(link)
                        pagelist.write('\n')


class MidiMadagasikara(object):
    @staticmethod
    def parse():
        f = open('midi-madagasikara-pagelistz', 'r')
        count = 0
        for url in f.readlines():
            print(url)
            page = requests.get(url)
            soup = bs4.BeautifulSoup(page.text)
            content = bytes()
            #soup = soup.find('div', {'class': 'full-article'})
            title = soup.find('title').text
            content += (title.upper() + '\n\n').encode('utf-8')
            for paragraph in soup.find_all('p'):
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

            with open('data/MidiMadagasikara/MidiMadagasikara-.%d.txt' % count, 'wb') as f:
                print(str(content))
                f.write(content)

            count += 1

    @staticmethod
    def list_pages():
        url = "http://www.midi-madagasikara.mg/category/faits-divers/page/%d/"
        with open('midi-madagasikara-pagelistz', 'w') as pagelist:
            for page_no in range(1, 1200):
                print('-'*20 + str(page_no) + '-'*20)
                page = requests.get(url % page_no)
                links = set()
                for link in re.findall(r"(http:\/\/www\.midi\-madagasikara\.mg\/faits-divers\/[0-9]+\/[0-9]+\/[0-9]+\/[a-zA-Z0-9/-]+)\"", page.text):
                    links.add(link)

                for link in links:
                    print(link)
                    pagelist.write(link)
                    pagelist.write('\n')

#AoRaha.list_pages()
MidiMadagasikara.parse()