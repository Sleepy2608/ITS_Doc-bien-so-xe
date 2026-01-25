# ITS - Doc bien so xe

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

References:
1. Vietnamese License Plate Recognition in 3 steps using OpenCV and KNN: https://youtu.be/7erlCp6d5w8?si=TsBLXfu-T4a1Owm9
2. mrzaizai2k: https://github.com/mrzaizai2k
3. [OpenCV] Full Hệ thống Nhận diện biển số xe, bãi đỗ xe thông minh (License plate Indentification): https://youtu.be/cItwiM6XBqs?si=yOonV5bU4Ftzf8xb
4. [OpenCV] P2 Nhận diện biển số xe (License plate identification) Python Opencv bằng FrameWork Django: https://youtu.be/Mf8-1IMCnnY?si=RI1T2rC_GElc3MT-
