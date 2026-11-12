from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

def split_dataset(data, labels):
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42, stratify=labels,)
    return (train_data, train_labels), (test_data, test_labels)

def fit_models(models, data, labels):
    fitted_models =  []
    probabilities = []
    predictions = []

    for mdl in models.values():
        model = make_pipeline(
            mdl["function"]
        )
        model.fit(data, labels)
        prob = model.predict_proba(data)[:, 1]
        pred = ((prob > 0.5).astype(int))

        fitted_models.append(model)
        probabilities.append(prob)
        predictions.append(pred)

    return fitted_models, probabilities, predictions

def test_models(models, test_data):
    probs = []
    preds = []
    
    for model in models:
        prob = model.predict_proba(test_data)[:, 1]
        pred = ((prob > 0.5).astype(int))

        probs.append(prob)
        preds.append(pred)
        
    return probs, preds

def print_models_accuracy(models, test_data, test_labels, names):
    for i in range(len(models)):
        accuracy = models[i].score(test_data, test_labels)
        print(f"{names[i]} model accuracy: {accuracy}")