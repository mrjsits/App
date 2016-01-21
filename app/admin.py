from django.contrib import admin
from .models import Food_kinds, Table, Foods, Staff, Bill_detail, Bill, HostProfile, Captcha, Service
from django.contrib.auth.models import User
# Register your models here.
class AdminViewHost(admin.ModelAdmin):
	list_display = ['host_mame', 'username', 'password', 'host_address', 'host_phone','host_email', 'host_create_date']
	class Meta:
		models = HostProfile
admin.site.register(HostProfile, AdminViewHost)
admin.site.register(Captcha)

class AdminViewService(admin.ModelAdmin):
	list_display = ['username', 'service_name', 'service_location', 'service_title', 'service_describe']
	class Meta:
		models = Service
admin.site.register(Service, AdminViewService)

class AdminViewFoods(admin.ModelAdmin):
	list_display = ['username', 'food_code', 'type_code', 'food_name', 'food_cost', 'food_unit', 'food_describe']
	class Meta:
		models = Foods
admin.site.register(Foods, AdminViewFoods)

class AdminViewFoodkinds(admin.ModelAdmin):
	list_display = ['username', 'type_code', 'type_name']
	class Meta:
		models = Food_kinds
admin.site.register(Food_kinds, AdminViewFoodkinds)