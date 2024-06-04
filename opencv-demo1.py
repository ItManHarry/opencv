import cv2 as cv
import sys
img = cv.imread(r'E:\Images\CGQ.jpg')
if img is None:
    sys.exit('Could not read the image!')
print('-' * 80)
print(img)
# shape property
dimensions = img.shape
print(dimensions)
rows = dimensions[0]
columns = dimensions[1]
color = dimensions[2]
print(f'Width: {columns}, Height: {rows}.  Resolution: {str(rows) + " X " + str(columns)}. '
      f'Pixel: {rows*columns}. Channels: {color}')
if color:
    print('It is a colorful image!')
else:
    print('It is a gray image!')
print('-' * 80)
size = img.size
print('Size is : ', size)
print('-' * 80)
dtype = img.dtype
print('Data type is : ', dtype)
print('-' * 80)
# some pixel channel values
b, g, r = img[6, 40]
print(f'Channel values are , Blue {b}, Green {g}, Red {r}.')
b, g, r = img[480, 40]
print(f'Channel values are , Blue {b}, Green {g}, Red {r}.')
print(f'Channel values are , Blue {img[480, 40, 0]}, Green {img[480, 40, 1]}, Red {img[480, 40, 2]}.')
print('-' * 80)
# set channel values
img[10, 30] = (0, 0, 255)
top_corner = img[0:50, 0:50]
print('Top corner type is : ', type(top_corner))
# show image
cv.imshow('My Photo', img)
k = cv.waitKey(0)
print('Key is : ', k)
