from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

# TODO ADD HYPERPARAMATERS FOR nearest neighbours/thresholds etc

modelsDict = {
    "logistic regression": {"function": LogisticRegression(C=1.0, max_iter=1000, random_state=42), "name": "Logistic Regression"},
    "knn": {"function": KNeighborsClassifier(n_neighbors=7, weights="distance", metric="minkowski"), "name": "K-Nearest Neighbour"},
    "decision tree": {"function": DecisionTreeClassifier(max_depth=4, min_samples_leaf=10, random_state=42), "name": "Decision Tree"},
    "mlp": {"function": MLPClassifier(hidden_layer_sizes=(64, 32), activation="relu", solver="adam", alpha=1e-4, early_stopping=True,max_iter=500, random_state=42), "name": "Multilayer Perceptron"}
}