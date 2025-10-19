import cv2
import numpy as np

img = cv2.imread("D:\AILearn\Digital image processing\code\image.png")
k = np.ones((5,5),np.uint8)
r = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)
cv2.imshow("img", img)
cv2.imshow("r", r)
cv2.waitKey(0)
cv2.destroyAllWindows(
)