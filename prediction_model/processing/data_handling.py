import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config

#Load the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH,file_name)
    _data = pd.read_csv(filepath)
    _data.columns = [c.strip() for c in _data.columns] # Fix Column names
    return _data[config.FEATURES]

def convert_cat_to_bin(_data):
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()

    # loop through each of the columns in the DataFrame
    for cols in _data.columns:
        if _data[cols].dtype == 'object':
            # convert the categorical values to binary values
            _data[cols] = label_encoder.fit_transform(_data[cols])

    return _data
    
def normalize_data(_data):
    scaler = MinMaxScaler()

    # We can now normalise the columns we have highlighted
    _data[config.COL_NORM] = scaler.fit_transform(_data[config.COL_NORM])
    return _data

# Separate X and y
def separate_data(data):
    X = data.drop(config.TARGET, axis=1)
    y= data[config.TARGET]
    return X,y

#Split the dataset
def split_data(X, y, test_size=0.2, random_state=42):
  # Split into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
  return X_train, X_test, y_train, y_test

#Serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    print(save_path)
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

#Deserialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH,pipeline_to_load)
    model_loaded = joblib.load(save_path)
    print(f"Model has been loaded")
    return model_loaded