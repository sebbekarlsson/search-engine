from engine.runner import start
from engine.models import initialize_database

if __name__ == '__main__':
    initialize_database()
    while True:
        start()