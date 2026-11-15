import getopt, sys

args = sys.argv[1:]
options = "vpsdo:"
long_options = ["Verbose", "Plot", "Save", "Display","Output="]

verbose = False
plot = False
display = False
output_dir = None
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
        elif currentArg in ("-d", "--Display"):
            display = True
        elif currentArg in ("-o", "--Output"):
            output_dir = currentVal
            print("Output directory:", currentVal)
except getopt.error as err:
    print(str(err))

if output_dir is None: output_dir="./output/graphs"

import setup_helper as sh
import data_reader as dr
import auditor as au
import classifier as cl
import metrics as mt
import plot_helper as ph

datapath = sh.get_data_path()

if verbose: print("Loading data from path: " + datapath)
data = dr.read_json(datapath)

flattened_data = au.flatten_dataset(data)
if verbose: print(f"{len(flattened_data)} samples detected")

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
    ph.plot_models_predictions(names, probs, preds, labelsource, labelnames, save=save, show=display, verbose=verbose, output=output_dir)
    ph.plot_models_metrics(names, evaluation_results, save=save, show=display, verbose=verbose, output=output_dir)