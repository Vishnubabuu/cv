import cv2
import time
cap=cv2.VideoCapture(0)
while cap.isOpened():
    process_start =time.time()
    ret,frame=cap.read()
    if not ret:
        break
    process_end=time.time()

    process_time_frame= process_end-process_start
    print(f"time per frame is :{1.0/process_time_frame}")

    cv2.imshow('output',frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()