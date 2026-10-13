import getopt, sys
import os

args = sys.argv[1:]
options = "vcpfo:"
long_options = ["Verbose", "Plot", "Filename=","Output="]

verbose = False
plot = False
output_dir = None
filename = None

try:
    arguments, values = getopt.getopt(args, options, long_options)
    for currentArg, currentVal in arguments:
        if currentArg in ("-v", "--Verbose"):
            verbose = True
        elif currentArg in ("-p", "--Plot"):
            plot = True
        elif currentArg in ("-f", "--Filename"):
            filename = currentVal
        elif currentArg in ("-o", "--Output"):
            output_dir = currentVal
            print("Output directory:", currentVal)
except getopt.error as err:
    print(str(err))

import setup_helper as sh
import image_reader as ir
import image_processor as ip
import image_viewer as iv
import output_helper as oh

bike_img_path, mb_img_path = sh.get_image_path()

ttl_img_count = sh.get_total_image_count()

img = []

if verbose: print("Attempting to read bike images from path: " + bike_img_path + " & motorbikes from path: " + mb_img_path)

imgs, read_image_count = ir.read_images(bike_pathname=bike_img_path, mb_pathname=mb_img_path, img_count=ttl_img_count)

if verbose: print("Read " + str(read_image_count) + " total images.\nRead "+ str(len(imgs[0])) + " bike images.\nRead " + str(len(imgs[1])) + " motorbike images.")

if verbose: print("Resizing images")

resized_images = ip.resize_images(imgs)

if plot: iv.view_images(resized_images, "Resized images")

if verbose: print("Normalising images")

normalized_images = ip.normalize_images(resized_images)

if plot: iv.view_images(normalized_images, "Normalized images")

if verbose: print("Thresholding images")

thresholded_images = ip.threshold_images(normalized_images)

if plot: iv.view_images(thresholded_images, "Thresholded images")

if verbose: 
    if None not in (output_dir, filename): print("Writing data to " + output_dir + "/" + filename)
    else: print("Writing data to " + str(os.getcwd()) + "/output/data.json")

oh.write_output(thresholded_images, filename, pathname=output_dir)