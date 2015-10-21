import threading
from urllib.request import urlopen
from urllib.parse import urljoin
from lxml import etree
from .utils import get_filename, get_dir
from .config import get_config
from .models import Post


class Spider(threading.Thread):

    def __init__ (self, name, url, dumpster):
        threading.Thread.__init__(self)
        self.name = name
        self.url = url
        self.config = get_config()
        self.dumpster = dumpster

    def run(self):
        print(self.url)

        try:
            response = urlopen(self.url)
        except:
            return False

            html = response.read()
            tree = etree.HTML(html)
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

                post = Post()
                post.title = href
                post.content = post.title
                post.type = 'url'

                self.dumpster.add(post)


            return True

                