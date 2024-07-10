import numpy as np
import cv2
import constant
import matplotlib.pylab as plt
image = np.zeros((400, 400, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
figure = plt.figure()
figure.add_subplot(111)
def update_img_with_matplotlib():
    img_RGB = image[:, :, ::-1]
    plt.imshow(img_RGB)
    figure.canvas.draw()
def click_mouse_event(event):
    print(f'Center {int(round(event.xdata))}, {int(round(event.ydata))}')
    cv2.circle(image, (int(round(event.xdata)), int(round(event.ydata))), 30, constant.ALL_COLORS['blue'], cv2.FILLED)
    update_img_with_matplotlib()
update_img_with_matplotlib()
figure.canvas.mpl_connect('button_press_event', click_mouse_event)
plt.show()