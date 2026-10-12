import os
import warnings

def get_image_path(img_path_env_name = "IMAGES_PATH"):
    ""
    img_path = os.getenv(img_path_env_name)
    assert img_path is not None, "IMAGES_PATH could not be read, make sure to set IMAGES_PATH environment variable"

    bike_img_path = img_path + "/bike"
    mb_img_path = img_path + "/motorbike"

    return bike_img_path, mb_img_path

def get_total_image_count(ttl_img_count_env_name = "TOTAL_IMAGES_COUNT"):
    ttl_img_count = os.getenv(ttl_img_count_env_name)
    if ttl_img_count is None:
        warnings.warn("TOTAL_IMAGES_COUNT not set, reading all images")
    else:
        ttl_img_count = int(ttl_img_count)
        assert ttl_img_count != 0, "Set TOTAL_IMAGES_COUNT to none zero even integer"

        if ttl_img_count % 2 != 0:
            ttl_img_count = ttl_img_count + 1

    return ttl_img_count