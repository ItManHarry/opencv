import cv2 as cv
o_img = cv.imread(r'logo.png')
b, g, r = cv.split(o_img)
m_img = cv.merge([r, g, b])
cv.imshow('Origin Image', o_img)
cv.imshow('ReMaged Image', m_img)
cv.waitKey(0)
cv.destroyWindow()