# diabetes_prediction/ml_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def bmi_calculate(height, weight):
    bmi = weight / (height**2)
    return bmi

def ml_predict(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age):
    # Read the training dataset
    df = pd.read_csv('diabetes_prediction/diabetes.csv')

    # Arrange the data
    x = df.drop(['Outcome'], axis=1)
    y = df.iloc[:, -1]

    # Split the data into training and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Create and train the random forest classifier
    rf = RandomForestClassifier()
    rf.fit(x_train, y_train)

    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    # Make predictions
    prediction_result = rf.predict(input_data)

    # Return the actual prediction result
    return prediction_result


