import cv2

img = cv2.imread("D:\AILearn\Digital image processing\code\image.png")
img2 = cv2.medianBlur(img, 3) # 中值滤波滤波核大小为3
img3 = cv2.GaussianBlur(img, (3, 3), 0) # 高斯滤波核大小为3x3
img4 = cv2.blur(img, (3, 3)) # 均值滤波核大小为3x3
cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

