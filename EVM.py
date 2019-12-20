# -*- coding: utf-8 -*-
# Volker Göhler 2019,2020
# orig work: https://github.com/flyingzhao/PyEVM

import logging

from EVM.cli import CLI
from EVM.magnifycolor import MagnifyColor
from EVM.magnifymotion import MagnifyMotion
from EVM.mode import Mode

if __name__ == "__main__":
    cli = CLI()

    logging.basicConfig(level=cli.get_log_level)

    # create magnification correct Object
    if cli.get_mode == Mode.COLOR:
        print("Starting Magnification in Color Mode")
        Magnify = MagnifyColor
    elif cli.get_mode == Mode.MOTION:
        print("Starting Magnification in Motion Mode")
        Magnify = MagnifyMotion
    else:
        raise NotImplementedError("Unknown Mode")

    Magnify(cli.get_file.name, low=cli.get_low, high=cli.get_high, levels=cli.get_levels,
            amplification=cli.get_amplification)
