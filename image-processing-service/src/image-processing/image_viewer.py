from matplotlib import pyplot as plt

def view_images(images):
    rows = len(images)
    cols = len(images[0])

    print("ROWS = " + str(rows) + " COLS = " + str(cols) + "\n\n" + str(images))

    for i in range(rows):
        for j in range(cols):
            plt.subplot(rows, cols, j + 1)
            plt.imshow(images[i][j])

    plt.show()