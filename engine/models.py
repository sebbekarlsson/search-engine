from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine, TIMESTAMP
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:cdn@localhost/search")

def new_session():
    Session = sessionmaker()
    Session.configure(bind=engine)

    sess = Session()

    return sess

sess = new_session()

class Data():
    created = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    token = Column(String(160))

class Post(Base, Data):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(160))
    content = Column(String(1024))
    type = Column(String(160))

def save_url(url):
    old_post = sess.query(Post).filter(Post.title==url).first()

    if old_post is None:
        post = Post()
        post.title = url
        post.content = post.title
        post.type = 'url'

        sess.add(post)
        sess.commit()
        sess.flush()

def initialize_database():
    Base.metadata.create_all(engine)
    