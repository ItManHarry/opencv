import cv2 as cv
import sys
img = cv.imread(r'logo.png', cv.IMREAD_GRAYSCALE)
if img is None:
    sys.exit('Could not read the image!')
print('-' * 80)
print(img)
# shape property
dimensions = img.shape
print(dimensions)
rows = dimensions[0]
columns = dimensions[1]
# color = dimensions[2]
print(f'Width: {columns}, Height: {rows}.  Resolution: {str(rows) + " X " + str(columns)}. '
      f'Pixel: {rows*columns}.')
print('-' * 80)
size = img.size
print('Size is : ', size)
print('-' * 80)
dtype = img.dtype
print('Data type is : ', dtype)
print('-' * 80)
# some pixel channel values
i = img[6, 40]
print(f'Channel values {i}.')
top_corner = img[0:50, 0:50]
print('Top corner type is : ', type(top_corner))
# show image
cv.imshow('My Photo', img)
k = cv.waitKey(0)
print('Key is : ', k)
