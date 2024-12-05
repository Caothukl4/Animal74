import cv2
from ultralytics import YOLO

# Đường dẫn đến mô hình
model_path = '74.pt'  # Thay đổi đường dẫn đến mô hình của bạn

# Tải mô hình
model = YOLO(model_path)

# Mở camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    if not ret:
        print("Không thể đọc khung hình từ camera.")
        break

    # Thực hiện dự đoán
    results = model(frame)

    # Hiển thị kết quả trên khung hình
    annotated_frame = results[0].plot()  # Lấy khung hình đã đánh dấu
    cv2.imshow('YOLOv8 Detection', annotated_frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()


# import cv2
# import os
# from ultralytics import YOLO

# # Đường dẫn đến mô hình và thư mục ảnh
# model_path = '74.pt'  # Thay đổi đường dẫn đến mô hình của bạn
# image_folder = 'C:\\Users\\pc\\OneDrive\\Documents\\CyberLink\\Máy tính\\cndpt'  # Thay đổi đường dẫn đến thư mục chứa ảnh của bạn

# # Tải mô hình
# model = YOLO(model_path)

# # Lấy danh sách tất cả các ảnh trong thư mục
# image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# # Duyệt qua từng ảnh trong thư mục
# for image_file in image_files:
#     image_path = os.path.join(image_folder, image_file)

#     # Đọc ảnh
#     frame = cv2.imread(image_path)
#     if frame is None:
#         print(f"Không thể đọc ảnh {image_file}")
#         continue

#     # Thực hiện dự đoán
#     results = model(frame)

#     # Hiển thị kết quả trên ảnh
#     annotated_frame = results[0].plot()  # Lấy khung hình đã đánh dấu
#     cv2.imshow('YOLOv8 Detection', annotated_frame)

#     # Đợi người dùng nhấn phím để xem ảnh tiếp theo, hoặc thoát khi nhấn 'q'
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break

# # Đóng cửa sổ hiển thị
# cv2.destroyAllWindows()
