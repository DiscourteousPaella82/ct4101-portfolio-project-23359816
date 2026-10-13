import os
import json
import warnings
import numpy as np

def write_output(output, pathname="./output", filename="data"):
    if os.path.exists(pathname) != True:
        warnings.warn(pathname + " doesn't exist, creating new output directory")
        os.mkdir(pathname)

    s = [[],[]]
    __convert_to_list(output, s)

    with open(pathname + "/" + filename, "w") as file:
        json.dump(s, file)

def __convert_to_list(data, res):
    for i in range(len(res)):
        __convert_to_list_helper(data[i], res, i)


def __convert_to_list_helper(data, res, index):
    if isinstance(data, np.ndarray):
        res[index].append(data.tolist())
    else:
        for j in data:
            __convert_to_list_helper(j, res, index)