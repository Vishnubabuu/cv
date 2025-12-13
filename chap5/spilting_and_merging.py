import cv2
import matplotlib.pyplot as plt

def show_with_matplotlib(color_img, title, pos):
    img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title, fontsize=8)
    plt.axis('off')

image = cv2.imread('color_spaces.png')
h,w=image.shape[:2]

plt.figure(figsize=(h, w))
plt.suptitle("Splitting and merging channels in OpenCV", fontsize=14, fontweight='bold')

# ---- ROW 1 ----
show_with_matplotlib(image, "Original BGR image", 1)

(b, g, r) = cv2.split(image)

show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "B channel", 2)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "G channel", 3)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "R channel", 4)

image_copy = cv2.merge((b, g, r))
show_with_matplotlib(image_copy, "Merged BGR image", 5)

# ---- ROW 2 ----
image_without_blue = image.copy()
image_without_blue[:, :, 0] = 0
show_with_matplotlib(image_without_blue, "No Blue", 7)

image_without_green = image.copy()
image_without_green[:, :, 1] = 0
show_with_matplotlib(image_without_green, "No Green", 8)

image_without_red = image.copy()
image_without_red[:, :, 2] = 0
show_with_matplotlib(image_without_red, "No Red", 9)

# ---- ROW 3: CHANNELS AFTER REMOVAL ----
# Channels after removing Blue
(b2, g2, r2) = cv2.split(image_without_blue)
show_with_matplotlib(cv2.cvtColor(b2, cv2.COLOR_GRAY2BGR), "No Blue → B", 13)
show_with_matplotlib(cv2.cvtColor(g2, cv2.COLOR_GRAY2BGR), "No Blue → G", 14)
show_with_matplotlib(cv2.cvtColor(r2, cv2.COLOR_GRAY2BGR), "No Blue → R", 15)

# Channels after removing Green
(b3, g3, r3) = cv2.split(image_without_green)
show_with_matplotlib(cv2.cvtColor(b3, cv2.COLOR_GRAY2BGR), "No Green → B", 16)
show_with_matplotlib(cv2.cvtColor(g3, cv2.COLOR_GRAY2BGR), "No Green → G", 17)
show_with_matplotlib(cv2.cvtColor(r3, cv2.COLOR_GRAY2BGR), "No Green → R", 18)

plt.tight_layout()
plt.show()
