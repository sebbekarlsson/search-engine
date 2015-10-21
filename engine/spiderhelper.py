from .models import new_session, Post
from .config import get_config


class SpiderHelper(object):

    def get_urls(self, limit, fallback_url=get_config()['spider']['fallback_url']):

        session = new_session()

        try:
            posts = session.query(Post).filter(Post.type=='url').limit(limit)
        except:
            return [fallback_url]

        if posts is None:
            return [fallback_url]

        count = posts.count()

        if count == 0:
            return [fallback_url]
    

        urls = []
        for i, post in enumerate(posts):

            # Printing a nice little percentage view to the console
            percentage = (i/count) * 100
            print('Fetching URLs: {p}%'.format(p=percentage), end="\r")

            urls.append(post.title)
            session.query(Post).filter(Post.title==post.title).delete()
            session.commit()

        session.close()

        return urls
