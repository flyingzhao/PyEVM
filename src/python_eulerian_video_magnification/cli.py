# -*- coding: utf-8 -*-
"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mpython_eulerian_video_magnification` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``python_eulerian_video_magnification.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``python_eulerian_video_magnification.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import logging
import os.path
import sys
from typing import IO

from python_eulerian_video_magnification.magnifycolor import MagnifyColor
from python_eulerian_video_magnification.magnifymotion import MagnifyMotion
from python_eulerian_video_magnification.mode import Mode


class CLI:
    """The command line interface for evm"""

    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser(
            description='This starts eulerian video magnification on the command line',
            epilog='volker.goehler@informatik.tu-freiberg.de',
            prog=os.path.split(sys.argv[0])[-1] if '__main__' not in sys.argv[0] else 'eulerian_video_magnification '
        )
        # prog parameter is a fix if the program is called from module level
        # io group
        io_group = self.parser.add_argument_group("system arguments")
        io_group.add_argument('input', type=argparse.FileType('r'), help="the input video file to work on")
        # TODO meta information for each file worked on, orig filename, timestamp start and end, size, parameter count
        io_group.add_argument('-o', help='output-folder', nargs='?', default=os.path.join(os.path.curdir, "videos"),
                              type=str)
        io_group.add_argument('--color_suffix', help='the suffix to use for color modified result files', nargs='?',
                              type=str, default='color')
        io_group.add_argument('--motion_suffix', help='the suffix to use for motion modified result files', nargs='?',
                              type=str, default='motion')
        io_group.add_argument('--loglevel', help="log level", choices=["debug", "info", "warning", "error", "critical"],
                              type=str,
                              default="warning")

        # arguments
        arg_group = self.parser.add_argument_group("parameters")
        arg_group.add_argument('-m', '--mode', help='the mode of the operation, either enhance colors or motions',
                               type=Mode.from_string,
                               choices=list(Mode), default=Mode.COLOR)
        arg_group.add_argument('-c', '--low', default=0.4, type=float, help="low parameter (creek)")
        arg_group.add_argument('-p', '--high', default=3, type=float, help="high parameter (peek)")
        arg_group.add_argument('-l', '--levels', default=3, type=int, help="levels parameter")
        arg_group.add_argument('-a', '--amplification', default=20, type=int, help="amplification parameter")

    def parse(self, args: list):
        self.args = self.parser.parse_args(args=args)
        self.__sanitize_input()

    def __sanitize_input(self):
        """ This checks for further conditions in input args """
        self.__check_for_video_file()
        self.__manage_output_folder()

    def __check_for_video_file(self):
        """ we check if the input file is valid """
        formats = ('avi', 'mpg', 'mpeg', 'mp4')
        if os.path.splitext(self.args.input.name)[-1] in (".%s" % ext for ext in formats):
            # we got a valid (at least according to extension) file
            pass
        else:
            logging.critical("Input is not a video file. Only supports %s" % ", ".join(formats))
            sys.exit(10)

    def __manage_output_folder(self):
        """ in case the output folder is not existent we create it """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    @property
    def get_log_level(self) -> int:
        """ parses the input loglevel to the numeric value """
        logging.debug(self.args)
        return getattr(logging, self.args.loglevel.upper(), None)

    @property
    def get_mode(self) -> Mode:
        logging.debug(self.args)
        return self.args.mode

    @property
    def get_file(self) -> IO:
        return self.args.input

    @property
    def get_low(self) -> float:
        return self.args.low

    @property
    def get_high(self) -> float:
        return self.args.high

    @property
    def get_levels(self) -> int:
        return self.args.levels

    @property
    def get_amplification(self) -> int:
        return self.args.amplification

    @property
    def output_folder(self) -> str:
        return self.args.o


def main(args=None):
    cli = CLI()
    cli.parse(args=args)

    logging.basicConfig(level=cli.get_log_level)

    # create magnification correct Object
    if cli.get_mode == Mode.COLOR:
        print("Starting Magnification in Color Mode")
        magnify = MagnifyColor
        suffix = cli.args.color_suffix
    elif cli.get_mode == Mode.MOTION:
        print("Starting Magnification in Motion Mode")
        magnify = MagnifyMotion
        suffix = cli.args.motion_suffix
    else:
        raise NotImplementedError("Unknown Mode")

    work = magnify(cli.get_file.name, low=cli.get_low, high=cli.get_high, levels=cli.get_levels,
                   amplification=cli.get_amplification, suffix=suffix, output_folder=cli.args.o)
    work.do_magnify()
