from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

modelsDict = {
    "logistic regression": LogisticRegression(C=1.0, max_iter=1000, random_state=42),
    "knn": KNeighborsClassifier(n_neighbors=7, weights="distance", metric="minkowski"),
    "decision tree": DecisionTreeClassifier(max_depth=4, min_samples_leaf=10, random_state=42),
    "mlp": MLPClassifier(hidden_layer_sizes=(64, 32), activation="relu", solver="adam", alpha=1e-4, early_stopping=True,max_iter=500, random_state=42)
}