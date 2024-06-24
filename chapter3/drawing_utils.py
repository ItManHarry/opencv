import matplotlib.pyplot as plt
def show_with_matploylib(img, title):
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()