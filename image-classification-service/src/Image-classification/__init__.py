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
import plot_helper as ph

datapath = sh.get_data_path()

if verbose: print("Loading data from path: " + datapath)
data = dr.read_json(datapath)

#if plot:
#    iv.view_images(data)

flattened_data = au.flatten_dataset(data)

normalized_data = au.normalize_dataset(flattened_data)

labels = au.generate_labels(normalized_data)

train, test = cl.split_dataset(normalized_data, labels)

from models import modelsDict

fitted_models, probabilities, predictions = cl.fit_models(modelsDict, test[0], test[1])


baseline_model, baseline_prob, baseline_pred = cl.fit_baseline(train[0], train[1])

test_prob, test_pred = cl.test_model(baseline_model, test[0])

cl.print_model_accuracy(baseline_model, test[0], test[1])


knn_model, knn_prob, knn_pred = cl.fit_kNN(train[0], train[1])

test_knn_prob, test_knn_pred = cl.test_model(knn_model, test[0])

cl.print_model_accuracy(knn_model, test[0], test[1], model_name="K-Nearest Neighbours")


tree_model, tree_prob, tree_pred = cl.fit_decision_tree(train[0], train[1])

test_tree_prob, test_tree_pred = cl.test_model(tree_model, test[0])

cl.print_model_accuracy(tree_model, test[0], test[1], model_name="Decision Tree")

if plot:
    print("Plotting model predictions")
    ph.plot_model(baseline_prob, baseline_pred, train[1], modelname="Logistic Regression", labelset="training", save=save, filename="Baseline_train_predictions.png") 
    print("Plotting test predictions")
    ph.plot_model(test_prob, test_pred, test[1], modelname="Logistic Regression", labelset="testing", save=save, filename="Baseline_test_predictions.png")

if plot:
    print("Plotting model predictions")
    ph.plot_model(knn_prob, knn_pred, train[1], modelname="K-Nearest Neighbours", labelset="training", save=save, filename="KNN_train_predictions.png") 
    print("Plotting test predictions")
    ph.plot_model(test_knn_prob, test_knn_pred, test[1], modelname="K-Nearest Neighbours", labelset="testing", save=save, filename="KNN_test_predictions.png")
    
if plot:
    print("Plotting model predictions")
    ph.plot_model(tree_prob, tree_pred, train[1], modelname="Decision Tree", labelset="training", save=save, filename="Tree_train_predictions.png") 
    print("Plotting test predictions")
    ph.plot_model(test_tree_prob, test_tree_pred, test[1], modelname="Decision Tree", labelset="testing", save=save, filename="Tree_test_predictions.png")