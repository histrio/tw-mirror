import sys
import logging

import coloredlogs

from tw_mirror import TWMirrorError
from tw_mirror.core import out_sync

logger = logging.getLogger("tw-mirror")


def get_parser():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="print debug messages to stderr")
    subparsers = parser.add_subparsers(required=True)
    parser_up = subparsers.add_parser("sync")
    parser_up.set_defaults(func=out_sync)
    return parser


def setup_logger(args):
    lvl = logging.DEBUG if args.debug else logging.INFO
    logger.setLevel(lvl)
    coloredlogs.install(level="DEBUG", logger=logger)


def main():
    try:
        args = get_parser().parse_args()
        setup_logger(args)
        args.func(args)
        return 0
    except TWMirrorError as err:
        logger.error("Process failed. Unable to complete due to: %s", err)
        return 1


if __name__ == "__main__":
    sys.exit(main())
