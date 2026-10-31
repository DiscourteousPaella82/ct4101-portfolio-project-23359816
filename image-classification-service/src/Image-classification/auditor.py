import numpy as np
from pandas import DataFrame as df

def flatten_dataset(dataset):
    flattened_dataset = []
    flattened_dataset += dataset[0] + dataset[1]
    return flatten_dataset

def inspect_dataset(dataset):
    data = df(dataset)
    print(df.describe(data))