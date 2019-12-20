# -*- coding: utf-8 -*-
# Volker Göhler 2019,2020
import cv2
import numpy as np


def build_gaussian_pyramid(src, level=3):
    s = src.copy()
    pyramid = [s]
    for i in range(level):
        s = cv2.pyrDown(s)
        pyramid.append(s)
    return pyramid


def build_laplacian_pyramid(src, levels=3):
    gaussianPyramid = build_gaussian_pyramid(src, levels)
    pyramid = []
    for i in range(levels, 0, -1):
        GE = cv2.pyrUp(gaussianPyramid[i])
        L = cv2.subtract(gaussianPyramid[i - 1], GE)
        pyramid.append(L)
    return pyramid


def gaussian_video(video_tensor, levels=3):
    for i in range(0, video_tensor.shape[0]):
        frame = video_tensor[i]
        pyr = build_gaussian_pyramid(frame, level=levels)
        gaussian_frame = pyr[-1]
        if i == 0:
            vid_data = np.zeros((video_tensor.shape[0], gaussian_frame.shape[0], gaussian_frame.shape[1], 3))
        vid_data[i] = gaussian_frame
    return vid_data


def laplacian_video(video_tensor, levels=3):
    tensor_list = []
    for i in range(0, video_tensor.shape[0]):
        frame = video_tensor[i]
        pyr = build_laplacian_pyramid(frame, levels=levels)
        if i == 0:
            for k in range(levels):
                tensor_list.append(np.zeros((video_tensor.shape[0], pyr[k].shape[0], pyr[k].shape[1], 3)))
        for n in range(levels):
            tensor_list[n][i] = pyr[n]
    return tensor_list
