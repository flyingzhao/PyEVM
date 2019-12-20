# -*- coding: utf-8 -*-
# Volker Göhler 2019,2020

import numpy as np


class Converter:
    """
    collection of colour space format methods
    TODO do we need these?
    """

    @staticmethod
    def __convert(src, t_array):
        [rows, cols] = src.shape[:2]
        dst = np.zeros((rows, cols, 3), dtype=np.float64)
        for i in range(rows):
            for j in range(cols):
                dst[i, j] = np.dot(t_array, src[i, j])
        return dst

    @staticmethod
    def rgb2ntsc(src):
        t_array = np.array([[0.114, 0.587, 0.298], [-0.321, -0.275, 0.596], [0.311, -0.528, 0.212]])
        return Converter.__convert(src, t_array)

    @staticmethod
    def ntsc2rbg(src):
        """
        convert YIQ to RGB
        """
        t_array = np.array([[1, -1.108, 1.705], [1, -0.272, -0.647], [1, 0.956, 0.620]])
        return Converter.__convert(src, t_array)
