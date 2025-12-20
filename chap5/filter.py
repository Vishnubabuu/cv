import cv2
import numpy as np

img=cv2.imread('D:\cv\mlcv_env\chap5\cat-face.png')
kernel_average = np.ones((5,5),np.float32)/25
smooth_img=cv2.filter2D(img,-1,kernel_average)
cv2.imshow('smoothed_image.png',smooth_img)
cv2.imshow('original_image.png',img)
print("Averaging Kernel: \n", kernel_average)
cv2.waitKey(0)
cv2.destroyAllWindows()