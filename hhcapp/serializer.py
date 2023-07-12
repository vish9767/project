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
        model=webmodels.agg_hhc_patients
        fields=['phone']
    def create(self,validated_data):
        return webmodels.agg_hhc_callers.objects.create(**validated_data)
    
#-------------------------------------------------------------------------------------------------
class colleagueRegistersSerializer(serializers.ModelSerializer):
    # otp = serializers.CharField(write_only=True)

    class Meta:
        model = webmodels.agg_hhc_callers
        fields = ('id', 'caller_id', 'email', 'fname', 'lname','otp')

class colleagueVerifyPhoneOTPSerializer(serializers.ModelSerializer):
    model = webmodels.agg_hhc_callers
    fields = ('id', 'caller_id','otp')
    
class colleagueRegistersSerializer(serializers.ModelSerializer):
    # otp = serializers.CharField(write_only=True)

    class Meta:
        model = webmodels.agg_hhc_callers
        fields = ('caller_id', 'email', 'fname', 'lname','otp')

class verifyPhoneSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(write_only=True)

    class Meta:
        model = webmodels.agg_hhc_callers
        fields = ('id', 'caller_id')
        # extra_kwargs = {'otp': {'write_only': True}}

    def create(self, validated_data):
        otp = validated_data['otp']
        # otp = validated_data['otp']
        user = webmodels.agg_hhc_callers.objects.create_user(password=otp, **validated_data)
        return user
    
class CreatePhoneNo(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_callers
        fields=['caller_id', 'otp']
    def create(self,validated_data):
        return webmodels.agg_hhc_callers.objects.create(**validated_data)
    

#========================================================================================================
class agg_hhc_patients(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_patients
        fields=['first_name','name','Age','Gender','email_id','phone_no','mobile_no']

class add_multiple_address_serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_add_address
        fields="__all__"
class agg_hhc_app_refered_by_serializer(serializers.ModelSerializer):
    class Meta:
        model = webmodels.agg_hhc_hospitals
        fields=['hospital_name', 'hosp_id']

class agg_hhc_prefered_consultants_serializer(serializers.ModelSerializer):
    class Meta:
        model = webmodels.agg_hhc_doctors_consultants
        fields=[ 'doct_cons_id','first_name', 'last_name', 'middle_name']

          
class agg_hhc_patient_doc_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = webmodels.agg_hhc_patient_documents
        fields = ['agg_sp_pt_id', 'doc_name', 'doucment', 'added_at_time']



#-----------------------------------vishal--------------------------------------------------------------------



class agg_hhc_callers_Serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_callers
        fields='__all__'

class webserializers(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_callers
        fields=['phone']
    def create(self,validated_data):
        return webmodels.agg_hhc_callers.objects.create(**validated_data)
    
class agg_hhc_app_patient_by_caller_id(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_patients
        fields='__all__'

class agg_hhc_app_address_by_caller_id(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_app_add_address
        fields="__all__"
#___________________________________________state______________
class agg_hhc_state_serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_state
        fields="__all__"

#______________________________sub_services_from_service_id__________________________
class agg_hhc_sub_services_serializer(serializers.ModelSerializer):
    class Meta:
        model=webmodels.agg_hhc_sub_services
        fields="__all__"