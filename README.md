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
   python3 -m venv env 
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

