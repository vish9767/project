# from django.db import models
# from hhcweb.models import active_inactive_enum
# from django_enumfield import enum
# from hhcweb import models as webmodels

# # Create your models here.


# class status_enum(enum.Enum):
# 	Active = 1
# 	Inactive = 2
# 	Delete = 3
"""

class agg_hhc_app_caller_register(models.Model):#113
	app_user_id=models.AutoField(primary_key=True)
	phone=models.BigIntegerField(null=True)#this will used to store otp
	otp=models.IntegerField(null=True)
	otp_expire_time=models.DateTimeField(null=True)
	fname=models.CharField(max_length=50,null=True)
	lname=models.CharField(max_length=50,null=True)
	age=models.IntegerField(null=True)
	gender=models.CharField(max_length=20,null=True)
	email=models.EmailField(null=True)
	contact=models.BigIntegerField(null=True)
	alter_contact=models.BigIntegerField(null=True)
	Address=models.CharField(max_length=50,null=True)
	save_this_add=models.CharField(max_length=50,null=True)
	added_date=models.DateField(null=True,auto_now=True)
	profile_pic=models.ImageField(null=True)# profile picture
	status=enum.EnumField(active_inactive_enum,null=True)

class agg_hhc_app_family_details(models.Model):
	family_member_id = models.AutoField(primary_key=True)
	phone = models.BigIntegerField(null=True)
	otp = models.IntegerField(null=True)
	otp_expire_time = models.DateTimeField(null=True)
	fname = models.CharField(max_length=50, null=True)
	lname = models.CharField(max_length=50, null=True)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=20, null=True)
	email = models.EmailField(null=True)
	contact = models.BigIntegerField(null=True)
	alter_contact = models.BigIntegerField(null=True)
	Address = models.CharField(max_length=250, null=True)
	save_this_add = models.CharField(max_length=250, null=True)
	added_date = models.DateField(null=True)
	app_user_id = models.IntegerField(null=True)
	relation = models.ForeignKey(webmodels.agg_hhc_caller_relation, on_delete=models.SET_NULL, null=True)
	status = enum.EnumField(status_enum,null=True)

class agg_hhc_app_add_address(models.Model):
	address_id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=500, null=True)
	app_call_reg_id = models.ForeignKey(agg_hhc_app_caller_register, on_delete=models.SET_NULL,null=True)"""