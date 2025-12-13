import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_with_matplotlib(out_img,title,pos):
    img_RGB = out_img[:,:,::-1]
    ax = plt.subplot(3,6,pos)
    plt.imshow(img_RGB)
    plt.title(title,fontsize=8)
    plt.axis("off")

image=cv2.imread('lena_image.png')
h,w=image.shape[:2]
plt.figure(figsize=(12,6))
plt.suptitle("Splitting and merging channels in OpenCV", fontsize=14, fontweight='bold')
show_with_matplotlib(image,"input",1)

resized_image=cv2.resize(image,(w * 2,h * 2),interpolation=cv2.INTER_LINEAR)
show_with_matplotlib(resized_image,"2x INTER_LINEAR",2)

dst_image=cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
show_with_matplotlib(dst_image,"0.5x INTER_LINEAR",3)

m=np.float32([[1,0,200],[0,1,30]])
tran_img=cv2.warpAffine(image,m,(w,h))
show_with_matplotlib(tran_img,"transulated",7)

m=np.float32([[1,0,-200],[0,1,-30]])
neg_tran_img=cv2.warpAffine(image,m,(w,h))
show_with_matplotlib(neg_tran_img,"transulated",8)

m=cv2.getRotationMatrix2D((w/2.0,h/2.0),180,1)
dst_img = cv2.warpAffine(image,m,(w,h))
show_with_matplotlib(dst_img,"rotate",9)

dst_img= image[80:200,230:330]
show_with_matplotlib(dst_img,"cropped",10)

pt1=np.float32([[135,45],[385,48],[135,230]])
pt2=np.float32([[135,45],[385,48],[150,230]])
m=cv2.getAffineTransform(pt1,pt2)
dst_image=cv2.warpAffine(image,m,(w,h))
show_with_matplotlib(dst_image,"affline_trans",13)

pt1=np.float32([[450,65],[517,65],[431,164],[552,164]])
pt2=np.float32([[0,0],[300,0],[0,300],[300,300]])
m=cv2.getPerspectiveTransform(pt1,pt2)
dst_img=cv2.warpPerspective(image,m,(300,300))
show_with_matplotlib(dst_img,"persp_img",14)
plt.tight_layout()
plt.show()