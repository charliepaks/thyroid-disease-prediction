
#### Purpose
The purpose of this project is to predict recurrence of well differentiated thyroid cancer. The data set was collected in duration of 15 years and each patient was followed for at least 10 years.

#### Dataset Source
The data was procured from thyroid disease datasets provided by the UCI Machine Learning Repository.

#### Data Dictionary
The summary of columns and their descriptions for this dataset is enumerated below:

Age: The age of the patient at the time of diagnosis or treatment.
Gender: The gender of the patient (male or female).
Smoking: Whether the patient is a smoker or not.
Hx Smoking: Smoking history of the patient (e.g., whether they have ever smoked).
Hx Radiotherapy: History of radiotherapy treatment for any condition.
Thyroid Function: The status of thyroid function, possibly indicating if there are any abnormalities.
Physical Examination: Findings from a physical examination of the patient, which may include palpation of the thyroid gland and surrounding structures.
Adenopathy: Presence or absence of enlarged lymph nodes (adenopathy) in the neck region.
Pathology: Specific types of thyroid cancer as determined by pathology examination of biopsy samples.
Focality: Whether the cancer is unifocal (limited to one location) or multifocal (present in multiple locations).
Risk: The risk category of the cancer based on various factors, such as tumor size, extent of spread, and histological type.
T: Tumor classification based on its size and extent of invasion into nearby structures.
N: Nodal classification indicating the involvement of lymph nodes.
M: Metastasis classification indicating the presence or absence of distant metastases.
Stage: The overall stage of the cancer, typically determined by combining T, N, and M classifications.
Response: Response to treatment, indicating whether the cancer responded positively, negatively, or remained stable after treatment.
Recurred: Indicates whether the cancer has recurred after initial treatment.

## Running Locally

Add PYTHONPATH variable for `~/.bash_profile ` for MacOS


## Virtual Environment
Install virtualenv

```python
python3 -m pip install virtualenv
```

Check version
```python
virtualenv --version
```

Create virtual environment

```python
virtualenv ml_package
```

Activate virtual environment

For Linux/Mac
```python
source ml_package/bin/activate
```
For Windows
```python
ml_package\Scripts\activate
```

Deactivate virtual environment

```python
deactivate
```


## Directory structure

```bash
prediction_model


├── MANIFEST.in
├── prediction_model
│   ├── config
│   │   ├── config.py
│   │   └── __init__.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── test.csv
│   │   └── train.csv
│   ├── __init__.py
│   ├── pipeline.py
│   ├── predict.py
│   ├── processing
│   │   ├── data_handling.py
│   │   ├── __init__.py
│   │   └── preprocessing.py
│   ├── trained_models
│   │   ├── classification.pkl
│   │   └── __init__.py
│   ├── training_pipeline.py
│   └── VERSION
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── pytest.ini
    └── test_prediction.py
```


# Build the Package

1. Goto Project directory and install dependencies
`pip install -r requirements.txt`

2. Create Pickle file after training:
`python prediction_model/training_pipeline.py`

3. Create source distribution and wheel
`python setup.py sdist bdist_wheel`

# Installation of Package

Go to project directory where `setup.py` file is located

1. To install it in editable or developer mode
```python
pip install -e .
```
```.``` refers to current directory

```-e``` refers to --editable mode

2. Normal installation
```python
pip install .
```
```.``` refers to current directory

3. Also can be installed from git as well after pushing to github

```
pip install git+https://github.com/charliepaks/thyroid-disease-prediction.git
```

# Testing the Package Working

1. Remove the PYTHONPATH from environment variables 
2. Goto a separate location which is outside of package directory
3. Create a new virual environment using the commands mentioned above & activate it
4. Before installing, test whether you are able to import the package of `prediction_model` - (you should not be able to do it)
5. Now in the new environment install the package using the generated file
`pip install git+https://github.com/charliepaks/thyroid-disease-prediction.git`
6. Now try importing the prediction_model, you should be able to do it successfully
7. Extras : Run training pipeline using the package, and also conduct the test


