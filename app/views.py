from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import formHostRegister, formLogin, formCaptcha, formService
import random
from django import forms
from .models import Food_kinds, Table, Foods, Staff, Bill_detail, Bill, HostProfile, Captcha
# Create your views here.


def register(request):
	captcha_code = Captcha()
	captcha_code.createcaptcha()
	field_captcha = formCaptcha(request.POST or None)

	host_register_form = formHostRegister(request.POST or None)
	context = {
		'host_register_form': host_register_form,
		'captcha': captcha_code.captcha_code,
		'field_captcha': field_captcha,
	}
	if request.method == "POST":
		get_host_register_form = formHostRegister(request.POST) #get Post from html
		getcaptcha = formCaptcha(request.POST) #get Post from html
		if get_host_register_form.is_valid() and getcaptcha.is_valid(): # check form 
			getdata_register = get_host_register_form.save(commit = False) #save profile register
			keepcaptcha= getcaptcha.save(commit = False)
			if getdata_register.password == getdata_register.repeat_password: # check correct password
				for i in Captcha.objects.all():
					if i.captcha_code == keepcaptcha.captcha_code: #check captcha code
						user = User.objects.create_user(request.POST['username'], '', request.POST['password']) # create user
						user.save() # save
						getdata_register.save() # save profile register
						userlogin = authenticate(username = request.POST['username'], password = request.POST['password'])
						login(request, userlogin)
						return redirect('serviceview')
		else:
			pass
	return render(request, 'register.html', context)

@login_required
def home (request):
	context = {
		
	}
	return render(request, 'home.html', context)


def loginview(request):
	host_login = formLogin(request.POST or None)
	context = {
		'host_login':host_login,
	}
	if request.method == "POST":
		if host_login.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user.is_active:
				login(request, user)
				return redirect('home')
		else:
			pass
	return render(request, 'login.html', context)

def logoutview(request):
	if request.user.is_authenticated():
		logout(request)
	return redirect('loginview')

def serviceview(request):
	serviceinfo = formService(request.POST or None)
	context = {
		'serviceinfo' : serviceinfo,
	}
	if request.method == "POST":
		serviceinfo = formService(request.POST)	
		if serviceinfo.is_valid():
			getservice = serviceinfo.save(commit = False)
			getservice.username =  request.user.username
			getservice.save()
			return redirect('home')
		else:
			pass
	return render(request, 'service.html', context)

