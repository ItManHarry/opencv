import numpy as np
import cv2
import constant
import drawing_utils
image = np.zeros((650, 650, 3), dtype='uint8')
image.fill(255)
fonts = {
    0: 'FONT HERSHEY SIMPLEX',
    1: 'FONT HERSHEY PLAIN',
    2: 'FONT HERSHEY DUPLEX',
    3: 'FONT HERSHEY COMPLEX',
    4: 'FONT HERSHEY TRIPLEX',
    5: 'FONT HERSHEY COMPLEX SMALL',
    6: 'FONT HERSHEY SCRIPT SIMPLEX',
    7: 'FONT HERSHEY SCRIPT COMPLEX',
}
colors = {
    0: 'blue',
    1: 'green',
    2: 'red',
    3: 'yellow',
    4: 'magenta',
    5: 'cyan',
    6: 'black',
    7: 'dark_gray',
}
position = (10, 30)
for key, value in colors.items():
    print(f'Key is {key}, value {value}')
    cv2.putText(image, fonts[key], position, key, 1.1, constant.ALL_COLORS[value], 2, cv2.LINE_4)
    position = (position[0], position[1]+40)
    cv2.putText(image, fonts[key].lower(), position, key, 1.1, constant.ALL_COLORS[value], 2, cv2.LINE_4)
    position = (position[0], position[1] + 40)
drawing_utils.show_with_matploylib(image, 'All Fonts')