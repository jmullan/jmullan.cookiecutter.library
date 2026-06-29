#!/usr/bin/env python3.13
"""Rhe main command-line entrypoint."""
import logging

from jmullan.cmd import cmd
from jmullan.logging import easy_logging

logger = logging.getLogger(__name__)


class Main(cmd.Main) -> None:
    """Do a thing."""
    def __init__(self):
        super().__init__()

    def setup(self) -> None:
        """Do something after parsing args but before main."""
        super().setup()
        if self.args.verbose:
            easy_logging.easy_initialize_logging("DEBUG")
        else:
            easy_logging.easy_initialize_logging()


    def main(self) -> None:
        """Do something after getting set up."""
        super().main()
        logger.debug(self.args)


def main() -> None:
    """Run the command via the command-line entrypoint."""
    Main().main()


if __name__ == "__main__":
    main()
