import logging
from tweepy import OAuthHandler, Stream
from kafka import KafkaProducer
from .listener import LoggerListener

logger = logging.getLogger(__name__)


def stream_twitter(kafka_host, kafka_topic, tracking_tag, twitter_tokens):
    logger.debug("Initializing kafka producer")
    producer = KafkaProducer(bootstrap_servers=[kafka_host])
    logger.debug("Initializing listener")
    listener = LoggerListener(producer, kafka_topic)

    auth = OAuthHandler(twitter_tokens['apikey'], twitter_tokens['apisecret'])
    auth.set_access_token(twitter_tokens['accesstoken'], twitter_tokens['accesssecret'])

    stream = Stream(auth, listener)
    if not tracking_tag.startswith('#'):
        tracking_tag = '#' + tracking_tag

    logger.info("Starting streaming")
    stream.filter(track=tracking_tag)
