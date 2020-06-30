import logging
import sys
from .factory import set_up

logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

if sys.gettrace():  # check if any debugger involved
    _logger.setLevel(logging.DEBUG)

set_up()
