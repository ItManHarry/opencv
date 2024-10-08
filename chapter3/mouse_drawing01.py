import numpy as np
import cv2
import constant
image = np.zeros((600, 600, 3), dtype='uint8')
image.fill(255)
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), 10, constant.ALL_COLORS['magenta'], -1)
    if event == cv2.EVENT_MOUSEMOVE:
        print(f'Mouse move ({x}: {y})')
    if event == cv2.EVENT_LBUTTONUP:
        print('Left button up...')
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Button down...')
cv2.namedWindow('Image mouse')
cv2.setMouseCallback('Image mouse', draw_circle)
while True:
    cv2.imshow('Image mouse', image)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()