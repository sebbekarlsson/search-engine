import threading
from urllib.request import urlopen
from urllib.parse import urljoin
from lxml import etree
from .utils import get_filename, get_dir
from .models import Post, new_session
from .config import config


class Spider(threading.Thread):

    def __init__ (self, name, url, dumpster):
        threading.Thread.__init__(self)
        self.name = name
        self.url = url
        self.config = config
        self.dumpster = dumpster
        self.session = new_session()

    def run(self):
        try:
            response = urlopen(self.url)
            html = response.read()
            tree = etree.HTML(html)
        except:
            return False

        links = tree.xpath('//a')

        for link in links:
            try:
                href = link.attrib['href']
            except KeyError:
                href = self.config['spider']['fallback_url']

            if not href.startswith('http') and not href.startswith('https'):
                new_href = urljoin(self.url, href)
                if not new_href.startswith('http') and not new_href.startswith('https'):
                    href = self.config['spider']['fallback_url']
                else:
                    href = new_href

            old = None
            try:
                old = self.session.query(Post).filter(Post.title==href).first()
            except:
                self.session.close()
                return False

            if old is None:
                print(self.url)

                spider = Spider(name='Spiderman', url=href, dumpster=self.dumpster)
                spider.start()

                post = Post()
                post.title = href
                post.content = post.title
                post.type = 'url'

                self.dumpster.add(post)


        self.session.close()

        return True

                