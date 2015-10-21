from .models import new_session
import threading


class SQLDumpster(threading.Thread):

    def __init__ (self):
        threading.Thread.__init__(self)
        self.queries = []
        self.session = new_session()

    def add(self, obj):
        self.queries.append(obj)

    def run(self):
        while True:
            for i, q in enumerate(self.queries):
                with self.session.no_autoflush:
                    self.session.add(q)
                    self.queries.remove(q)
            try:
                self.session.commit()
            except:
                pass
