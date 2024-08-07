# Flask App 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.6 or higher
* pip (package installer for Python)

### Installing

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**

   ```bash
   cd <project-directory>
   ```

3. **Checkout the correct branch**

   ```bash
   git checkout Flask-app
   ```

4. **Create a virtual environment (recommended):**

   ```bash
   python -m venv env 
   ```

5. **Activate the virtual environment:**

   * Linux/macOS:
     ```bash
     source env/bin/activate
     ```
   * Windows:
     ```bash
     env\Scripts\activate
     ```

6. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   * **Note:** If taking a lot of time, move on to the next step and then install libraries one by one as required.

### Running the App

1. **Set the `FLASK_APP` environment variable:**
   ```bash
   cd app
   ```

   ```bash
   export FLASK_APP=app 
   ```
   * **Note:** On Windows, use `set FLASK_APP=app` instead.

3. **Run the Flask development server:**

   ```bash
   flask run
   ```

   The application should now be running at  [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

```
flask-app/
├── app/
│   ├── __init__.py
│   ├── __pycache__/
│   │   └── ...
│   ├── data/
│   │   └── ...
│   ├── models/
│   │   └── ...
│   ├── notebooks/
│   │   └── ...
│   ├── static/
│   │   └── ...
│   └── templates/
│       └── ...
├── run.py
├── requirements.txt
└── README.md
```

* **`app/`**: Contains the Flask application code.
    * **`__init__.py`**: Initializes the Flask app.
    * **`data/`**:  hold data files used by the app.
    * **`models/`**: stores trained models
    * **`notebooks/`**: contains Jupyter notebooks used for EDA or training.
    * **`static/`**:  Holds static assets.
    * **`templates/`**: Contains HTML templates for the app's views.

## Notebooks

- [Telecomm_Churn_EDA.ipynb](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/Telecomm_Churn_EDA.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/Telecomm_Churn_EDA.ipynb): Exploratory Data Analysis on Telecom churn dataset.
- [Logistic_Regression.ipynb](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/Logistic_Regression.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/Logistic_Regression.ipynb): Predicting churn using Logistic Regression.
- [Decision_Tree_Classifier.ipynb](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/Decision_Tree_Classifier.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/Decision_Tree_Classifier.ipynb): Predicting churn using Decision Tree Classifier.
- [knnclassification.ipynb](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/knnclassification.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/knnclassification.ipynb): Predicting churn using KNN classification.
- [RandomForestClassifier.ipynb](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/RandomForestClassifier.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hariskhan-hk/Churn_pred/blob/main/app/notebooks/RandomForestClassifier.ipynb): Predicting churn using Random Forest Classifier.


 
