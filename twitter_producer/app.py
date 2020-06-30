import logging
from .logic.producer import stream_twitter
from .factory import config, get_args

logger = logging.getLogger(__name__)


def main():
    logger.info('Started')
    args = get_args()
    stream_twitter(config.get_kafka_host(), config.get_twitter_raw_topic(), args.tag, config.get_twitter_tokens())
    logger.info('Done')
