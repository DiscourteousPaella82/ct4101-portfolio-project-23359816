from matplotlib import pyplot as plt

def view_images(images, title = ""):
    rows = len(images)
    cols = len(images[0])

    for i in range(rows):
        for j in range(len(images[i])):
            plt.subplot(i + 1, cols, j + 1)
            plt.imshow(images[i][j], cmap="gray",)
            plt.xticks([]), plt.yticks([])

    plt.title(title)
    
    plt.show()