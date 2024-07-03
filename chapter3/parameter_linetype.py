import numpy as np
import cv2
import constant
import drawing_utils
image = np.zeros((20, 20, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
cv2.line(image, (5, 0), (20, 15), constant.ALL_COLORS['red'], 1, cv2.LINE_4)
cv2.line(image, (0, 0), (20, 20), constant.ALL_COLORS['blue'], 1, cv2.LINE_AA)
cv2.line(image, (0, 5), (15, 20), constant.ALL_COLORS['yellow'], 1, cv2.LINE_8)
drawing_utils.show_with_matploylib(image, 'LINE_4 LINE_AA LINE_8')