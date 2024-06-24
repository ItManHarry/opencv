import cv2
import numpy as np
import constant
import drawing_utils
image = np.zeros((500, 500, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
separation = 40
for key in constant.ALL_COLORS:
    cv2.line(image, (0, separation), (500, separation), constant.ALL_COLORS[key], 10)
    separation += 40
drawing_utils.show_with_matploylib(image, 'Dictionary with some predefined colors')