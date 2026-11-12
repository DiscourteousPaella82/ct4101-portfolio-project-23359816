from sklearn.metrics import precision_score, recall_score, roc_auc_score

def test_models(models, test_data):
    probs = []
    preds = []
    
    for model in models:
        prob = model.predict_proba(test_data)[:, 1]
        pred = ((prob > 0.5).astype(int))

        probs.append(prob)
        preds.append(pred)
        
    return probs, preds

def evaluate_models(models, test_data, test_predictions, test_labels):
    scores = [] 

    for i in range(len(models)):
        scores.append({"accuracy":0, "precision":0, "recall":0, "roc_auc":0})
        scores[i]["accuracy"]=models[i].score(test_data, test_labels)
        scores[i]["precision"]=precision_score(test_labels, test_predictions[i], average="weighted")
        scores[i]["recall"]=recall_score(test_labels, test_predictions[i], average="weighted")
        scores[i]["roc_auc"]=roc_auc_score(test_labels, test_predictions[i])

    return scores