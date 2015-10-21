from engine.spider import Spider
from engine.spiderhelper import SpiderHelper
from .sqldumpster import SQLDumpster
from .models import sess
from .config import get_config


spider_size = int(get_config()['spider']['size'])

helper = SpiderHelper()
dumpster = SQLDumpster()
dumpster.start()
threads = []

def start():

    urls = helper.get_urls(limit=spider_size)

    for num, url in zip(range(0, spider_size), urls):
        thread = Spider(name='Spiderman', url=url, dumpster=dumpster)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
