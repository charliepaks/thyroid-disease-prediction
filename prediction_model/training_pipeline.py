import pandas as pd
import numpy as np 
from pathlib import Path
import os
import sys
import joblib

# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# # Then perform import
from prediction_model.config import config  
from prediction_model.processing.data_handling import load_dataset,save_pipeline,separate_data,split_data
import prediction_model.processing.preprocessing as pp 
import prediction_model.pipeline as pipe 
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

models = {"Logistic Regression": LogisticRegression(random_state=42),
         "Decision Tree": DecisionTreeClassifier(random_state=42),
         "Random Forest": RandomForestClassifier(random_state=42)}

def fit_and_score(models, X_train, X_test, y_train, y_test):
    np.random.seed(42)

    # Loop through the models
    for name, model in models.items():
        # Fit the model to the data
        model.fit(X_train, y_train)
        # Evaluate the model and append its score to model_scores
        # Make predictions on the testing set
        y_preds = model.predict(X_test)

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, y_preds)
        precision = precision_score(y_test, y_preds)
        recall = recall_score(y_test, y_preds)
        f1 = f1_score(y_test, y_preds)

        # Print evaluation metrics
        print(name, ":")
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1)
        print("")

if __name__=='__main__':
    fit_and_score()