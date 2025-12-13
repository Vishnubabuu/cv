import cv2

cap=cv2.VideoCapture(r'D:\cv\mlcv_env\chap3\6548176-hd_1920_1080_24fps.mp4')
frame=cap.get(cv2.CAP_PROP_FRAME_COUNT)
while(True):
    ret,frame=cap.read()
    if not ret:
        break

    cv2.imshow("out",frame)
    if (cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

