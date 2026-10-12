import setup_helper as sh
import image_reader as ir

bike_img_path, mb_img_path = sh.get_image_path()

ttl_img_count = sh.get_total_image_count()

img = []
print("Attempting to read bike images from path: " + bike_img_path + " & motorbikes from path: " + mb_img_path)
img, read_image_count = ir.read_images(bike_pathname=bike_img_path, mb_pathname=mb_img_path, count=ttl_img_count)

print("Read " + str(img[0]) + " bike images & " + str(img[1]) + " motorbike images")