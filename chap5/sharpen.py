import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_with_matplotlib(out_img, title, pos):
    img_RGB = out_img[:, :, ::-1]
    ax = plt.subplot(3, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title, fontsize=10)
    plt.axis("off")
image = cv2.imread('D:\\cv\\mlcv_env\\chap5\\cat-face.png')
h, w = image.shape[:2]
show_with_matplotlib(image, "Original Image", 1)

smoothed=cv2.GaussianBlur(image, (9, 9), 10)
show_with_matplotlib(smoothed, "Smoothed Image", 2)

unsharped=cv2.addWeighted(image, 1.5, smoothed, -0.5, 0)
show_with_matplotlib(unsharped, "Sharpened Image", 3)

kernel_sharpen_1 = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

kernel_sharpen_2 = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

kernel_sharpen_3 = np.array([[1, 1, 1],
                             [1, -7, 1],
                             [1, 1, 1]])

kernel_sharpen_4 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0

sharpened_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
show_with_matplotlib(sharpened_1, "Sharpened with Kernel 1", 4)

sharpened_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
show_with_matplotlib(sharpened_2, "Sharpened with Kernel 2", 5)

sharpened_3 = cv2.filter2D(image, -1, kernel_sharpen_3)
show_with_matplotlib(sharpened_3, "Sharpened with Kernel 3", 6)

sharpened_4 = cv2.filter2D(image, -1, kernel_sharpen_4)
show_with_matplotlib(sharpened_4, "Sharpened with Kernel 4", 7) 

plt.tight_layout()
plt.show()