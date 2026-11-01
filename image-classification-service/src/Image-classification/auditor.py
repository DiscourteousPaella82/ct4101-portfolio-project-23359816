import numpy as np
from pandas import DataFrame as df

def flatten_dataset(data):
    data1 = []
    data1 += data[0] + data[1]

    dataset = np.asarray(data1, dtype=np.float32)
    flattened_dataset = dataset.reshape(dataset.shape[0], -1)
    return flattened_dataset

def generate_labels(data):
    size = len(data) // 2
    labels = np.zeros(size)
    labels = np.append(labels, np.ones(size))
    return labels

def inspect_dataset(dataset):
    data = df(dataset)
    df.describe(data)
    return

def normalize_dataset(dataset):
    return dataset / 255.0