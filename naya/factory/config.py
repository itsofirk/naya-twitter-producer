from configparser import ConfigParser

_config = ConfigParser()


def get_twitter_tokens():
    return dict(_config.items('twitter'))
