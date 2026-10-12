import cv2 as cv

def read_images(bike_pathname, mb_pathname, count, imread_flag=cv.IMREAD_GRAYSCALE):
    "Read in images.\nWill read all images if count undefined.\nDefaultly reads images as greyscale"
        
    bike_imgs = []
    mb_imgs = []

    if count is None:
        bike_imgs = cv.imreadmulti(filename=bike_pathname, flags=imread_flag)
        mb_imgs = cv.imreadmulti(filename=mb_pathname, flags=imread_flag)
    else:
        bike_imgs = cv.imreadmulti(filename=bike_pathname, count=(count / 2), flags=imread_flag)
        mb_imgs = cv.imreadmulti(filename=mb_pathname, count=(count / 2), flags=imread_flag)

    imgs = [bike_imgs, mb_imgs]

    ttl_read_img_count = len(bike_imgs) + len(mb_imgs)
    return imgs, ttl_read_img_count
