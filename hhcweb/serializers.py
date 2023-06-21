from rest_framework import serializers
from hhcweb import models

#---------------------------------------------- Sandip ----------------------------------------------------------
class agg_hhc_caller_relation_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_caller_relation
        fields = ['caller_rel_id','relation']           

class agg_hhc_locations_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_locations
        fields = ['loc_id','location'] 


class agg_hhc_services_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_services
        fields = ['srv_id','service_title'] 

class agg_hhc_sub_services_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_sub_services
        fields = ['sub_srv_id','recommomded_service'] 

class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_sub_services
        fields = '__all__'

class Model2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_services
        fields = '__all__'

class AddPatientOrCheckCallerExistSerializer(serializers.Serializer):
    model1 = Model1Serializer()
    model2 = Model2Serializer()

    


# ------------------------------------------------------ Vishal -------------------------------------------------------
class agg_hhc_purpose_call_serializer(serializers.ModelSerializer):#25
    class Meta:
        model=models.agg_hhc_purpose_call
        fields='__all__'
        


class agg_hhc_gender_serializer(serializers.ModelSerializer):#112
    class Meta:
        model=models.agg_hhc_gender
        fields='__all__'


class agg_hhc_patients_serializer(serializers.ModelSerializer):#6
    class Meta:
        model=models.agg_hhc_patients
        fields='__all__'
        
#############______________get patient details from caller id but latest record_______#

class get_latest_patient_record_from_caller_id(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_patients
        fields='__all__'

#####_____________________agg_hhc_callers_____________________________________________#######

class agg_hhc_callers_serializer(serializers.ModelSerializer):#20
    class Meta:
        model=models.agg_hhc_callers
        fields="__all__"


    
##_______________________________enquiry_list________________##

class agg_hhc_patinet_list_enquiry_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_patinet_list_enquiry
        fields='__all__'

#_____________________________agg_hhc_service_professional_details____##
class agg_hhc_service_professional_details_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_service_professional_details
        fields='__all__'