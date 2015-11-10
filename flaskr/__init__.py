import yaml


with open("flaskr/config.yml", 'r') as stream:
    config = yaml.load(stream)