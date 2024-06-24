import cv2
import numpy as np
import drawing_utils
import constant
image = np.zeros((400, 400, 3), dtype='uint8')
cv2.rectangle(image, (10, 50), (60, 300), constant.ALL_COLORS['green'], 5)
cv2.rectangle(image, (80, 50), (130, 300), constant.ALL_COLORS['red'], -1)
cv2.rectangle(image, (150, 50), (350, 100), constant.ALL_COLORS['blue'], -1)
cv2.rectangle(image, (150, 150), (350, 300), constant.ALL_COLORS['cyan'], 10)
drawing_utils.show_with_matploylib(image, 'Rectangle Shape')