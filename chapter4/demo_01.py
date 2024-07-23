import matplotlib.pyplot as plt
import cv2
import utils
img = cv2.imread(r'color_spaces.png')
plt.figure(figsize=(13, 5))
plt.suptitle('Splitting and merging channels in OpenCV', fontsize=6, fontweight='bold')
utils.show_with_matplotlib(img, 'BGR-image', 1)
b, g, r = cv2.split(img)
utils.show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), 'BGR-(B)', 2)
utils.show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), 'BGR-(G)', 2+6)
utils.show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), 'BGR-(R)', 2+6*2)
# RGB image
img_copy = cv2.merge((b, g, r))
utils.show_with_matplotlib(img_copy, 'BGR - image(copy)', 1+6)
b_copy = img[:, :, 0]
img_without_blue = img.copy()
img_without_blue[:, :, 0] = 0
img_without_green = img.copy()
img_without_green[:, :, 1] = 0
img_without_red = img.copy()
img_without_red[:, :, 2] = 0
utils.show_with_matplotlib(img_without_blue, 'BGR without B', 3)
utils.show_with_matplotlib(img_without_green, 'BGR without G', 3+6)
utils.show_with_matplotlib(img_without_red, 'BGR without R', 3+6*2)
images = {'B': img_without_blue, 'G': img_without_green, 'R': img_without_red}
index = 4
for k, image in images.items():
    b, g, r = cv2.split(image)
    utils.show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), f'BGR without {k} (B)', index)
    utils.show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), f'BGR without {k} (G)', index+6)
    utils.show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), f'BGR without {k} (R)', index+6*2)
    index += 1
plt.show()