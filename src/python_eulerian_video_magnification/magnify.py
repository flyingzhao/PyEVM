# -*- coding: utf-8 -*-
import cv2
import numpy as np


class Magnify:
    def __init__(self, video_filename: str, low: float, high: float, levels: int = 3, amplification: int = 20):
        self._low = low
        self._high = high
        self._levels = levels
        self._amplification = amplification
        self._out_file_name = "out.avi"
        self._in_file_name = video_filename

    def load_video(self) -> (np.ndarray, int):
        cap = cv2.VideoCapture(self._in_file_name)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        video_tensor = np.zeros((frame_count, height, width, 3), dtype='float')
        x = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if ret is True:
                video_tensor[x] = frame
                x += 1
            else:
                break
        return video_tensor, fps

    def save_video(self, video_tensor: np.ndarray) -> None:
        four_cc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        [height, width] = video_tensor[0].shape[0:2]
        writer = cv2.VideoWriter(self._out_file_name, four_cc, 30, (width, height), 1)
        for i in range(0, video_tensor.shape[0]):
            writer.write(cv2.convertScaleAbs(video_tensor[i]))
        writer.release()

    def do_magnify(self) -> None:
        tensor, fps = self.load_video()
        video_tensor = self._magnify_impl(tensor, fps)
        self.save_video(video_tensor)

    def _magnify_impl(self, tensor: np.ndarray, fps: int) -> np.ndarray:
        raise NotImplementedError("This should be overwritten!")
