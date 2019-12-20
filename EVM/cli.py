#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Volker Göhler 2019,2020

import argparse
import logging
import os.path
from typing import IO

from EVM.mode import Mode


class CLI:
    """The command line interface for evm"""

    def __init__(self):
        parser = argparse.ArgumentParser(description='This starts eulerian video magnification on the command line',
                                         epilog='volker.goehler@informatik.tu-freiberg.de'
                                         )
        # io group
        io_group = parser.add_argument_group("system arguments")
        io_group.add_argument('input', type=argparse.FileType('r'), help="the input video file to work on")
        # TODO meta information for each file worked on, orig filename, timestamp start and end, size, parameter count
        io_group.add_argument('-o', help='output-folder', nargs='?', default=os.path.join(os.path.curdir, "videos"),
                              type=str)
        io_group.add_argument('--color_suffix', help='the suffix to use for color modified result files', nargs='?',
                              type=str, default='color')
        io_group.add_argument('--motion_suffix', help='the suffix to use for motion modified result files', nargs='?',
                              type=str, default='motion')
        io_group.add_argument('--log', help="log level", choices=["debug", "info", "warning", "error", "critical"],
                              type=str,
                              default="warning")

        # arguments
        arg_group = parser.add_argument_group("parameters")
        arg_group.add_argument('-m', help='mode', choices=['color', 'motion'], default='color')
        arg_group.add_argument('-c', '--low', default=0.4, type=float, help="low parameter (creek)")
        arg_group.add_argument('-p', '--high', default=3, type=float, help="high parameter (peek)")
        arg_group.add_argument('-l', '--levels', default=3, type=int, help="levels parameter")
        arg_group.add_argument('-a', '--amplification', default=20, type=int, help="amplification parameter")

        self.args = parser.parse_args()

        self.__sanitize_input()

        ## logic steps
        # copy input to video/original folder
        # create the result video in video/result/{originalname}_{methodname}

    def __sanitize_input(self):
        """ This checks for further conditions in input args """
        self.__check_for_video_file()
        self.__manage_output_folder()

    def __check_for_video_file(self):
        """ we check if the input file is valid """
        formats = ('avi', 'mpg', 'mpeg')
        if os.path.splitext(self.args.input) in (".%s" % ext for ext in formats):
            # we got a valid (at least according to extension) file
            pass
        else:
            logging.CRITICAL("Input is not a video file. Only supports %s" % ", ".join(formats))
            SystemExit()

    def __manage_output_folder(self):
        """ in case the output folder is not existent we create it """
        if not os.path.exists(self.args.output_folder):
            os.makedirs(self.args.output_folder)

    @property
    def get_log_level(self) -> int:
        """ parses the input loglevel to the numeric value """
        return getattr(logging, self.args.logging.upper(), None)

    @property
    def get_mode(self) -> int:
        return getattr(Mode, self.args.mode.upper(), None)

    @property
    def get_file(self) -> IO:
        return self.args.input

    @property
    def get_low(self) -> int:
        return self.args.low

    @property
    def get_high(self) -> int:
        return self.args.high

    @property
    def get_levels(self) -> int:
        return self.args.levels

    @property
    def get_amplification(self) -> int:
        return self.args.amplification
