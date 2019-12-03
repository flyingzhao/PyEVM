#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Volker Göhler 2019

import argparse
import os.path


class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Do EVM.')
        parser.add_argument('input', type=argparse.FileType('r'))
        parser.add_argument('method', choices=['color', 'motion'])
        parser.add_argument('output-folder', nargs='?', default=os.path.join(os.path.curdir, "videos"), type=str)
        parser.add_argument('color-suffix', nargs='?', type=str, default='color')
        parser.add_argument('motion-suffix', nargs='?', type=str, default='motion')

        args = parser.parse_args()
        print(args.accumulate(args.integers))

    def __usage(self):
        pass

