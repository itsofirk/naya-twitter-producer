from .arguments import _parser
from .config import _config


def set_up():
    args = _parser.parse_args()
    for f in args.config:
        _config.read(f)
