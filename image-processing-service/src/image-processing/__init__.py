import setup_helper as sh
import image_reader as ir
import image_processor as ip
import image_viewer as iv

bike_img_path, mb_img_path = sh.get_image_path()

ttl_img_count = sh.get_total_image_count()

img = []
print("Attempting to read bike images from path: " + bike_img_path + " & motorbikes from path: " + mb_img_path)
imgs, read_image_count = ir.read_images(bike_pathname=bike_img_path, mb_pathname=mb_img_path, img_count=ttl_img_count)

print("Read " + str(read_image_count) + " total images.\nRead "+ str(len(imgs[0])) + " bike images.\nRead " + str(len(imgs[1])) + " motorbike images.")

normalized_images = ip.normalize_images(imgs)
