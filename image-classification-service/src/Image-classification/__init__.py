import getopt, sys

args = sys.argv[1:]
options = "vpf:"
long_options = ["Verbose", "Plot", "Filename"]

verbose = False
plot = False
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
except getopt.error as err:
    print(str(err))


import setup_helper as sh
import data_reader as dr
import image_viewer as iv

datapath = sh.get_data_path()

if verbose: print("Loading data from path: " + datapath)

data = dr.read_json(datapath)

iv.view_images(data)