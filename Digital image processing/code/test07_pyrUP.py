import cv2
import numpy as np

img = cv2.imread("D:\AILearn\Digital image processing\code\image.png", cv2.IMREAD_GRAYSCALE)

r1 = cv2.pyrUp(img)  # 上采样
r2 = cv2.pyrUp(r1)  # 上采样
r3 = cv2.pyrUp(r2)  # 上采样
r4 = cv2.pyrUp(r3)  # 上采样

cv2.imshow("r1", r1)  # 显示上采样结果
cv2.imshow("r2", r2)  # 显示上采样结果
cv2.imshow("r3", r3)  # 显示上采样结果
cv2.imshow("r4", r4)  # 显示上采样结果
cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()  # 关闭所有窗口