# ITS - Doc bien so xe

Info:
1. Language: Python.
2. Using OpenCV.

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
