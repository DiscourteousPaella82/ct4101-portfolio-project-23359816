from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline

# TODO ADD HYPERPARAMATERS FOR nearest neighbours/thresholds etc

def split_dataset(data, labels):
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42, stratify=labels,)
    return (train_data, train_labels), (test_data, test_labels)

def fit_models(models, data, labels):
    fitted_models =  []
    probabilities = []
    predictions = []

    for model_func in models:
        model = make_pipeline(
            models.get(model_func)
        )
        model.fit(data, labels)
        prob = model.predict_proba(data)[:, 1]
        pred = ((prob > 0.5).astype(int))

        fitted_models.append(model)
        probabilities.append(prob)
        predictions.append(pred)

    return fitted_models, probabilities, predictions

def fit_baseline(data, labels):
    model = make_pipeline(
        LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    )
    model.fit(data, labels)
    prob = model.predict_proba(data)[:, 1]
    pred = ((prob > 0.5).astype(int))

    return model, prob, pred

def fit_kNN(data, labels):
    model = make_pipeline(
        KNeighborsClassifier(n_neighbors=7, weights="distance", metric="minkowski")
    )
    model.fit(data, labels)
    prob = model.predict_proba(data)[:, 1]
    pred = ((prob > 0.5).astype(int))

    return model, prob, pred

def fit_decision_tree(data, labels):
    model = make_pipeline(
        DecisionTreeClassifier(max_depth=4, min_samples_leaf=10, random_state=42)
    )
    model.fit(data, labels)
    prob = model.predict_proba(data)[:, 1]
    pred = ((prob > 0.5).astype(int))

    return model, prob, pred

def fit_cnn(data, labels):
    model = make_pipeline(
        MLPClassifier(max_depth=4, min_samples_leaf=10, random_state=42)
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