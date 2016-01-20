from django.db import models
from django.utils import timezone
import random
from django import forms
# Create your models here.


class Type_of_food(models.Model):
	username = models.CharField(max_length = 20)
	type_code = models.CharField(max_length=10)
	type_name = models.CharField(max_length = 20)


class Table(models.Model):
	username = models.CharField(max_length = 20)
	table_code = models.CharField(max_length = 10)
	table_floor = models.CharField(max_length = 10)
	table_status = models.BooleanField(default = False)

class Foods(models.Model):
	username = models.CharField(max_length = 20)
	food_code = models.CharField(max_length = 10)
	type_code = models.CharField(max_length = 10)
	food_name = models.CharField(max_length = 30)
	food_cost = models.BigIntegerField()
	food_unit = models.CharField(max_length = 10)
	foodde_scribe = models.TextField()

class Staff(models.Model):
	username = models.CharField(max_length = 20)
	staff_code = models.CharField(max_length = 10)
	staff_password = models.CharField(max_length = 20)
	staff_name = models.CharField(max_length = 30)

class Bill_detail(models.Model):
	username = models.CharField(max_length = 20)
	bill_code = models.CharField(max_length = 10)
	food_code = models.CharField(max_length = 10)
	number = models.BigIntegerField()
	cost_on_food  =  models.BigIntegerField()

class Bill(models.Model):
	username = models.CharField(max_length = 20)
	bill_code = models.CharField(max_length = 10)
	table_code =  models.CharField(max_length = 10)
	table_floor = models.CharField(max_length = 10)
	staff_code = models.CharField(max_length = 10)
	bill_created = models.DateTimeField(default = timezone.now())
	bill_sale = models.BigIntegerField()
	bill_service = models.BigIntegerField()
	bill_total = models.BigIntegerField()
	bill_cost = models.BigIntegerField()

class Hostprofile (models.CharField):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	repeat_password = models.CharField(max_length = 30)
	hostmame = models.CharField(max_length = 20)
	host_porn = models.DateField()
	hostaddress = models.CharField(max_length = 30)
	hostphone = models.CharField(max_length = 12)
	hostemail = models.CharField(max_length = 30)
	host_create_date = models.DateTimeField(default = timezone.now())
	captcha_code = models.CharField(max_length = 10)

class Captcha(models.Model):
	captcha_code = models.CharField(max_length = 10)
	def createcaptcha(self):
 		l_max = 8
 		temp = ''
 		for i in range(0,l_max):
 			temp += random.choice('0123456789abcdefghijklmnopqrstuxyzABCDEFGHIJKLMNOPQRSTUXYZ')
 			self.captcha_code = temp
 			self.save()