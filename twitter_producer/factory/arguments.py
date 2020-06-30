import argparse

_parser = argparse.ArgumentParser()
_parser.add_argument('-c', '--config', help='.ini config file/s', nargs='+', required=True)
_parser.add_argument('--tag', help='twitter hash-tag to stream', required=True)
