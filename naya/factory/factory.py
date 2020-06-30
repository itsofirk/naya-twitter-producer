from .arguments import _parser
from .config import _config


def get_args():
    return _parser.parse_args()


def set_up():
    args = get_args()
    for f in args.config:
        _config.read(f)
