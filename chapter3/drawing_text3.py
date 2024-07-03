import numpy as np
import cv2
import constant
import drawing_utils
image = np.zeros((400, 1200, 3), dtype='uint8')
image.fill(255)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
thickness = 5
text = 'abcdefghijklmnopqrstuvwxyz'
circle_radius = 10
ret, baseline = cv2.getTextSize(text, font, font_scale, thickness)
text_width, text_height = ret
text_x = int(round(image.shape[1]-text_width) / 2)
text_y = int(round(image.shape[0]-text_height) / 2)
cv2.circle(image, (text_x, text_y), circle_radius, constant.ALL_COLORS['green'], -1)
cv2.rectangle(image, (text_x, text_y+baseline), (text_x+text_width-thickness, text_y-text_height), constant.ALL_COLORS['blue'], thickness)
cv2.circle(image, (text_x, text_y+baseline), circle_radius, constant.ALL_COLORS['red'], -1)
cv2.circle(image, (text_x+text_width-thickness, text_y-text_height), circle_radius, constant.ALL_COLORS['cyan'], -1)
cv2.line(image, (text_x, text_y+int(round(thickness/2))), (text_x+text_width-thickness, text_y+int(round(thickness/2))), constant.ALL_COLORS['yellow'], thickness)
cv2.putText(image, text, (text_x, text_y), font, font_scale, constant.ALL_COLORS['magenta'],thickness)
drawing_utils.show_with_matploylib(image, 'Text Functions')