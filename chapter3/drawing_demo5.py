import numpy as np
import cv2
import constant
import drawing_utils
image = np.zeros((300, 300, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
cv2.line(image, (0, 0), (300, 300), constant.ALL_COLORS['green'], 3)
cv2.rectangle(image, (0, 0), (100, 100), constant.ALL_COLORS['blue'], 3)
ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (300, 300))
if ret:
    cv2.line(image, p1, p2, constant.ALL_COLORS['yellow'], 3)
drawing_utils.show_with_matploylib(image, 'Advanced Image - ClipLine')
image2 = np.zeros((300, 300, 3), dtype='uint8')
image2[:] = constant.ALL_COLORS['dark_gray']
cv2.arrowedLine(image2, (50, 50), (200, 50), constant.ALL_COLORS['red'], 3, 8, 0, 0.1)
cv2.arrowedLine(image2, (50, 120), (200, 120), constant.ALL_COLORS['green'], 3, cv2.LINE_AA, 0, 0.3)
cv2.arrowedLine(image2, (50, 200), (200, 200), constant.ALL_COLORS['blue'], 3, 8, 0, 0.3)
drawing_utils.show_with_matploylib(image2, 'Advanced Image - Arrowed Line')