from django.db import models

class Patient_data(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    blood_pressure = models.IntegerField()
    skin_thickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.FloatField()
    dpf = models.FloatField()
    age = models.IntegerField()
    outcome = models.IntegerField()

