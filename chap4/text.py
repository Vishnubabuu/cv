import cv2
import numpy as np

image=np.zeros((400,400,3),dtype='uint8')
image[:]=(255,255,255)
for i in range(0,8):
    p=i*10
    q=i*30
    cv2.putText(image,"hello man",(p,q),i,0.9,(255,220,220),3,cv2.LINE_AA)
cv2.imshow("output",image)
cv2.waitKey(0)
cv2.destroyAllWindows()