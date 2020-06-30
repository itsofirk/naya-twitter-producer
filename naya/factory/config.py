from configparser import ConfigParser

_config = ConfigParser()


def get_twitter_tokens():
    return dict(_config.items('twitter'))


def get_kafka_host():
    return _config.get('naya', 'kafka_host')


def get_twitter_raw_topic():
    return _config.get('naya', 'twitter_raw_topic')
