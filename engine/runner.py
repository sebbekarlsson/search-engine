from engine.spider import Spider
from engine.spiderhelper import SpiderHelper
from .sqldumpster import SQLDumpster
from .models import sess
from .config import config
import time


config = config

dumpster = SQLDumpster()
dumpster.start()
helper = SpiderHelper()
threads = []


def run():
    while True:
        urls = helper.get_urls(config['spider']['size'])

        for url in urls:
            if len(threads) < int(config['spider']['size']):
                thread = Spider(name='Spiderman', url=url, dumpster=dumpster)
                thread.start()
                threads.append(thread)
            
            print(url)

def start():
    del threads[:]
    run()

