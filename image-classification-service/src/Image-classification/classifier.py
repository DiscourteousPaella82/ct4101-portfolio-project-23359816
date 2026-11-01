from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

def split_dataset(data, labels):
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42, stratify=labels,)
    return (train_data, train_labels), (test_data, test_labels)


def fit_baseline(data, labels):
    model = make_pipeline(
        LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    )
    model.fit(data, labels)
    prob = model.predict_proba(data)[:, 1]
    pred = ((prob > 0.5).astype(int))

    return model, prob, pred

def test_model(model, test_data):
    prob = model.predict_proba(test_data)[:, 1]
    pred = ((prob > 0.5).astype(int))
    return prob, pred

def print_model_accuracy(model, test_data, test_labels, model_name="Baseline"):
    accuracy = model.score(test_data, test_labels)
    print(f"{model_name} model accuracy: {accuracy}")