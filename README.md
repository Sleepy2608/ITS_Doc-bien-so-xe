# ITS - Doc bien so xe
Topic: Xây dựng hệ thống nhận diện biển số xe (Building a license plate recognition system).

Info:
1. Language: Python.
2. Using K-nearest neighbors (KNN) to associate detected plates across consecutive frames by measuring feature similarity, helping maintain consistent identities and stabilize recognition results
3. OpenCV serves as the foundational computer vision library for preprocessing, traditional license plate detection, basic object tracking, and visualization in license plate tracking systems.
4. Using in real life license plate to test the program.

To sum up, the system is developed using Python ≥ 3.8, with OpenCV employed for image processing and NumPy for data representation. The K-Nearest Neighbors (KNN) algorithm is applied for license plate character recognition, while scikit-learn supports basic machine learning operations. The dependency list is intentionally minimized to ensure reproducibility and efficient deployment.

How to run:
1. Download the ZIP file.
2. Extract all files.
3. Open the project and check whether all file paths and required libraries are correctly configured.
4. Run the complier.
5. To run image: Type `python Image_test2.py` or run in file Image_test2.py
--> All test images will be displayed.
--> The detected numbers and letters on the license plate will be shown.
6. To run video: Type `python Video_test2.py` or run in Video_test2.py (Video size: 1920x1080 - auto implemented)
--> The video will be displayed.
--> All valid and suitable generated results will be displayed and counted using probability.

Note:
1. Use GenData.py to generate KNN data points which is `classifications.txt` and `flattened_images.txt`
2. `training_chars.png` is the input of GenData.py
3. `Preprocess.py` contains functions for image processing
4. Read `setup.txt` to set up suitable environments and libraries to run.
5. If you cannot play the testing video, please refer to `README-VIDEO.txt`.

References:
1. OpenCV Tutorial: Unlock the Power of Visual Data Processing: https://www.datacamp.com/tutorial/opencv-tutorial?utm_cid=19589720824&utm_aid=157156376071&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-apac_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9198559-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~apac-en~dsa~tofu~tutorial~machine-learning&gad_source=1&gad_campaignid=19589720824&gbraid=0AAAAADQ9WsEmOSTlQCEplRrIL04Bd9iY0&gclid=Cj0KCQiAvtzLBhCPARIsALwhxdrewsX8hPb7oae6R3FEtFT8gLkI69W673qBH7A8aVkzF5DyAvXVIqAaAqhEEALw_wcB
2. OpenCV tutorial for beginners | FULL COURSE in 3 hours with Python: https://www.youtube.com/watch?v=eDIj5LuIL4A
3. Machine Learning - K-nearest neighbors (KNN): https://www.w3schools.com/python/python_ml_knn.asp
4. Researched youtuber: Hà Nam 88, Computer vision engineer, Mrzaizai2k - AI, Nicholas Renotte,...
