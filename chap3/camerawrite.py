import cv2
cap=cv2.VideoCapture(0)
frame_width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cap.get(cv2.CAP_PROP_FPS)

fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=r'D:\cv\mlcv_env\chap3\out.mp4'
out=cv2.VideoWriter(out,fourcc,int(fps),(int(frame_width),int(frame_height)),False)

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break

    cv2.imshow("output",frame)

    if cv2.waitKey(1) & 0XFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()