import cv2 as cv

def normalize_images(images):
    normalized_images = [[], []]

    for i in range(len(images)):
        for image in images[i]:
            normalized_image = cv.normalize(image, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
            normalized_images[i].append(normalized_image)

    return normalized_images

def threshold_images(images, threshold=100):
    thresholded_images = [[],[]]

    for i in range(len(images)):
        for image in images[i]:
            _, thresholded_image = cv.threshold(image, threshold, 255, cv.THRESH_BINARY)
            thresholded_images[i].append(thresholded_image)

    return thresholded_images