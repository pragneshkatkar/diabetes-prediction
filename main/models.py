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
	diabetes_pedigree_function = models.DecimalField(max_digits=5, decimal_places=2)
	age = models.IntegerField()
	model1_prediction = models.CharField(max_length=10, default='0%')
	model2_prediction = models.CharField(max_length=10, default='0%')
	model3_prediction = models.CharField(max_length=10, default='0%')
	model4_prediction = models.CharField(max_length=10, default='0%')
	result = models.CharField(max_length=10, default='0%') 
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

class DietBlog(models.Model):
	heading = models.CharField(max_length=60)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
