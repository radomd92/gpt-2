import sys
from crawler.lagazette import Crawler as lagazette
from crawler.aoraha import Crawler as aoraha
from crawler.delire import Crawler as delire
from crawler.midi import Crawler as midi
from crawler.newsmada import Crawler as newsmada

if __name__ == '__main__':
	for journal in [aoraha, delire, midi, newsmada, lagazette]:
		spider_class = journal
		spider_obj = spider_class()
		spider_obj.fetch_today()
		spider_obj.parse()
