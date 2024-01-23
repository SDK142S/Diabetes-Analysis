# diabetes_prediction/views.py
from django.shortcuts import render
from .models import Patient_data
from .ml_model import ml_predict

def index(request):
    if request.method == 'POST':
        # Retrieve input data from the form
        pregnancies = int(request.POST.get('pregnancies'))
        glucose = int(request.POST.get('glucose'))
        blood_pressure = int(request.POST.get('blood_pressure'))
        skin_thickness = int(request.POST.get('skin_thickness'))
        insulin = int(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        dpf = float(request.POST.get('dpf'))
        age = int(request.POST.get('age'))

        # Make predictions using your ML model
        outcome = ml_predict(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)

        # Save the patient data and prediction result to the database
        patient = Patient_data.objects.create(
            pregnancies=pregnancies,
            glucose=glucose,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin=insulin,
            bmi=bmi,
            dpf=dpf,
            age=age,
            outcome=outcome
        )

    # Fetch the latest patient from the database
    patient = Patient_data.objects.last()

    return render(request, 'index.html', {'patient': patient})
