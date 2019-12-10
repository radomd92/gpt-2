import sys
from crawler.lagazette import Crawler as lagazette
from crawler.aoraha import Crawler as aoraha
from crawler.midi import Crawler as midi
from crawler.newsmada import Crawler as newsmada

spider_class = newsmada
spider_obj = spider_class()
spider_obj.list_pages(987)
# spider_obj.parse()
