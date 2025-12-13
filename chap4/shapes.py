import cv2
import numpy as np
image=np.zeros((400,400,3),dtype="uint8")
image[:]=(220,220,220)
cv2.line(image,(0,0),(400,400),(0,255,0),3)
cv2.rectangle(image,(100,100),(300,300),(220,0,255),-1)
cv2.circle(image,(200,200),50,(255,220,220),-1)
cv2.imshow("output",image)
cv2.waitKey(0)
cv2.destroyAllWindows()