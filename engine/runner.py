from engine.spider import Spider
from engine.spiderhelper import SpiderHelper
from .sqldumpster import SQLDumpster
from .models import sess, Post
from .config import config
import time


config = config

dumpster = SQLDumpster()
dumpster.start()
helper = SpiderHelper()
threads = []


def run():
    while True:
        if len(threads) < int(config['spider']['size']):
            urls = helper.get_urls(config['spider']['size'])

            for url in urls:
                thread = Spider(name='Spiderman', url=url, dumpster=dumpster)
                thread.start()
                threads.append(thread)

                print(url)
        else:
            del threads[:]
            

def start():
    del threads[:]
    run()

