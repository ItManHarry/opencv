import numpy as np
import cv2
import constant
import drawing_utils
image = np.zeros((120, 512, 3), dtype='uint8')
image.fill(255)
cv2.putText(image, 'Mastering OpenCV with Python!!!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, constant.ALL_COLORS['red'], 2, cv2.LINE_4)
cv2.putText(image, 'Mastering OpenCV with Python!!!', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, constant.ALL_COLORS['red'], 2, cv2.LINE_AA)
cv2.putText(image, 'Mastering OpenCV with Python!!!', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, constant.ALL_COLORS['red'], 2, cv2.LINE_8)
drawing_utils.show_with_matploylib(image, 'Text')