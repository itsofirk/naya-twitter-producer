import logging
import sys

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if sys.gettrace():  # check if any debugger involved
    logger.setLevel(logging.DEBUG)
