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

def resize_images(images, size=(224,224)):
    resized_images = [[],[]]

    for i in range(len(images)):
        for image in images[i]:
            resized_image = cv.resize(image, size, dst=None, fx=None, fy=None, interpolation=cv.INTER_LINEAR)
            resized_images[i].append(resized_image)

    return resized_images

def laplacian_images(images):
    processed_images = [[], []]

    for i in range(len(images)):
        for image in images[i]:
            processed_image = cv.Laplacian(image, cv.CV_64F)
            processed_images[i].append(processed_image)

    return processed_images