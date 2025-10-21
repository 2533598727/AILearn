import cv2
import numpy as np

img = cv2.imread("D:\AILearn\Digital image processing\code\image.png", cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img, 120, 200)  # 应用 Canny 边缘检测，阈值为 50 和 150

cv2.imshow("Canny", canny)  # 显示 Canny 边缘检测结果
cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()  # 关闭所有窗口