import cv2
import numpy as np
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("left button clicked double")
        cv2.circle(image,(x,y),10,(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("left button down")
    elif event == cv2.EVENT_LBUTTONUP:
        print("left button up")
    
image=np.zeros((500,500,3),dtype="uint8")
cv2.namedWindow('Image mouse')
cv2.setMouseCallback('Image mouse', draw_circle)
# cv2.setMouseCallback('Image mouse', draw_circle, param=image) 
while True:
    cv2.imshow('Image mouse', image)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.imwrite("out.png",image)

cv2.destroyAllWindows()
