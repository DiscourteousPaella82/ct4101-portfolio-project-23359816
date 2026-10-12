import cv2 as cv
import os
import warnings

def read_images_dir(pathname, count, imread_flag):
    "Reads all images in given path"

    images = []

    no_files = len(os.listdir(pathname))
    count_read_failed = 0

    if no_files != 0:
        if count is not None:
            i = 0
            for (_, _, files) in os.walk(pathname):
                for file in files:
                    try:
                        if (i == count):
                            break

                        filename = pathname + "/" + file

                        image = cv.imread(filename, imread_flag)
                        images.append(image)
                    except:
                        count_read_failed += 1
                        warnings.warn("Failed to read file: " + file)
                    finally:
                        i += 1
        else:
            for (_, _, files) in os.walk(pathname):
                for file in files:
                    try:
                        filename = pathname + "/" + file
                    
                        image = cv.imread(filename, imread_flag)
                                           
                        images.append(image)
                    except:
                        count_read_failed += 1
                        warnings.warn("Failed to read file: " + file)

    else:
        warnings.warn("No files to be read in " + pathname)

    if count_read_failed != 0:
        warnings.warn("Failed to read " + count_read_failed + " files")

    return images

def read_images(bike_pathname, mb_pathname, img_count, imread_flag=cv.IMREAD_GRAYSCALE):
    "Read in images.\nWill read all images if count undefined.\nDefaultly reads images as greyscale"
        
    bike_imgs = []
    mb_imgs = []

    if img_count is None:
        bike_imgs = read_images_dir(pathname=bike_pathname, count=None, imread_flag=imread_flag)
        mb_imgs = read_images_dir(pathname=mb_pathname, count=None, imread_flag=imread_flag)
    else:
        bike_imgs = read_images_dir(pathname=bike_pathname, count=(img_count/2), imread_flag=imread_flag)
        mb_imgs = read_images_dir(pathname=mb_pathname, count=(img_count/2), imread_flag=imread_flag)

    ttl_read_img_count = len(bike_imgs) + len(mb_imgs)

    imgs = [bike_imgs, mb_imgs]

    return imgs, ttl_read_img_count
