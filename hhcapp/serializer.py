from rest_framework import serializers
#from hhcapp import models
from hhcweb import models as webmodels

#-------------------------------------sandip------------------------------------------------------------------- 
class agg_hhc_app_services_serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_services
        fields = ['service_title', 'image_path'] 

class webserializers(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_family_details
        fields=['phone']
    def create(self,validated_data):
        return webmodels.agg_hhc_app_caller_register.objects.create(**validated_data)
    
class agg_hhc_app_family_details(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_family_details
        fields=['fname','lname','age','gender','email','contact','alter_contact']

class add_multiple_address_serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_add_address
        fields=['address','app_call_reg_id', 'name']






#-----------------------------------vishal--------------------------------------------------------------------



class agg_hhc_app_caller_register_Serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_caller_register
        fields='__all__'

class webserializers(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_caller_register
        fields=['phone']
    def create(self,validated_data):
        return webmodels.agg_hhc_app_caller_register.objects.create(**validated_data)
    
class agg_hhc_app_patient_by_caller_id(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_patients
        fields='__all__'

class agg_hhc_app_address_by_caller_id(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_add_address
        fields="__all__"
        