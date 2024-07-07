import pandas as pd
from flask import Flask, request, render_template, jsonify
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import SMOTE

app = Flask(__name__)

# Define paths
project_root = '/home/shoaib/Code/Churn_pred' 
data_path = os.path.join(project_root, 'app', 'data', 'Cleaned_Telecom_Dataset_New.csv')
models_dir = os.path.join(project_root, 'app', 'models')

# Load the saved scaler
scaler_path = os.path.join(models_dir, 'scaler.pkl')
scaler = pickle.load(open(scaler_path, 'rb'))

df_1 = pd.read_csv(data_path)
df_1 = df_1.drop('Unnamed: 0', axis=1)  # Remove 'Unnamed: 0' column if it exists

@app.route("/")
def loadPage():
    return render_template('home.html', query="")

@app.route("/", methods=['POST'])
def predict():
    model_name = request.form['model_name'] 

    # Get feature inputs from the form 
    input_features = []
    for i in range(1, 37):
        feature_value = request.form.get(f'query{i}', 0.0) # Default to 0.0 for missing values
        input_features.append(float(feature_value))

    # Create a DataFrame from input features (important for scaling)
    features = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 'Partner_No',
                'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service',
                'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic',
                'InternetService_No', 'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
                'OnlineBackup_No', 'OnlineBackup_Yes', 'DeviceProtection_No internet service',
                'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_Yes', 'StreamingMovies_No',
                'StreamingMovies_Yes', 'Contract_Month-to-month', 'Contract_One year',
                'Contract_Two year', 'PaperlessBilling_No', 'PaymentMethod_Bank transfer (automatic)',
                'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
                'tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36',
                'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']
    new_df = pd.DataFrame([input_features], columns=features)

    # Scale the input features using the loaded scaler
    scaled_input_features = scaler.transform(new_df)

    # Load the selected model
    model_path = os.path.join(models_dir, f'{model_name}.pkl')
    model = pickle.load(open(model_path, "rb"))
    print(model_path)

    # Make prediction using scaled input
    single = model.predict(scaled_input_features)  
    probability = model.predict_proba(scaled_input_features)[:, 1]
    print(single)

    if single == 1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {:.2f}%".format(probability[0]*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {:.2f}%".format(probability[0]*100)

    return render_template('home.html', output1=o1, output2=o2, 
                       query1 = request.form['query1'],
                        query2 = request.form['query2'],
                        query3 = request.form['query3'],
                        query4 = request.form['query4'],
                        query5 = request.form['query5'],
                        query6 = request.form['query6'],
                        query7 = request.form['query7'],
                        query8 = request.form['query8'],
                        query9 = request.form['query9'],
                        query10 = request.form['query10'],
                        query11 = request.form['query11'],
                        query12 = request.form['query12'],
                        query13 = request.form['query13'],
                        query14 = request.form['query14'],
                        query15 = request.form['query15'],
                        query16 = request.form['query16'],
                        query17 = request.form['query17'],
                        query18 = request.form['query18'],
                        query19 = request.form['query19'],
                        query20 = request.form['query20'],
                        query21 = request.form['query21'],
                        query22 = request.form['query22'],
                        query23 = request.form['query23'],
                        query24 = request.form['query24'],
                        query25 = request.form['query25'],
                        query26 = request.form['query26'],
                        query27 = request.form['query27'],
                        query28 = request.form['query28'],
                        query29 = request.form['query29'],
                        query30 = request.form['query30'],
                        query31 = request.form['query31'],
                        query32 = request.form['query32'],
                        query33 = request.form['query33'],
                        query34 = request.form['query34'],
                        query35 = request.form['query35'],
                        query36 = request.form['query36']
    )

@app.route("/show_accuracies")
def show_accuracies():
    # Load your dataset
    df = pd.read_csv('/home/shoaib/Code/Churn_pred/app/data/Cleaned_Telecom_Dataset_New.csv')
    df = df.drop('Unnamed: 0', axis=1)  

    # Prepare your features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    
    # Scale the features
    X_scaled = scaler.fit_transform(X)
    
    # Apply SMOTEENN to the entire dataset
    sm = SMOTEENN(smote=SMOTE(random_state=42))
    X_resampled, y_resampled = sm.fit_resample(X_scaled, y)
    
    # Split the resampled data
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
    
    accuracies = {}
    
    # Calculate accuracy for each model
    for model_name in ['decision_tree_smote_model', 'knn_smote_model', 'logistic_regression_smote_model', 'random_forest_smote_model']:
        model_path = os.path.join(models_dir, f'{model_name}.pkl')
        model = pickle.load(open(model_path, "rb"))
        
        # Predict on resampled test data
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred) * 100
        accuracies[model_name] = accuracy
    
    return render_template('results.html', accuracies=accuracies)

if __name__ == "__main__":
    app.run(debug=True)