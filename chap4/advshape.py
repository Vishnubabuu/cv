import cv2
import numpy as np
image=np.zeros((400,400,3),dtype="uint8")
# cv2.line(image,(0,0),(400,400),(0,255,255),3)
# cv2.rectangle(image,(0,0),(100,100),(255,0,0),3)
# ret,p1,p2=cv2.clipLine((0,0,100,100),(0,0),(300,300))
# if ret:
#     cv2.line(image,p1,p2,(255,0,255),3)
# cv2.arrowedLine(image,(100,200),(300,200),(255,255,0),3,8,0,0.1)
# cv2.arrowedLine(image,(100,100),(300,100),(0,255,0),3,cv2.LINE_AA,0,0.3)
# cv2.arrowedLine(image,(100,300),(300,300),(0,255,255),3,cv2.LINE_4,0,0.3)
# cv2.ellipse(image,(200,200),(100,80),90,0,360,(0,220,250),-1)
pts=np.array([[250,5],[220,80],[280,80],[280,5]],np.int32)
pts=pts.reshape(-1,1,2)
cv2.polylines(image,[pts],True,(0,0,255),3)
cv2.imshow("output",image)
cv2.waitKey(0)
cv2.destroyAllWindows()