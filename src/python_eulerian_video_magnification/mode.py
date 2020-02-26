# -*- coding: utf-8 -*-
import enum


@enum.unique
class Mode(enum.Enum):
    COLOR = 1
    MOTION = 2

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return Mode[s.upper()]
        except KeyError:
            raise ValueError()
