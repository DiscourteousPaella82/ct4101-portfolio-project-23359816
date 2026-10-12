import getopt, sys

args = sys.argv[1:]
options = "vpo:"
long_options = ["Verbose", "Plot", "Output="]

verbose = False
plot = False
output = "."

try:
    arguments, values = getopt.getopt(args, options, long_options)
    for currentArg, currentVal in arguments:
        if currentArg in ("-v", "--Verbose"):
            verbose = True
        elif currentArg in ("-p", "--Plot"):
            verbose = True
        elif currentArg in ("-o", "--Output"):
            print("Output directory:", currentVal)
except getopt.error as err:
    print(str(err))

import setup_helper as sh
import image_reader as ir
import image_processor as ip
import image_viewer as iv

bike_img_path, mb_img_path = sh.get_image_path()

ttl_img_count = sh.get_total_image_count()

img = []

if verbose: print("Attempting to read bike images from path: " + bike_img_path + " & motorbikes from path: " + mb_img_path)

imgs, read_image_count = ir.read_images(bike_pathname=bike_img_path, mb_pathname=mb_img_path, img_count=ttl_img_count)

if verbose: print("Read " + str(read_image_count) + " total images.\nRead "+ str(len(imgs[0])) + " bike images.\nRead " + str(len(imgs[1])) + " motorbike images.")

normalized_images = ip.normalize_images(imgs)

if plot: iv.view_images(normalized_images, "Normalized images")

thresholded_images = ip.threshold_images(normalized_images)

if plot: iv.view_images(thresholded_images, "Thresholded images")

resized_images = ip.resize_images(thresholded_images)

if plot: iv.view_images(resized_images, "Resized images")