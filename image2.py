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

###### Draw contour and filter out the license plate  #############
contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]  # Lấy 10 contours có diện tích lớn nhất
# cv2.drawContours(img, contours, -1, (255, 0, 255), 3) # Vẽ tất cả các ctour trong hình lớn

screenCnt = []
for c in contours:
    peri = cv2.arcLength(c, True)  # Tính chu vi
    approx = cv2.approxPolyDP(c, 0.06 * peri, True)  # làm xấp xỉ đa giác, chỉ giữ contour có 4 cạnh
    [x, y, w, h] = cv2.boundingRect(approx.copy())
    ratio = w / h
    # cv2.putText(img, str(len(approx.copy())), (x,y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
    # cv2.putText(img, str(ratio), (x,y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
    if (len(approx) == 4):
        screenCnt.append(approx)

        cv2.putText(img, str(len(approx.copy())), (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)

if screenCnt is None:
    detected = 0
    print("No plate detected")
else:
    detected = 1
