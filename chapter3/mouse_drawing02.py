import cv2
import numpy as np
import constant
image = np.zeros((600, 600, 3), dtype='uint8')
# image.fill(255)
def print_text():
    pos_1 = (10, 500)
    pos_2 = (10, 525)
    pos_3 = (10, 550)
    pos_4 = (10, 575)
    cv2.putText(image, 'Double left click: add a circle', pos_1, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Simple right click: delete last circle', pos_2, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Double right click: delete all circles', pos_3, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Press \'p\' to exit', pos_4, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
def draw_circle(event, x, y, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('event: left button double click')
        circles.append((x, y))
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print('event: right button click')
        circles[:] = []
    if event == cv2.EVENT_RBUTTONDOWN:
        print('event: right button double click')
        if circles:
            circles.pop()
        else:
            print('no circle to delete')
    if event == cv2.EVENT_MOUSEMOVE:
        print('event: Mouse move')
    if event == cv2.EVENT_LBUTTONUP:
        print('event: left button down')
    if event == cv2.EVENT_LBUTTONUP:
        print('event: left button up')
circles = []
cv2.namedWindow('Image Mouse')
cv2.setMouseCallback('Image Mouse', draw_circle)
print_text()
clone = image.copy()
while True:
    image = clone.copy()
    for pos in circles:
        cv2.circle(image, pos, 30, constant.ALL_COLORS['blue'], -1)
    cv2.imshow('Image Mouse', image)
    if cv2.waitKey(400) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()