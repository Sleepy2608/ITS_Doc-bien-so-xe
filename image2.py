import math

import cv2
import numpy as np

import Preprocess

ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9

n = 1

Min_char = 0.01
Max_char = 0.09

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

img = cv2.imread("data/image/10.jpg")
img = cv2.resize(img, dsize=(1920, 1080))
