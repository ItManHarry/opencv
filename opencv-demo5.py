import cv2 as cv
import numpy as np
o_img = cv.imread(r'logo.png')
# split
b, g, r = cv.split(o_img)
# merge
m_img = cv.merge([r, g, b])
# concatenate
c_img = np.concatenate((o_img, m_img), axis=1)
# show merged image
cv.imshow('Merged Image', c_img)
cv.waitKey(0)
cv.destroyAllWindows()
# save image
cv.imwrite('merged_logo.png', c_img)
