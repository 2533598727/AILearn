import cv2
import numpy as np

img = cv2.imread("D:\AILearn\Digital image processing\code\image.png", cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)  # 计算 x 方向的 Sobel 导数
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)  # 计算 y 方向的 Sobel 导数
sobelx = cv2.convertScaleAbs(sobelx)  # 取绝对值并转换为 8 位无符号整数
sobely = cv2.convertScaleAbs(sobely)  # 取绝对值并转换为 8 位无符号整数
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  # 加权合并 x 和 y 方向的导数

scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)  # 计算 x 方向的 Scharr 导数
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)  # 计算 y 方向的 Scharr 导数
scharrx = cv2.convertScaleAbs(scharrx)  # 取绝对值并转换为 8 位无符号整数
scharry = cv2.convertScaleAbs(scharry)  # 取绝对值并转换为 8 位无符号整数
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)  # 加权合并 x 和 y 方向的导数

cv2.imshow("Sobel", sobelxy)  # 显示 Sobel 导数
cv2.imshow("Scharr", scharrxy)  # 显示 Scharr 导数
cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()  # 关闭所有窗口