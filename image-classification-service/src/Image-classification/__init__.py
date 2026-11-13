import getopt, sys

args = sys.argv[1:]
options = "vpsf:"
long_options = ["Verbose", "Plot", "Save", "Filename="]

verbose = False
plot = False
filename = None
save = False

try:
    arguments, values = getopt.getopt(args, options, long_options)
    for currentArg, currentVal in arguments:
        if currentArg in ("-v", "--Verbose"):
            verbose = True
        elif currentArg in ("-p", "--Plot"):
            plot = True
        elif currentArg in ("-s", "--Save"):
            save = True
        elif currentArg in ("-f", "--Filename"):
            filename = currentVal
except getopt.error as err:
    print(str(err))


import setup_helper as sh
import data_reader as dr
import image_viewer as iv
import auditor as au
import classifier as cl
import metrics as mt
import plot_helper as ph

datapath = sh.get_data_path()

if verbose: print("Loading data from path: " + datapath)
data = dr.read_json(datapath)

flattened_data = au.flatten_dataset(data)

normalized_data = au.normalize_dataset(flattened_data)

labels = au.generate_labels(normalized_data)

train, test = cl.split_dataset(normalized_data, labels)

from models import modelsDict

names = []
for value in modelsDict.values(): names.append(value["name"])

fitted_models, probabilities, predictions = cl.fit_models(modelsDict, train[0], train[1])

test_probabilities, test_predictions = mt.test_models(fitted_models, test[0])

evaluation_results = []

evaluation_results = mt.evaluate_models(fitted_models, test[0], test_predictions, test[1])

labelnames = ["training", "testing"]
labelsource = [train[1], test[1]]

probs = [probabilities, test_probabilities]
preds = [predictions, test_predictions]

if plot:
    ph.plot_models_predictions(names, probs, preds, labelsource, labelnames, save=save, show=False, verbose=verbose)
    ph.plot_models_metrics(names, evaluation_results, save=save, show=False, verbose=verbose)