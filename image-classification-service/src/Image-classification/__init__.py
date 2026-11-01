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
import auditor as au
import classifier as cl
import plot_helper as ph

datapath = sh.get_data_path()

if verbose: print("Loading data from path: " + datapath)
data = dr.read_json(datapath)

if plot:
    iv.view_images(data)

flattened_data = au.flatten_dataset(data)
labels = au.generate_labels(flattened_data)

train, test = cl.split_dataset(flattened_data, labels)

model, prob, pred = cl.fit_baseline(train[0], train[1])

test_prob, test_pred = cl.test_model(model, test[0])

cl.print_model_accuracy(model, test[0], test[1])

if plot:
    print("Plotting model predictions")
    ph.plot_model(prob, pred, train[1], save=True, filename="Baseline_train_predictions.png") 
    print("Plotting test predictions")
    ph.plot_model(test_prob, test_pred, test[1], save=True, filename="Baseline_test_predictions.png")