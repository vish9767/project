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


# class agg_hhc_services_serializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.agg_hhc_services
#         fields = ['srv_id','service_title'] 

# class agg_hhc_sub_services_serializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.agg_hhc_sub_services
#         fields = ['sub_srv_id','srv_id','recommomded_service'] 

class agg_hhc_sub_services_serializer(serializers.ModelSerializer): 
    
    class Meta:
        model = models.agg_hhc_sub_services
        fields = ['sub_srv_id','recommomded_service','srv_id','cost']


class agg_hhc_services_serializer(serializers.ModelSerializer):
    service = agg_hhc_sub_services_serializer(many=True, read_only=True)
    class Meta:
        model = models.agg_hhc_services
        fields = ['srv_id','service_title', 'service', ]



# class Model1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.agg_hhc_sub_services
#         fields = '__all__'

# class Model2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.agg_hhc_services
#         fields = '__all__'

# class AddPatientOrCheckCallerExistSerializer(serializers.Serializer):
#     model1 = Model1Serializer()
#     model2 = Model2Serializer()

class agg_hhc_add_service_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['srv_id','pt_id', 'sub_srv_id', 'start_date', 'end_date','prof_prefered', 'srv_prof_id', 'discount_type', 'discount','total_cost','final_cost']

class Caller_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_callers
        fields = ['phone', 'fname', 'lname', 'caller_rel_id' ]

class relation_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_caller_relation
        fields = ['caller_rel_id', 'relation']

class patient_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_patients
        fields = ['agg_sp_pt_id','name', 'Gender', 'Suffered_from', 'hosp_id', 'dob', 'phone_no', 'email_id']

class hospital_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_hospitals
        fields = ['hosp_id', 'hospital_name']

class DateSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['start_date'] = instance.start_date.strftime('%Y-%m-%d')
        representation['end_date'] = instance.end_date.strftime('%Y-%m-%d')
        return representation
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


#__________________________agg_hhc_callers_seralizer____________________##
class agg_hhc_callers_seralizer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_callers
        fields='__all__'

class agg_hhc_app_patient_by_caller_phone_no(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_patients
        fields='__all__'

#______________________________________agg_hhc_callers_serializer_____________
class agg_hhc_callers(serializers.ModelSerializer):#20
    class Meta:
        model=models.agg_hhc_callers
        fields='__all__'

#------------------------------------agg_hhc_hospitals_serializer_____________
class agg_hhc_hospitals_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_hospitals
        fields='__all__'
    
#-----------------------------------agg_hhc_agg_hhc_pincode-----------------------
class agg_hhc_pincode_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_pincode
        fields="__all__"

#--------------------------------------agg_hhc_city--------------------------
class agg_hhc_city(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_city
        fields='__all__'