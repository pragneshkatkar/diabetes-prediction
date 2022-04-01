from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prediction(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=60)
	number_of_pregnancies = models.IntegerField()
	glucose = models.DecimalField(max_digits=5, decimal_places=2)
	blood_pressure = models.DecimalField(max_digits=5, decimal_places=2)
	skin_thickness = models.DecimalField(max_digits=5, decimal_places=2)
	insulin = models.DecimalField(max_digits=5, decimal_places=2)
	bmi = models.DecimalField(max_digits=5, decimal_places=2)
	age = models.IntegerField()
	model1_prediction = models.BooleanField()
	model2_prediction = models.BooleanField()
	model3_prediction = models.BooleanField()
	model4_prediction = models.BooleanField()
	result = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	
class Doctor(models.Model):
	name = models.CharField(max_length=60)
	degree = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	contact_number = models.IntegerField()
	is_active = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

class UsersAddress(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=60)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=60)
	country = models.CharField(max_length=60)
	zip_code = models.IntegerField()

class Feedback(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	feedback = models.TextField()
