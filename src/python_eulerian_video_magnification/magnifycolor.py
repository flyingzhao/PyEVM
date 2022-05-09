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
        origin_video_shape = origin_video.shape[1:]
        for i in range(0, amp_video.shape[0]):
            img = amp_video[i]
            for x in range(self._levels):
                img = cv2.pyrUp(img)  # this doubles the dimensions of img each time
            # ensure that dimensions are equal
            origin_video[i] += self._correct_dimensionality_problem_after_pyr_up(img, origin_video_shape)
        return origin_video

    def _correct_dimensionality_problem_after_pyr_up(self, img: np.ndarray, origin_video_frame_shape) -> np.ndarray:
        if img.shape != origin_video_frame_shape:
            return np.resize(img, origin_video_frame_shape)
        else:
            return img

    def principal_component_analysis(self, tensor: np.ndarray):
        # Data matrix tensor, assumes 0-centered
        n, m = tensor.shape
        assert np.allclose(tensor.mean(axis=0), np.zeros(m))
        # Compute covariance matrix
        covariance_matrix = np.dot(tensor.T, tensor) / (n - 1)
        # Eigen decomposition
        eigen_vals, eigen_vecs = np.linalg.eig(covariance_matrix)
        # Project tensor onto PC space
        X_pca = np.dot(tensor, eigen_vecs)
        return X_pca
