import cv2 as cv

def normalize_images(images):
    normalized_images = [[], []]

    for i in range(len(images)):
        for image in images[i]:
            normalized_image = cv.normalize(image, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
            normalized_images[i].append(normalized_image)

    return normalized_images