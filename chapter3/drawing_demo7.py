import numpy as np
import cv2
import drawing_utils
import constant
image = np.zeros((400, 400, 3), dtype='uint8')
pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
pts = pts.reshape(-1, 1, 2)
cv2.polylines(image, [pts], True, constant.ALL_COLORS['green'], 3)
drawing_utils.show_with_matploylib(image, 'Polygons')