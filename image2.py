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

######## Upload KNN model ######################
npaClassifications = np.loadtxt("classifications.txt", np.float32)
npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)
npaClassifications = npaClassifications.reshape(
    (npaClassifications.size, 1))  # reshape numpy array to 1d, necessary to pass to call to train
kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)
#########################

################ Image Preprocessing #################
imgGrayscaleplate, imgThreshplate = Preprocess.preprocess(img)
canny_image = cv2.Canny(imgThreshplate, 250, 255)  # Canny Edge
kernel = np.ones((3, 3), np.uint8)
dilated_image = cv2.dilate(canny_image, kernel, iterations=1)  # Dilation
# cv2.imshow("dilated_image",dilated_image)

###########################################
