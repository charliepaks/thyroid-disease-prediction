import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

FILE_NAME = 'Thyroid_Diff'
TEST_FILE = "test_data.csv"

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models')



TARGET = 'Recurred'

#Final features used in the model
FEATURES = ['Age', 'Gender', 'Smoking', 'Hx Smoking',
       'Hx Radiothreapy', 'Thyroid Function', 'Physical Examination', 'Adenopathy',
       'Pathology', 'Focality', 'Risk','T', 'N', 'M', 'Stage', 'Response', 'Recurred']

PRED_FEATURES = ['Age', 'Gender', 'Smoking', 'Hx Smoking',
       'Hx Radiothreapy', 'Thyroid Function', 'Physical Examination', 'Adenopathy',
       'Pathology', 'Focality', 'Risk','T', 'N', 'M', 'Stage', 'Response']

NUM_FEATURES = ['Age']

CAT_FEATURES = ['Gender', 'Smoking', 'Hx Smoking',
       'Hx Radiothreapy', 'Thyroid Function', 'Physical Examination', 'Adenopathy',
       'Pathology', 'Focality', 'Risk','T', 'N', 'M', 'Stage', 'Response']

COL_NORM = ['Age', 'Thyroid Function', 'Pathology', 'Risk', 'Physical Examination', 'Adenopathy',  'Response']


