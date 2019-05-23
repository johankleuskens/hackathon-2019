import cv2
import os
import time

cam = cv2.VideoCapture(-1)

cv2.namedWindow("test")

img_counter = 0

os.chdir("../keras-frcnn")

oldepoch = time.time()

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if not ret:
        break
    if time.time() - oldepoch > 15:
	oldepoch = time.time()
        img_name = "/tmp/opencv_frame.jpg".format(0)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
	os.system("python test_frcnn_count.py --input_dir /tmp --input_file ~/tmp/opencv_frame.jpg --output_dir /tmp")

cam.release()

cv2.destroyAllWindows()
