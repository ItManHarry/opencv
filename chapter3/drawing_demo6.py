import numpy as np
import cv2
import drawing_utils
import constant
image = np.zeros((300, 300, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
cv2.ellipse(image, (80, 80), (60, 40), 0, 0, 360, constant.ALL_COLORS['red'], -1)
cv2.ellipse(image, (80, 200), (80, 40), 0, 0, 360, constant.ALL_COLORS['green'], 3)
cv2.ellipse(image, (80, 200), (10, 40), 0, 0, 360, constant.ALL_COLORS['blue'], 3)
cv2.ellipse(image, (200, 200), (10, 40), 0, 0, 180, constant.ALL_COLORS['yellow'], 3)
cv2.ellipse(image, (200, 100), (10, 40), 0, 0, 270, constant.ALL_COLORS['cyan'], 3)
cv2.ellipse(image, (250, 250), (30, 30), 0, 0, 360, constant.ALL_COLORS['magenta'], 3)
cv2.ellipse(image, (250, 100), (20, 40), 45, 0, 360, constant.ALL_COLORS['gray'], 3)
drawing_utils.show_with_matploylib(image, 'Ellipse')