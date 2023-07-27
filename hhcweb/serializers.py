from rest_framework import serializers
from hhcweb import models
from hhcweb.models import agg_com_colleague


# We are writing this because we need confirm password field in our Registration Request
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    # grp_id = serializers.PrimaryKeyRelatedField(queryset=agg_mas_group.objects.all(),many=False)
    
    class Meta:
        model  = agg_com_colleague
        fields = ['pk','clg_ref_id', 'clg_first_name', 'clg_mid_name' ,'clg_last_name' ,'grp_id' ,'clg_email' ,'clg_mobile_no' ,'clg_gender' ,'clg_address' ,'clg_is_login' ,'clg_designation' ,'clg_state' ,'clg_division' ,'clg_district' ,'clg_break_type' ,'clg_senior' ,'clg_hos_id' ,'clg_agency_id' ,'clg_status' ,'clg_added_by' ,'clg_modify_by' ,'clg_Date_of_birth' ,'clg_Work_phone_number' ,'clg_work_email_id' ,'clg_Emplyee_code' ,'clg_qualification','clg_avaya_agentid' ,'clg_Aadhar_no','clg_specialization', 'clg_profile_photo_path' ,'clg_joining_date' ,'clg_marital_status', 'password','password2']

        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not match')

        return data
    
    def create(self, validated_data):
        group_data = validated_data.pop('grp_id')
        validated_data['grp_id'] = group_data
        user = agg_com_colleague.objects.create_user(**validated_data)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    clg_ref_id = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = agg_com_colleague
        fields = ['clg_ref_id', 'password']










#---------------------------------------------- Sandip ----------------------------------------------------------
class agg_hhc_caller_relation_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_caller_relation
        fields = ['caller_rel_id','relation']           

class agg_hhc_locations_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_locations
        fields = ['loc_id','location'] 


class agg_hhc_sub_services_serializer(serializers.ModelSerializer): 
    class Meta:
        model = models.agg_hhc_sub_services
        fields = ['sub_srv_id','recommomded_service','srv_id','cost']


class agg_hhc_services_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_services
        fields = ['srv_id','service_title']

class agg_hhc_event_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_events
        fields = ['pt_id','start_date','end_date','srv_id','sub_srv_id']

class agg_hhc_add_service_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['srv_id','pt_id', 'sub_srv_id', 'start_date', 'end_date','prof_prefered', 'srv_prof_id']

class agg_hhc_add_discount_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_events
        fields = ['discount_type', 'discount','total_cost','final_cost']

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

class payment_status(serializers.Serializer):
    class Meta:
        model = models.agg_hhc_payments
        fields = ['pay_id', 'Transaction_Type', 'amount']
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
    fullname=serializers.SerializerMethodField()
    class Meta:
        model=models.agg_hhc_callers
        fields=('fullname','caller_id','phone','caller_rel_id','age','gender','email','contact_no','alter_contact','Address','save_this_add','profile_pic','caller_status')
    def get_name(self,obj):
        return f"{obj.fname} {obj.lname}".strip()


    
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
    fullname = serializers.SerializerMethodField()
    class Meta:
        model=models.agg_hhc_callers
        fields=('fullname','caller_id','phone','caller_rel_id','age','gender','email','contact_no','alter_contact','Address','save_this_add','profile_pic','caller_status')
    def get_fullname(self, obj):
        return f"{obj.fname} {obj.lname}".strip()
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

#------------------------------------agg_hhc_service_professionals------------

class agg_hhc_service_professionals_serializer(serializers.ModelSerializer): #professional availablity details with professional name and professional skill 
    class Meta:
        model=models.agg_hhc_service_professionals
        fields=('first_name','last_name','skill_set')
    
#-------------------------------------agg_hhc_professional_scheduled-----------

class agg_hhc_professional_scheduled_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_professional_scheduled
        fields=('srv_prof_id','scheduled_date','from_time','to_time')

#------------------------------------agg_hhc_event_professional---------------------

class agg_hhc_event_professional_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_event_professional
        fields=('eve_prof_id','eve_id','eve_req_id','srv_prof_id','eve_poc_id','srv_id')

#--------------------------------agg_hhc_recived_hospitals------------------

class agg_hhc_recived_hospitals_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_recived_hospitals
        fields=('')





#----------------------------------------agg_hhc_professional_zone------------------------#

class agg_hhc_professional_zone_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_professional_zone
        fields='__all__'




#--------------------------------------mayank--------------------------------------------

class AggHHCServiceProfessionalSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = models.agg_hhc_service_professionals
        fields = ('full_name', 'Services', 'phone_no','Ratings','Experience','Calendar')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}".strip()


#--------------------------------------agg_hhc_service_professionals------------------

class agg_hhc_service_professionals_zone_serializer(serializers.ModelSerializer):
    fullname=serializers.SerializerMethodField()
    class Meta:
        model=models.agg_hhc_service_professionals
        fields=('fullname','skill_set')
    def get_fullname(self,obj): 
        return f"{obj.first_name} {obj.last_name}".strip()
    

#--------------------------------agg_hhc_feedback_answers----------------------------

class agg_hhc_feedback_answers_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_service_professionals
        fields='__all__'

#---------------------------------------agg_hhc_event_plan_of_care------------------

class agg_hhc_event_plan_of_care_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_event_plan_of_care
        fields='__all__'


#---------------------------------------------Nikita P---------------------------------------------------------

class agg_hhc_professional_zone_serializer(serializers.ModelSerializer):
    class Meta:
        model  = models.agg_hhc_professional_zone
        fields = '__all__'
        
    def validate(self, data):
        return data
    
class agg_hhc_service_professional_serializer(serializers.ModelSerializer):
    class Meta:
        model  = models.agg_hhc_service_professionals
        fields = '__all__'
        
    def validate(self, data):
        return data
    
class agg_hhc_detailed_event_plan_of_care_serializer(serializers.ModelSerializer):
    class Meta:
        model  = models.agg_hhc_detailed_event_plan_of_care
        fields = '__all__'
        
    def validate(self, data):
        return data


#--------------------mohin------------------------------------------------------------------

class patients_info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_patients
        fields = ['name','mobile_no']
        
class hhc_services_date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['start_date','end_date','prof_prefered']

class hhc_services_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_services
        fields = ['service_title']

class agg_hhc_sub_services_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_sub_services
        fields = ['recommomded_service']
        
class agg_hhc_professional_zone_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_professional_zone
        fields = ['Name']
        
class CombinedSerializer(serializers.Serializer):
    patients = patients_info_Serializer()
    date = hhc_services_date_Serializer()
    services = hhc_services_Serializer()
    subservices = agg_hhc_sub_services_Serializer()
    professionalzone = agg_hhc_professional_zone_Serializer()