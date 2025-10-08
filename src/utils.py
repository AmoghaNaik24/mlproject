import os
import pickle
from sklearn.metrics import r2_score, mean_squared_error

def save_object(file_path, obj):
    """Save a Python object to a file using pickle"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)

def load_object(file_path):
    """Load a Python object from a pickle file"""
    with open(file_path, "rb") as file_obj:
        return pickle.load(file_obj)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Evaluate multiple models and return a dictionary of R2 scores.
    models: dict with {model_name: model_instance}
    """
    model_report = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        r2_train = r2_score(y_train, y_train_pred)
        r2_test = r2_score(y_test, y_test_pred)
        model_report[name] = {"R2_train": r2_train, "R2_test": r2_test}
    return model_report
