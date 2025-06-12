#!/usr/bin/env python3.13
import logging

from jmullan_cmd import cmd
from jmullan_logging import easy_logging

logger = logging.getLogger(__name__)


class Main(cmd.Main):
    """Do a thing"""
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        if self.args.verbose:
            easy_logging.easy_initialize_logging("DEBUG")
        else:
            easy_logging.easy_initialize_logging()


    def main(self):
        super().main()
        logger.debug(self.args)


def main():
    Main().main()


if __name__ == "__main__":
    main()
