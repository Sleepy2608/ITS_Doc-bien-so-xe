# Xây dựng hệ thống nhận diện biển số xe - ITS

**TIẾNG VIỆT**

Topic: Xây dựng hệ thống nhận diện biển số xe.

Thông tin dự án:
1. Ngôn ngữ: Python
2. Hệ thống sử dụng K-Nearest Neighbors (KNN) để liên kết các biển số được phát hiện qua các khung hình liên tiếp dựa trên độ tương đồng đặc trưng, giúp duy trì định danh ổn định và cải thiện kết quả nhận diện.
3. OpenCV là thư viện thị giác máy tính chính, dùng cho tiền xử lý ảnh, phát hiện biển số theo phương pháp truyền thống, theo dõi đối tượng cơ bản và trực quan hóa kết quả.
4. Hệ thống được kiểm thử với biển số xe thực tế.

Tóm lại, hệ thống được phát triển trên nền Python ≥ 3.8, sử dụng OpenCV cho xử lý ảnh và NumPy cho biểu diễn dữ liệu. Thuật toán KNN được áp dụng cho bài toán nhận dạng ký tự biển số, với scikit-learn hỗ trợ các thao tác học máy cơ bản. Danh sách thư viện được tối giản nhằm đảm bảo khả năng tái lập và hiệu quả triển khai.

Cách chạy chương trình:
1. Tải file ZIP của dự án.
2. Giải nén toàn bộ file.
3. Mở project và kiểm tra đường dẫn file cũng như các thư viện cần thiết.
4. Chạy chương trình.
5. Khi chạy với ảnh: Gõ: python `Image_test2.py` hoặc chạy trực tiếp file Image_test2.py -> Tất cả ảnh test sẽ được hiển thị cùng với ký tự nhận diện trên biển số.
6. Chạy với video: Gõ: python `Video_test2.py` hoặc chạy trực tiếp file Video_test2.py (Độ phân giải video đầu vào: 1920×1080) -> Video sẽ được hiển thị và các kết quả nhận diện hợp lệ sẽ được hiển thị và đếm dựa trên xác suất.

Cấu trúc dự án:
1. Sử dụng `GenData.py` để tạo dữ liệu huấn luyện cho KNN, bao gồm `classifications.txt` và `flattened_images.txt`.
2. File `training_chars.png` là dữ liệu đầu vào cho `GenData.py`.
3. `Preprocess.py` chứa các hàm tiền xử lý ảnh.
4. Đọc file `setup.txt` để thiết lập môi trường và thư viện phù hợp.
5. Nếu không thể chạy video test, hãy đọc ở `README-VIDEO.txt` trong tệp data.

References:
1. Hướng dẫn OpenCV: Unlock the Power of Visual Data Processing: https://www.datacamp.com/tutorial/opencv-tutorial?utm_cid=19589720824&utm_aid=157156376071&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-apac_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9198559-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~apac-en~dsa~tofu~tutorial~machine-learning&gad_source=1&gad_campaignid=19589720824&gbraid=0AAAAADQ9WsEmOSTlQCEplRrIL04Bd9iY0&gclid=Cj0KCQiAvtzLBhCPARIsALwhxdrewsX8hPb7oae6R3FEtFT8gLkI69W673qBH7A8aVkzF5DyAvXVIqAaAqhEEALw_wcB
2. OpenCV tutorial for beginners | FULL COURSE in 3 hours with Python: https://www.youtube.com/watch?v=eDIj5LuIL4A
3. Machine Learning - K-nearest neighbors (KNN): https://www.w3schools.com/python/python_ml_knn.asp
4. Các youtuber được dùng để tham khảo: Hà Nam 88, Computer vision engineer, Mrzaizai2k - AI, Nicholas Renotte,...

#
**ENGLISH**

Topic: Building a license plate recognition system.

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

Project Structure:
1. Use `GenData.py` to generate KNN data points which is `classifications.txt` and `flattened_images.txt`.
2. `training_chars.png` is the input of `GenData.py`.
3. `Preprocess.py` contains functions for image processing.
4. Read `setup.txt` to set up suitable environments and libraries to run.
5. If you cannot play the testing video, please refer to `README-VIDEO.txt` in the data folder.

References:
1. OpenCV Tutorial: Unlock the Power of Visual Data Processing: https://www.datacamp.com/tutorial/opencv-tutorial?utm_cid=19589720824&utm_aid=157156376071&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-apac_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9198559-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~apac-en~dsa~tofu~tutorial~machine-learning&gad_source=1&gad_campaignid=19589720824&gbraid=0AAAAADQ9WsEmOSTlQCEplRrIL04Bd9iY0&gclid=Cj0KCQiAvtzLBhCPARIsALwhxdrewsX8hPb7oae6R3FEtFT8gLkI69W673qBH7A8aVkzF5DyAvXVIqAaAqhEEALw_wcB
2. OpenCV tutorial for beginners | FULL COURSE in 3 hours with Python: https://www.youtube.com/watch?v=eDIj5LuIL4A
3. Machine Learning - K-nearest neighbors (KNN): https://www.w3schools.com/python/python_ml_knn.asp
4. Researched youtuber: Hà Nam 88, Computer vision engineer, Mrzaizai2k - AI, Nicholas Renotte,...
