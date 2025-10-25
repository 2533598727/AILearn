import cv2
import numpy as np

img = cv2.imread("D:\AILearn\Digital image processing\code\image.png", cv2.IMREAD_UNCHANGED)
out = cv2.Laplacian(img, cv2.CV_64F)  # 计算拉普拉斯导数
out = cv2.convertScaleAbs(out)  # 取绝对值并转换为 8 位无符号整数
cv2.imshow("Laplacian", out)  # 显示拉普拉斯导数
cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()  # 关闭所有窗口