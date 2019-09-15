import cv2
import numpy as np
from camera import VideoCamera

while True:
    frame = VideoCamera().get_frame()
