from sklearn.model_selection import StratifiedKFold, cross_validate

def split_dataset():
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
 
    res = cross_validate(model, X, y, cv=cv,scoring={"f1":"f1", "roc_auc":"roc_auc"},
                         return_train_score=True)

    print(res["test_f1"].mean(), res["test_f1"].std())
    return res