from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

class userform(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=50)
	email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter emailid'}),required=True,max_length=50)
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter firstname'}),required=True,max_length=50)
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last_name'}),required=True,max_length=50)
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),required=True,max_length=50)
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter confirm_password'}),required=True,max_length=50)

	class Meta():
		model=User
		fields=['username','email','first_name','last_name','password']
# Validation of username  and email

	def clean_username(self):
		user=self.cleaned_data['username']
		try:
			match=User.objects.get(username=user)
		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("Username already exist")

	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			mt=validate_email(email)
		except:
			return forms.ValidationError("Email is not in correct format")
		return email


	def clean_confirm_password(self):
		pas=self.cleaned_data['password']
		cpas=self.cleaned_data['confirm_password']
		MIN_LENGTH=8
		if pas and cpas:
			if pas != cpas:
				raise forms.ValidationError("password and confirm_password does not match")
			else:
				if len(pas)<MIN_LENGTH:
					raise forms.ValidationError("password should have atleast %d charecter" %MIN_LENGTH)
				if pas.isdigit():
					raise forms.ValidationError("password should not all numbers")

		

# charts forms.py

class View_Report_Form(forms.ModelForm):
	max_temperature=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Temperature'}),required=True,max_length=10)
	min_temperature=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Temperature'}),required=True,max_length=10)
	max_humidity=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Humidity'}),required=True,max_length=10)
	min_humidity=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Humidity'}),required=True,max_length=10)
	class Meta:
		model=TempHumdity
		fields=['max_temperature','min_temperature','max_humidity','min_humidity',]
		
