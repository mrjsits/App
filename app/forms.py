from .models import Food_kinds, Table, Foods, Staff, Bill_detail, Bill, HostProfile, Captcha, Service
from django import forms
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
import random

class formHostRegister(forms.ModelForm):
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput())
	repeat_password = forms.CharField(max_length = 30, widget = forms.PasswordInput())
	class Meta:
		model =  HostProfile
		fields = ['host_mame', 'username', 'password', 'repeat_password', 'host_address', 'host_phone', 'host_email']

class formLogin(forms.ModelForm):
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput())
	class Meta:
		model = HostProfile
		fields = ['username', 'password']

class formCaptcha(forms.ModelForm):
	captcha_code = forms.CharField(max_length = 10)
	class Meta:
		model = Captcha
		fields = ['captcha_code']

class formService (forms.ModelForm):
	class Meta:
		model = Service
		fields = ['service_name', 'service_location','service_title', 'service_describe']
	

