# -*- coding: utf-8 -*-

import cv2
import numpy as np

from python_eulerian_video_magnification.filter import temporal_ideal_filter
from python_eulerian_video_magnification.magnify import Magnify
from python_eulerian_video_magnification.pyramid import gaussian_video


class MagnifyColor(Magnify):
    def _magnify_impl(self, tensor: np.ndarray, fps: int) -> np.ndarray:
        gau_video = gaussian_video(tensor, levels=self._levels)
        filtered_tensor = temporal_ideal_filter(gau_video, self._low, self._high, fps)
        amplified_video = self._amplify_video(filtered_tensor)
        return self._reconstruct_video(amplified_video, tensor)

    def _amplify_video(self, gaussian_vid):
        return gaussian_vid * self._amplification

    def _reconstruct_video(self, amp_video, origin_video):
        final_video = np.zeros(origin_video.shape)
        for i in range(0, amp_video.shape[0]):
            img = amp_video[i]
            for x in range(self._levels):
                img = cv2.pyrUp(img)
            img = img + origin_video[i]
            final_video[i] = img
        return final_video
