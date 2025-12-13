import cv2
import numpy as np
import matplotlib.pyplot as plt
input=cv2.imread('image.png')
b,g,r = cv2.split(input)
out= cv2.merge([r,g,b])
plt.subplot(211)
plt.imshow(input)
plt.subplot(212)
plt.imshow(out)
plt.show()
fin=np.concatenate((input,out),axis=1)
cv2.imshow('out',out)
cv2.imshow('inp',input)
cv2.imshow('fin',fin)
cv2.waitKey(0)
cv2.destroyAllWindows()