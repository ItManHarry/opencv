import drawing_utils
import numpy as np
import cv2
import constant
image = np.zeros((400, 400, 3), dtype='uint8')
cv2.line(image, (0, 0), (400, 400), constant.ALL_COLORS['green'], 3)
cv2.line(image, (0, 400), (400, 0), constant.ALL_COLORS['blue'], 3)
cv2.line(image, (200, 0), (200, 400), constant.ALL_COLORS['red'], 10)
cv2.line(image, (0, 200), (400, 200), constant.ALL_COLORS['yellow'], 10)
drawing_utils.show_with_matploylib(image, 'Canvas Show')