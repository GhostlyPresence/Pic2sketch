import cv2
import numpy as np 

cv2.namedWindow("out",flags=cv2.WINDOW_AUTOSIZE)

img = cv2.imread("image.jpg",0)
h,w = img.shape


stick = img.copy()
stick = cv2.resize(stick,(w//5,h//5))
hs,ws = stick.shape



k=29
neg = 255 - img
neg = cv2.GaussianBlur(neg,(k,k),0,0)
out = cv2.divide(img,255-neg,scale=256)
arr = np.ones((h,w),np.uint8)*50

out = cv2.subtract(out,arr)
out[0:hs,0:ws] = stick
cv2.imshow("out",out)
#cv2.imshow("stick",stick)

#cv2.imwrite("sketch.jpg",out)
cv2.waitKey(0)
