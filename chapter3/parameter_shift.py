import numpy as np
import cv2
import constant
import drawing_utils
'''
The shift parameter allows you to specify the number of the fractional bits
(on the right of the decimal point). In the end, the real point coordinates are calculated
as follows:
'''
def draw_float_circle(img, center, radius, color, thickness=1, lineType=8, shift=4):
    factor = 2 ** shift
    center = (int(round(center[0] * factor)), int(round(center[1] * factor)))
    radius = int(round(radius * factor))
    cv2.circle(img, center, radius, color, thickness, lineType, shift)
image = np.zeros((800, 800, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
draw_float_circle(image, (199, 199), 200, constant.ALL_COLORS['red'], shift=0)
draw_float_circle(image, (199.9, 199.9), 200, constant.ALL_COLORS['green'], shift=1)
draw_float_circle(image, (199.9, 199.9), 200, constant.ALL_COLORS['blue'], shift=2)
draw_float_circle(image, (199.9, 199.9), 200, constant.ALL_COLORS['yellow'], shift=3)
draw_float_circle(image, (199.9, 599.9), 200, constant.ALL_COLORS['blue'], shift=3)
draw_float_circle(image, (599.9, 199.9), 200, constant.ALL_COLORS['red'], shift=3)
draw_float_circle(image, (599.9, 599.9), 200, constant.ALL_COLORS['magenta'], shift=3)
drawing_utils.show_with_matploylib(image, 'Shift parameter!!!')