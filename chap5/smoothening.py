import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_with_matplotlib(out_img, title, pos):
    img_RGB = out_img[:, :, ::-1]
    ax = plt.subplot(3, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title, fontsize=8)
    plt.axis("off")

image = cv2.imread('D:\\cv\\mlcv_env\\chap5\\cat-face.png')
h, w = image.shape[:2]
show_with_matplotlib(image, "Original Image", 1)

kernel_5x5 = np.ones((5, 5), np.float32) / 25
kernel_10x10 = np.ones((10, 10), np.float32) / 100

smoothed_img_5x5 = cv2.filter2D(image, -1, kernel_5x5)
show_with_matplotlib(smoothed_img_5x5, "5x5 Averaging Filter", 2)

smoothed_img_10x10 = cv2.filter2D(image, -1, kernel_10x10)
show_with_matplotlib(smoothed_img_10x10, "10x10 Averaging Filter", 3)

gaussian_blur_5x5 = cv2.GaussianBlur(image, (5, 5), 0)
show_with_matplotlib(gaussian_blur_5x5, "5x5 Gaussian Blur", 4)

median_blur_5 = cv2.medianBlur(image, 5)
show_with_matplotlib(median_blur_5, "Median Blur k=5", 5)   

img_blur=cv2.blur(image, (5, 5))
show_with_matplotlib(img_blur, "cv2.blur k=5", 6)

img_box_filter=cv2.boxFilter(image, -1, (5, 5))
show_with_matplotlib(img_box_filter, "cv2.boxFilter k=5", 7)


smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
show_with_matplotlib(smooth_image_bf, "Bilateral Filter d=5", 8)

smooth_image_bf_2 = cv2.bilateralFilter(image, 9, 200, 200)
show_with_matplotlib(smooth_image_bf_2, "Bilateral Filter d=9", 9)

plt.tight_layout()
plt.show()