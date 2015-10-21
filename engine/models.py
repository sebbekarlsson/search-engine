from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine, TIMESTAMP
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///database.sqlite', connect_args={'check_same_thread':False})

def new_session():
    Session = sessionmaker()
    Session.configure(bind=engine)

    sess = Session()

    return sess

sess = new_session()

class Data():
    created = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    token = Column(String)

class Post(Base, Data):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    type = Column(String)

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
    