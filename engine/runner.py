from engine.spider import Spider
from engine.spiderhelper import SpiderHelper
from .sqldumpster import SQLDumpster
from .models import sess
from .config import config

config = config

dumpster = SQLDumpster()
dumpster.start()
helper = SpiderHelper()
spider_size = int(config['spider']['size'])
threads = []


def run():
    thread = Spider(name='Spiderman', url=helper.get_url(), dumpster=dumpster)
    thread.start()


def start():
    del threads[:]
    run()

