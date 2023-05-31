from django.db import models
from hhcweb.models import active_inactive_enum
from django_enumfield import enum
# Create your models here.
class agg_hhc_app_caller_register(models.Model):#113
	app_call_reg_id=models.AutoField(primary_key=True)
	phone=models.IntegerField(null=True)#this will used to store otp
	otp=models.IntegerField(null=True)
	otp_expire_time=models.DateTimeField(null=True)
	fname=models.CharField(max_length=50,null=True)
	lname=models.CharField(max_length=50)
	age=models.IntegerField(null=True)
	# gender=models.CharField(null=True)
	email=models.EmailField(null=True)
	contact=models.IntegerField(null=True)
	Address=models.CharField(max_length=50,null=True)
	pincode=models.IntegerField(null=True)
	house_no=models.CharField(max_length=50,null=True)
	town=models.CharField(max_length=50,null=True)
	state=models.CharField(max_length=50,null=True)
	save_this_add=models.CharField(max_length=50,null=True)
	added_date=models.DateField(null=True)
#	profile_pic=models.CharField(null=True)# profile picture
	# status=enum.EnumField(active_inactive_enum)
	
