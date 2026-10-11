import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

img_path = os.getenv("IMAGES_PATH")
assert img_path is not None, "IMAGES_PATH could not be read, make sure to set IMAGES_PATH environment variable"

bike_img_path = img_path + "/bike"
mb_img_path = img_path + "/motorbike"

bike_imgs = cv.imreadmulti(bike_img_path)
mb_imgs = cv.imreadmulti(mb_img_path)

plt.figure(figsize=(10,8))
plt.subplot(8, 4)

for i in range(8):
    plt.imshow(bike_imgs[i])
    plt.xticks([]), plt.yticks([])

for i in range(8):
    plt.imshow(mb_imgs[i])
    plt.xticks([]), plt.yticks([])

plt.show()