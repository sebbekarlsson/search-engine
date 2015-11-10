import os
from setuptools import setup


setup(
    name='searchengine',
    version='1.0',
    description='Search Engine',
    author='Sebastian Robert Karlsson',
    author_email='sebbekarlsson97@gmail.com',
    url='http://www.ianertson.com/',
    install_requires=[
        'flask',
        'flask-wtf',
        'lxml',
        'PyMySQL'
    ]
)