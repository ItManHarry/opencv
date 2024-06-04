import cv2 as cv
import sys
img = cv.imread(r'E:\Images\CGQ.jpg')
if img is None:
    sys.exit('Could not read the image!')
print('-' * 80)
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
# show image
cv.imshow('My Photo', img)
k = cv.waitKey(0)
print('Key is : ', k)
