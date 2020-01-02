# -*- coding: utf-8 -*-

import cv2
import numpy as np

from python_eulerian_video_magnification.filter import butter_bandpass_filter
from python_eulerian_video_magnification.magnify import Magnify
from python_eulerian_video_magnification.pyramid import laplacian_video


class MagnifyMotion(Magnify):
    def _magnify_impl(self, tensor: np.ndarray, fps: int) -> np.ndarray:
        lap_video_list = laplacian_video(tensor, levels=self._levels)
        filter_tensor_list = []
        for i in range(self._levels):
            filter_tensor = butter_bandpass_filter(lap_video_list[i], self._low, self._high, fps)
            filter_tensor *= self._amplification
            filter_tensor_list.append(filter_tensor)
        recon = self._reconstruct_from_tensor_list(filter_tensor_list)
        return tensor + recon

    def _reconstruct_from_tensor_list(self, filter_tensor_list):
        final = np.zeros(filter_tensor_list[-1].shape)
        for i in range(filter_tensor_list[0].shape[0]):
            up = filter_tensor_list[0][i]
            for n in range(self._levels - 1):
                up = cv2.pyrUp(up) + filter_tensor_list[n + 1][i]
            final[i] = up
        return final
