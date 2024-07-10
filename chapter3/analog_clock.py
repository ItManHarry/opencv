import cv2
import math
import datetime
import numpy as np
import constant
import drawing_utils
def array_to_tuple(arr):
    return tuple(arr.reshape(1, -1)[0])
image = np.zeros((640, 640, 3), dtype='uint8')
image[:] = constant.ALL_COLORS['light_gray']
hours_orig = np.array([
    (620, 320),
    (580, 470),
    (470, 580),
    (320, 620),
    (170, 580),
    (60, 470),
    (20, 320),
    (60, 170),
    (169, 61),
    (319, 20),
    (469, 60),
    (579, 169),
])
hours_dest = np.array([
    (600, 320),
    (563, 460),
    (460, 562),
    (320, 600),
    (180, 563),
    (78, 460),
    (40, 320),
    (77, 180),
    (179, 78),
    (319, 40),
    (459, 77),
    (562, 179),
])
for i in range(12):
    cv2.line(image, array_to_tuple(hours_orig[i]), array_to_tuple(hours_dest[i]), constant.ALL_COLORS['black'], 3)
cv2.circle(image, (320, 320), 310, constant.ALL_COLORS['dark_gray'], 8)
cv2.rectangle(image, (150, 175), (490, 270), constant.ALL_COLORS['dark_gray'], -1)
cv2.putText(image, 'Mastering OpenCV 4', (150, 200), 1, 2, constant.ALL_COLORS['light_gray'], 1, cv2.LINE_AA)
cv2.putText(image, 'with Python', (210, 250), 1, 2, constant.ALL_COLORS['light_gray'], 1, cv2.LINE_AA)
image_original = image.copy()
while True:
    date_time_now = datetime.datetime.now()
    time_now = date_time_now.time()
    hour = math.fmod(time_now.hour, 12)
    minute = time_now.minute
    second = time_now.second
    print(f'Time now -> {int(hour)}: {minute}: {second}')
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod(hour * 30 + minute / 2 + 270, 360)
    second_x = round(320 + 310 * math.cos(second_angle * 3.14 / 180))
    second_y = round(320 + 310 * math.sin(second_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (second_x, second_y), constant.ALL_COLORS['blue'], 2)
    minute_x = round(320 + 260 * math.cos(minute_angle * 3.14 / 180))
    minute_y = round(320 + 260 * math.sin(minute_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (minute_x, minute_y), constant.ALL_COLORS['blue'], 8)
    hour_x = round(320 + 220 * math.cos(hour_angle * 3.14 / 180))
    hour_y = round(320 + 220 * math.sin(hour_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (hour_x, hour_y), constant.ALL_COLORS['blue'], 10)
    cv2.circle(image, (320, 320), 10, constant.ALL_COLORS['dark_gray'], -1)
    cv2.imshow('Analog Clock', image)
    image = image_original.copy()
    # drawing_utils.show_with_matploylib(image, 'Analog Clock')
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()