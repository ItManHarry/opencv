import matplotlib.pyplot as plt
import cv2
def show_with_matplotlib(img, title, pos):
    img_RGB = img[:, :, ::-1]
    plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')