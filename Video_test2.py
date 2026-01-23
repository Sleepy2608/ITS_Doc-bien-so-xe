# Phúc
import math

import cv2
import numpy as np

import Preprocess

ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9

Min_char_area = 0.015
Max_char_area = 0.06

Min_char = 0.01
Max_char = 0.09

Min_ratio_char = 0.25
Max_ratio_char = 0.7

max_size_plate = 18000
min_size_plate = 5000

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

tongframe = 0
biensotimthay = 0

# Load KNN model
npaClassifications = np.loadtxt("classifications.txt", np.float32)
npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)
npaClassifications = npaClassifications.reshape(
    (npaClassifications.size, 1))  # reshape numpy array to 1d, necessary to pass to call to train
kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)
//Read video
cap = cv2.VideoCapture('data/video/video1.mp4')
while (cap.isOpened()):
    # Image preprocessing
    ret, img = cap.read()
    tongframe = tongframe + 1
    # img = cv2.resize(img, None, fx=0.5, fy=0.5)
    imgGrayscaleplate, imgThreshplate = Preprocess.preprocess(img)
    canny_image = cv2.Canny(imgThreshplate, 250, 255)  # Canny Edge
    kernel = np.ones((3, 3), np.uint8)
    dilated_image = cv2.dilate(canny_image, kernel,iterations=1)  # Dilation
    # Filter out license plates
    contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]  # Pick out 10 biggest contours
    screenCnt = []
    for c in contours:
        peri = cv2.arcLength(c, True)  # Tính chu vi
        approx = cv2.approxPolyDP(c, 0.06 * peri, True)  # Approximate the edges of contours
        [x, y, w, h] = cv2.boundingRect(approx.copy())
        ratio = w / h
        if (len(approx) == 4) and (0.8 <= ratio <= 1.5 or 4.5 <= ratio <= 6.5):
            screenCnt.append(approx)
    if screenCnt is None:
        detected = 0
        print("No plate detected")
    else:
        detected = 1
