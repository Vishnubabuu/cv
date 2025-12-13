import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_with_matplotlib(img, title):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

colors = {
    'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255),
    'yellow': (0, 255, 255), 'magenta': (255, 0, 255), 'cyan': (255, 255, 0),
    'white': (255, 255, 255), 'black': (0, 0, 0), 'gray': (125, 125, 125),
    'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
    'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)
}

# Create gray background image
image = np.zeros((400, 1200, 3), dtype='uint8')
image[:] = colors['gray']

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
thickness = 5
text = "abcdefghijklmnopqrstuvwxyz"
circle_radius = 10

# Get text size and baseline
(ret, baseline) = cv2.getTextSize(text, font, font_scale, thickness)
text_width, text_height = ret

# Center text properly
text_x = int((image.shape[1] - text_width) / 2)
text_y = int((image.shape[0] + text_height) / 2)  # ✅ FIXED (should use height, not width)

# Draw reference points and shapes
cv2.circle(image, (text_x, text_y), circle_radius, colors['green'], -1)
cv2.rectangle(image, (text_x, text_y + baseline),
              (text_x + text_width - thickness, text_y - text_height),
              colors['blue'], thickness)
cv2.circle(image, (text_x, text_y + baseline), circle_radius, colors['red'], -1)
cv2.circle(image, (text_x + text_width - thickness, text_y - text_height),
           circle_radius, colors['cyan'], -1)
cv2.line(image, (text_x, text_y + int(round(thickness / 2))),
         (text_x + text_width - thickness, text_y + int(round(thickness / 2))),
         colors['yellow'], thickness)

# Put text
cv2.putText(image, text, (text_x, text_y), font, font_scale, colors['magenta'], thickness)

# Show the image using matplotlib (RGB corrected)
show_with_matplotlib(image, 'cv2.getTextSize() + cv2.putText()')
