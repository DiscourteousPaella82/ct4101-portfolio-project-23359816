import cv2 as cv

def read_images(bike_pathname, mb_pathname, count, imread_flag=cv.IMREAD_GRAYSCALE):
    "Read in images.\nWill read all images if count undefined.\nDefaultly reads images as greyscale"
        
    bike_imgs = []
    mb_imgs = []

    ret_b = False
    ret_mb = False

    if count is None:
        ret_b, bike_imgs = cv.imreadmulti(mats=bike_imgs ,filename=bike_pathname, flags=imread_flag)
        ret_mb, mb_imgs = cv.imreadmulti(mats=mb_imgs, filename=mb_pathname, flags=imread_flag)
    else:
        ret_b, bike_imgs = cv.imreadmulti(mats=bike_imgs, filename=bike_pathname, count=(count / 2), flags=imread_flag)
        ret_mb, mb_imgs = cv.imreadmulti(mb_imgs=mb_imgs, filename=mb_pathname, count=(count / 2), flags=imread_flag)

    assert ret_b is not False, "Failed to read bike images"
    assert ret_mb is not False, "Failed to read motorbike images"
    
    imgs = [bike_imgs, mb_imgs]

    ttl_read_img_count = len(bike_imgs) + len(mb_imgs)
    
    print(str(bike_imgs))

    return imgs, ttl_read_img_count
