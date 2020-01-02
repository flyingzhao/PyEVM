# -*- coding: utf-8 -*-
# Volker Göhler 2019,2020
import enum


@enum.unique
class Mode(enum.Enum):
    COLOR = 1
    MOTION = 2
