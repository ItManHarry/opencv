import cv2
import constant
import numpy as np
import drawing_utils
image = np.zeros((400, 400, 3), dtype='uint8')
cv2.circle(image, (50, 50), 20, constant.ALL_COLORS['green'], 1)
cv2.circle(image, (100, 100), 30, constant.ALL_COLORS['blue'], -1)
cv2.circle(image, (200, 200), 40, constant.ALL_COLORS['magenta'], 10)
cv2.circle(image, (300, 300), 40, constant.ALL_COLORS['cyan'], -1)
drawing_utils.show_with_matploylib(image, 'Circle Drawing')