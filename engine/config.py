import yaml


def get_config():
    return yaml.load(open('engine/config.yml', 'r'))