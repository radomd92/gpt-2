import sys
from crawler.lagazette import Crawler as lagazette
from crawler.aoraha import Crawler as aoraha
from crawler.midi import Crawler as midi

spider_class = lagazette
spider_obj = spider_class()
# spider_obj.list_pages(300)
# spider_obj.parse()


import glob, os

for file in glob.glob('data/MidiMadagasikara/*', recursive=True):
    hit = 0
    j = file.split('.')
    if len(j) < 3:
        continue
    for char in 'cquwx':
        if char in j[-2]:
            hit += 3
    for char in 'ampntsy':
        if char in j[-2]:
            hit -= 2
    if hit > -5:
        print (file, hit)
        os.remove(file)

