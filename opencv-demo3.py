import cv2
import cv2 as cv
import sys
img = cv.imread('logo.png')
if img is None:
    sys.exit('Image can not be found.')
# cv.imshow('OpenCV logo', img)
# split the image
b, g, r = cv.split(img)
# merge the g, b, r into r, g, b
m_img = cv.merge([r, g, b])
import matplotlib.pyplot as plt
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(m_img)
plt.show()
k = cv.waitKeyEx(0)
cv2.destroyAllWindows()