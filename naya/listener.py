import logging

from kafka import KafkaProducer
from tweepy import StreamListener

logger = logging.getLogger(__name__)


class LoggerListener(StreamListener):
    def __init__(self, producer: KafkaProducer, topic):
        super(LoggerListener, self).__init__()
        self.producer = producer
        self.topic = topic

    def on_data(self, data):
        self.producer.send(self.topic, data.encode('utf-8'))
        logger.info(data)
        return True

    def on_error(self, status):
        logger.info(status)
