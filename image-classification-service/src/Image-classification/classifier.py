from sklearn.model_selection import StratifiedKFold

def split_dataset(data, labels):
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    train, test = cv.split(data, labels)
    return train, test