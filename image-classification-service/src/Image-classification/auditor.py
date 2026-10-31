from pandas import DataFrame as df

def inspect_dataset(dataset):
    data = df(dataset)
    print(df.describe(data))