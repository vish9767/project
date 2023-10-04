from rest_framework import serializers
from hhcweb.models import agg_com_colleague, agg_hhc_professional_zone, agg_hhc_service_professionals, agg_hhc_detailed_event_plan_of_care, agg_mas_group
from django.contrib.auth.hashers import make_password, check_password
from hhcweb import models

# We are writing this because we need confirm password field in our Registration Request
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    grp_id = serializers.PrimaryKeyRelatedField(queryset=agg_mas_group.objects.all(),many=False)
    
    class Meta:
        model  = agg_com_colleague
        # fields = ['pk','clg_ref_id','grp_id','clg_mobile_no', 'clg_otp', 'password','password2']
        fields = ['pk','clg_ref_id', 'clg_first_name', 'clg_mid_name' ,'clg_last_name' ,'grp_id' ,'clg_email' ,'clg_mobile_no' ,'clg_gender' ,'clg_address' ,'clg_is_login' ,'clg_designation' ,'clg_state' ,'clg_division' ,'clg_district' ,'clg_break_type' ,'clg_senior' ,'clg_hos_id' ,'clg_agency_id' ,'clg_status' ,'clg_added_by' ,'clg_modify_by' ,'clg_Date_of_birth' ,'clg_Work_phone_number' ,'clg_work_email_id' ,'clg_Emplyee_code' ,'clg_qualification','clg_avaya_agentid' ,'clg_Aadhar_no','clg_specialization', 'clg_profile_photo_path' ,'clg_joining_date' ,'clg_marital_status',  'clg_otp', 'clg_otp_count', 'clg_otp_expire_time', 'password','password2']

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

        # Hash the password before creating the user
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)

        # Create a new user with the hashed password
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
        fields = ['purp_call_id','event_status','Total_cost','discount_type','discount_value','final_amount']

class agg_hhc_event_response_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_events
        fields = ['agg_sp_pt_id','caller_id']

class agg_hhc_updateIDs_event_serializer(serializers.ModelSerializer): #also used to allocate
    class Meta:
        model = models.agg_hhc_events
        fields = ['eve_id','agg_sp_pt_id','caller_id','status']

class get_service_name(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_services
        fields = ['srv_id', 'service_title']

class get_sub_service_name(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_sub_services
        fields = ['sub_srv_id', 'recommomded_service']

class agg_hhc_add_service_serializer(serializers.ModelSerializer):
    srv_id = get_service_name()
    sub_srv_id = get_sub_service_name()
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_poc_id','srv_id', 'sub_srv_id', 'start_date', 'end_date', 'prof_prefered','remark']

class agg_hhc_add_service_put_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_poc_id','srv_id', 'sub_srv_id', 'start_date', 'end_date', 'prof_prefered','remark']

class put_agg_hhc_add_service_put_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_poc_id','srv_id', 'sub_srv_id', 'prof_prefered','remark']

class agg_hhc_create_service_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_poc_id','srv_id', 'sub_srv_id', 'start_date', 'end_date', 'prof_prefered','remark']

class agg_hhc_add_discount_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_events
        fields = ['discount_type', 'discount','total_cost','final_cost']

class relation_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_caller_relation
        fields = ['caller_rel_id', 'relation']

class Caller_details_serializer(serializers.ModelSerializer):
    caller_rel_id=relation_serializer()
    class Meta:
        model = models.agg_hhc_callers
        fields = ['phone', 'caller_fullname', 'caller_rel_id' ]

class Update_Caller_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_callers
        fields = ['phone', 'caller_fullname', 'caller_rel_id' ]



class preffered_proffesional(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_doctors_consultants
        fields = ['doct_cons_id','cons_fullname','mobile_no']

class patient_get_zone_serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_professional_zone
        fields = ['prof_zone_id', 'Name']

class agg_hhc_state(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_state
        fields = ['state_id','state_name']

class agg_hhc_city(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_city
        fields = ['city_id','city_name']

class hospital_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_hospitals
        fields = ['hosp_id', 'hospital_name']



class patient_detail_serializer(serializers.ModelSerializer):
    preferred_hosp_id=hospital_serializer()
    doct_cons_id=preffered_proffesional()
    prof_zone_id=patient_get_zone_serializer()
    state_id = agg_hhc_state()
    city_id = agg_hhc_city() 
    class Meta:
        model = models.agg_hhc_patients
        fields = ['agg_sp_pt_id','name', 'gender_id', 'Suffered_from', 'preferred_hosp_id', 'phone_no', 'patient_email_id','doct_cons_id','Age', 'state_id' ,'city_id' ,'address' ,'pincode' ,'prof_zone_id']

class update_patient_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_patients
        fields = ['agg_sp_pt_id','name', 'gender_id', 'Suffered_from', 'preferred_hosp_id', 'phone_no', 'patient_email_id','doct_cons_id','Age', 'state_id' ,'city_id' ,'address' ,'pincode' ,'prof_zone_id']
        # fields = ['agg_sp_pt_id','name', 'gender_id', 'Suffered_from', 'preferred_hosp_id', 'phone_no', 'patient_email_id','doct_cons_id','Age','state_id' ,'city_id' ,'address' ,'pincode' ,'prof_zone_id']



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
    # fullname=serializers.SerializerMethodField()
    class Meta:
        model=models.agg_hhc_callers
        fields=('caller_fullname','caller_id','phone','caller_rel_id','gender','email','contact_no','alter_contact','Address','save_this_add','profile_pic','purp_call_id')
    # def get_name(self,obj):
    #     return f"{obj.fname} {obj.lname}".strip()


    
##_______________________________enquiry_list________________##

class agg_hhc_patinet_list_enquiry_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_patient_list_enquiry
        fields='__all__'

class agg_hhc_get_state_serializer(serializers.ModelSerializer):    
    class Meta:
        model = models.agg_hhc_state
        fields = ['state_id','state_name']

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
    state= serializers.SerializerMethodField()
    city=serializers.SerializerMethodField()
    zone=serializers.SerializerMethodField()
    gender=serializers.SerializerMethodField()
    doct_cons=serializers.SerializerMethodField()
    class Meta:
        model=models.agg_hhc_patients
        fields='__all__'
    def get_state(self, instance):
        state_id_is = instance.state_id
        state_name_serializer = agg_hhc_get_state_serializer(state_id_is)
        return state_name_serializer.data
    def get_city(self,instance):
        city_id_is=instance.city_id
        city_id_serializer=agg_hhc_get_city_serializer(city_id_is)
        return city_id_serializer.data
    def get_zone(self,instance):
        zone_id_is=instance.prof_zone_id
        zone_id_serializer=agg_hhc_professional_zone_serializer(zone_id_is)
        return zone_id_serializer.data
    def get_gender(self,instance):
        gender_id_is=instance.gender_id
        gender_id_serializer=agg_hhc_gender_serializer(gender_id_is)
        return gender_id_serializer.data
    def get_doct_cons(self,instance):
        doct_cons_id_is=instance.doct_cons_id
        gender_id_serializer=preffered_proffesional(doct_cons_id_is)
        return gender_id_serializer.data



    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     print(instance)
    #     state_data = models.agg_hhc_state.objects.get(state_id=instance.state_id)
    #     state_data_serialized =agg_hhc_get_state_serializer(state_data).data
    #     data['state'] = state_data_serialized
    #     return data

#______________________________________agg_hhc_callers_serializer_____________
class agg_hhc_callers_details_serializer(serializers.ModelSerializer):#20
    # fullname = serializers.SerializerMethodField()
    caller_rel_id=relation_serializer()
    class Meta:
        model=models.agg_hhc_callers
        fields=('caller_fullname','caller_id','phone','caller_rel_id','Age','gender','email','contact_no','alter_contact','Address','save_this_add','profile_pic')
    # def get_fullname(self, obj):
    #     return f"{obj.fname} {obj.lname}".strip()
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

# class agg_hhc_professional_zone_serializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.agg_hhc_professional_zone
#         fields='__all__'




#--------------------------------------mayank--------------------------------------------
class JobTypeCountSerializer(serializers.ModelSerializer):
    class Meta :
        model  = agg_hhc_service_professionals
        fields = ['Job_type','status']
# class Services_data(serializers.ModelSerializer)
class AggHHCServiceProfessionalSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()
    # Services = Services_data()

    class Meta:
        model = models.agg_hhc_service_professionals
        fields = ('prof_fullname', 'srv_id', 'phone_no','Ratings','Experience','Calendar')

    # def get_full_name(self, obj):
    #     return f"{obj.first_name} {obj.middle_name} {obj.last_name}".strip()

class PaymentDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.agg_hhc_payment_details
        fields = ['pay_dt_id','eve_id', 'Total_cost', 'paid_by', 'amount_paid', 'amount_remaining', 'date','mode']

class GetPaymentDetailSerializer(serializers.ModelSerializer):  
    class Meta:
        model = models.agg_hhc_payment_details
        fields = ['eve_id', 'Total_cost', 'amount_paid', 'amount_remaining']

class GetEventPaymentDetailSerializer(serializers.ModelSerializer):  
    class Meta:
        model = models.agg_hhc_events
        fields = ['eve_id', 'final_amount']
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
        model  = agg_hhc_professional_zone
        fields = '__all__'
        
    def validate(self, data):
        return data
    
class agg_hhc_service_professional_serializer(serializers.ModelSerializer):
    class Meta:
        model  = agg_hhc_service_professionals

        fields = '__all__'
        
    def validate(self, data):
        return data
    
class agg_hhc_detailed_event_plan_of_care_serializer(serializers.ModelSerializer):
    class Meta:
        model  = agg_hhc_detailed_event_plan_of_care

        fields = '__all__'
        
    def validate(self, data):
        return data


#--------------------mohin------------------------------------------------------------------


class agg_hhc_events_serializers1(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_events
        fields="__all__"
    

#--------------------------------------ongoing service------------------



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_patients
        fields = ['name', 'phone_no']

class Patient_by_HHCID_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_patients
        fields = '__all__'




class ProfessionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_service_professionals
        # fields = ['first_name','last_name','srv_prof_id']prof_fullname
        fields = ['prof_fullname','srv_prof_id']



        
class ServiceSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_services
        fields = ['srv_id','service_title']


class ProfesNameSerializer(serializers.ModelSerializer):
    
    srv_prof_id = ProfessionalDataSerializer()
    srv_id = ServiceSerilaizer()
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['start_date','end_date','prof_prefered','eve_id','srv_id','srv_prof_id','service_status']

class SessionStatusSerializer(serializers.ModelSerializer):
    Total_case_count = serializers.SerializerMethodField()
    session_done = serializers.SerializerMethodField()

    class Meta:
        model = models.agg_hhc_detailed_event_plan_of_care
        fields = ['eve_id', 'Session_status', 'Total_case_count','session_done']
       
    def get_Total_case_count(self, obj):
        queryset = models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=obj.eve_id)
        return queryset.count()

    def get_session_done(self, obj):
        queryset = models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=obj.eve_id, Session_status=2)
        return queryset.count()

        

class AggHhcPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_payments
        fields = ['event_id', 'amount']


from django.db.models import Sum
class OngoingServiceSerializer(serializers.ModelSerializer):
    agg_sp_pt_id = PatientSerializer()
    srv_prof_id = ProfesNameSerializer(many=True, source = 'event_id')
    Pending_amount = serializers.SerializerMethodField()
    session_status = SessionStatusSerializer(many=True, source='event_id')  
    # status = serializers.SerializerMethodField()
    
    class Meta:
        model = models.agg_hhc_events
        fields = ('eve_id','event_code','Total_cost','agg_sp_pt_id','srv_prof_id','Pending_amount','session_status', 'status','event_status')
        # fields = ('eve_id','event_code','Total_cost','agg_sp_pt_id','srv_prof_id','Pending_amount','status','event_status')
    

    
    def to_representation(self, instance):
        event_status = instance.event_status
        status = instance.status
        if status == 1 and event_status == 2:
            return super().to_representation(instance)

    
    def get_Pending_amount(self, instance):
        total_cost = instance.Total_cost
        event_id = instance.eve_id
        try:
            

            payment_sum = models.agg_hhc_payment_details.objects.filter(eve_id=event_id).aggregate(total_amount_paid=Sum('amount_paid'))['total_amount_paid']
            print(payment_sum,'=================')
            if payment_sum is not None:
                return total_cost - payment_sum
            else:
                return total_cost

        
        except models.agg_hhc_payment_details.DoesNotExist:
            return total_cost

# -------------------------------------Amit Rasale------------------------------------------------------------
class agg_hhc_enquiry_previous_follow_up_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up
        fields=('enq_follow_up_id', 'event_id', 'follow_up_date_time', 'previous_follow_up_remark')

class agg_hhc_enquiry_Add_follow_up_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up
        fields=('enq_follow_up_id', 'event_id', 'follow_up', 'follow_up_date_time', 'previous_follow_up_remark')
        # fields = '__all__'

class agg_hhc_enquiry_create_follow_up_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up
        fields=('enq_follow_up_id', 'event_id','follow_up')

class agg_hhc_enquiry_follow_up_cancellation_reason_spero_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up_cancellation_reason
        fields = ['cancelation_reason_id','cancelation_reason','cancel_by_id']

class agg_hhc_enquiry_follow_up_cancellation_reason_patent_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up_cancellation_reason
        fields=('canclation_reason_id', 'canclation_reason_patent')

class agg_hhc_enquiry_Add_follow_up_Cancel_by_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up
        fields=('enq_follow_up_id', 'event_id', 'follow_up', 'cancel_by', 'canclation_reason', 'previous_follow_up_remark')

class agg_hhc_enquiry_Add_follow_up_create_service_serializer(serializers.ModelSerializer):   
    class Meta:
        model=models.agg_hhc_enquiry_follow_up
        fields=('enq_follow_up_id', 'event_id', 'follow_up',  'previous_follow_up_remark')



class enquiries_service_serializer(serializers.ModelSerializer):   
    class Meta:
        model= models.agg_hhc_enquiry_follow_up
        fields=('enq_follow_up_id', 'event_id', 'follow_up','added_date','last_modified_date')
class services(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_services
        fields = ['service_title']
class ServiceNameSerializer(serializers.ModelSerializer):
    srv_id = services()
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_id','srv_id','start_date']

class patient_professional_zone_serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_professional_zone
        fields = ['prof_zone_id','city_id', 'Name']

class AggHhcPatientListEnquirySerializer(serializers.ModelSerializer):
    prof_zone_id = patient_professional_zone_serializer()
    class Meta: 
        model = models.agg_hhc_patient_list_enquiry
        fields = [ 'pt_id',  'name', 'phone_no', 'Suffered_from', 'prof_zone_id']    #sandip

from django.db.models import Max, Q
class agg_hhc_service_enquiry_list_serializer(serializers.ModelSerializer):
    srv_id = ServiceNameSerializer(many=True, source = 'event_id')
    pt_id = AggHhcPatientListEnquirySerializer()
    folloup_id = serializers.SerializerMethodField()

    class Meta:
        model=models.agg_hhc_events
        fields = ('eve_id','event_code', 'patient_service_status', 'pt_id','srv_id', 'folloup_id')     #amit

    def get_folloup_id(self, obj):
        latest_follow_up_date = models.agg_hhc_enquiry_follow_up.objects.filter(
            event_id=obj.eve_id
        ).aggregate(latest_date=Max('follow_up_date_time'))['latest_date']

        has_follow_up_1 = models.agg_hhc_enquiry_follow_up.objects.filter(
            event_id=obj.eve_id,
            follow_up='1'
        ).exists()
        if has_follow_up_1:
            return []
        if latest_follow_up_date is None:
            return []
        queryset = models.agg_hhc_enquiry_follow_up.objects.filter(
            event_id=obj.eve_id
        ).exclude(Q(follow_up='1') | Q(follow_up_date_time__lt=latest_follow_up_date))
        serializer = enquiries_service_serializer(queryset, many=True)
        respose_data = {
            'data': serializer.data
        }
        return serializer.data




# --------------------------------------------------- Sandip Shimpi -------------------------------------------------
class agg_hhc_callers_createService_serializer(serializers.ModelSerializer):#20
    class Meta:
        model=models.agg_hhc_callers
        # fields=['caller_id','phone','caller_fullname', 'caller_rel_id','purp_call_id']
        fields='__all__'

class agg_hhc_patient_list_serializer(serializers.ModelSerializer):#6
    class Meta:
        model=models.agg_hhc_patient_list_enquiry
        fields='__all__'

class DateTimeFieldTZ(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime('%Y-%m-%d %H:%M:%S')

class agg_hhc_add_detail_service_serializer(serializers.ModelSerializer):
    actual_StartDate_Time = DateTimeFieldTZ()
    actual_EndDate_Time = DateTimeFieldTZ()
    class Meta:
        model = models.agg_hhc_detailed_event_plan_of_care
        fields = ['eve_poc_id','eve_id','index_of_Session','srv_prof_id','Session_status','actual_StartDate_Time','actual_EndDate_Time']
        # fields = '__all__'

class agg_hhc_doctors_consultants_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_doctors_consultants
        fields=['doct_cons_id','cons_fullname','mobile_no']

    # coupon_code serializer
class agg_hhc_coupon_code_serializers(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_coupon_codes
        fields="__all__"

class agg_hhc_get_city_serializer(serializers.ModelSerializer):    
    class Meta:
        model = models.agg_hhc_city
        fields = ['city_id','city_name','state_id']
# ---------------- service reschedule --------------

class Detailed_EPOC_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_detailed_event_plan_of_care
        # fields = ['agg_sp_dt_eve_poc_id','eve_id', 'start_date', 'end_date']
        fields = ['eve_id', 'start_date', 'end_date','remark']

class AggservicedetailSerializer(serializers.ModelSerializer):
    dtl_epoc_data = serializers.SerializerMethodField()  # Use SerializerMethodField

    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_id', 'start_date', 'end_date', 'dtl_epoc_data','remark']

    def get_dtl_epoc_data(self, instance):
        related_dtl_instances = models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=instance.eve_id)
        dtl_serializer = Detailed_EPOC_serializer(related_dtl_instances, many=True)
        return dtl_serializer.data
    



# ------------------ Professional Reschedule -------------------

# class Prof_Reschedule_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.agg_hhc_detailed_event_plan_of_care
#         fields = ['eve_id','start_date','end_date','srv_prof_id','Session_status']

class Prof_Reschedule_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_detailed_event_plan_of_care
        # fields = ['agg_sp_dt_eve_poc_id','eve_id','index_of_Session','start_date','end_date','srv_prof_id','Session_status']
        fields = ['agg_sp_dt_eve_poc_id','eve_id','start_date','end_date','srv_prof_id','remark']


# ----------------- prof avail ------------

# class prof_name(serializers.ModelSerializer):
#     class Meta:
#         model = models.agg_hhc_service_professionals
#         fields = ['srv_prof_id','professional_code','prof_fullname']
# class avail_prof_serializer(serializers.ModelSerializer):
#     srv_prof_id = prof_name()
#     class Meta:
#         model=models.agg_hhc_professional_sub_services
#         fields = ('srv_id','srv_prof_id')


# ----------- cancellation service ----------
from .models import status_enum
from django.utils import timezone
from datetime import timedelta
from django.db.models import F, ExpressionWrapper, FloatField

class Detail_Event_Plan_of_Care_Staus(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_detailed_event_plan_of_care
        fields = ['status']
    
class Event_Plan_of_Care_Staus(serializers.ModelSerializer):

    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['start_date','status']
    

class Event_Staus(serializers.ModelSerializer):
    Total_session = serializers.SerializerMethodField()
    per_session_cost = serializers.SerializerMethodField()
    completed_session_amt = serializers.SerializerMethodField()
    refund_amt = serializers.SerializerMethodField()
    

    class Meta:
        model = models.agg_hhc_events
        fields = ['eve_id','Total_cost','status','Total_session','per_session_cost','completed_session_amt','refund_amt']
       

    def get_Total_session(self, obj):
        # queryset = models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=obj.eve_id, Session_status=1)
        queryset = models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=obj.eve_id)
        return queryset.count()

    def get_per_session_cost(self, obj):
        Total_cost = obj.Total_cost  # Access Total_cost field of the obj
        Total_session = self.get_Total_session(obj)  # Call the previously defined method
        return int(Total_cost / Total_session) if Total_session > 0 else 0
    
    def get_completed_session_amt(self, obj):
        queryset = models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=obj.eve_id, Session_status=2)
        # return queryset.count()
        completed_session = queryset.count()
        per_session = self.get_per_session_cost(obj)
        return int(per_session * completed_session)
    
    def get_refund_amt(self,obj):
        total_cost = obj.Total_cost
        com_ses_amt = self.get_completed_session_amt(obj)
        ref_amt = total_cost - com_ses_amt
        current_date = timezone.now().date() 
        previous_24_hours = timezone.now() - timedelta(hours=24)
        previous_48_hours = timezone.now() - timedelta(hours=48)
        previous_24_hours_date = previous_24_hours.date()
        previous_48_hours_date = previous_48_hours.date()

        refaund_amt = 0

        srv_start_date = models.agg_hhc_event_plan_of_care.objects.filter(eve_id=obj.eve_id)
        for srv_start_dates in srv_start_date:
            if srv_start_dates.start_date.date() <= current_date:
                refaund_amt = 200
            elif srv_start_dates.start_date.date() >= previous_24_hours_date:
                refaund_amt = 200
            elif srv_start_dates.start_date.date() >= previous_48_hours_date:
                refaund_amt = 0
        
        return int(ref_amt - refaund_amt)
            


class ServiceCancellationSerializer(serializers.ModelSerializer):
    DetaileventStaus = Detail_Event_Plan_of_Care_Staus(source='event_id',read_only=True)
    eventPlanStaus = Event_Plan_of_Care_Staus(source='event_id',read_only=True)
    eventStaus = Event_Staus(source='event_id',read_only=True)
 

    class Meta:
        model = models.agg_hhc_cancellation_history
        # fields = ['canc_his_id','event_id','cancellation_by','reason','cancelled_date','DetaileventStaus','eventPlanStaus','eventStaus','cost_per_session']
        fields = ['canc_his_id','event_id','cancellation_by','reason','remark','DetaileventStaus','eventPlanStaus','eventStaus']

    


    def create(self, validated_data):
        event = validated_data.get('event_id')
        if event:
           
            try:
               

                detail_event_poc=models.agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=event)
                event_poc=models.agg_hhc_event_plan_of_care.objects.filter(eve_id=event)
                event_model=models.agg_hhc_events.objects.filter(eve_id=event.eve_id)
                
                for detail_event_poc_queryset in detail_event_poc:
                    detail_event_poc_queryset.status= status_enum.Inactive.value
                    detail_event_poc_queryset.save()
                
                for event_poc_queryset in event_poc:
                    event_poc_queryset.status= status_enum.Inactive.value
                    event_poc_queryset.save()
                
                for event_queryset in event_model:
                    event_queryset.status= status_enum.Inactive.value
                    event_queryset.save()

            except models.agg_hhc_detailed_event_plan_of_care.DoesNotExist:
                print("this is not available")
                pass  
        cancellation_history = models.agg_hhc_cancellation_history.objects.create(**validated_data)
        return cancellation_history
    

#-------------------------------------- professional availibility for cancellation---------------------------------------------------------------------------

class prof_name(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_service_professionals
        fields = ['srv_prof_id','prof_fullname']
class avail_prof_serializer(serializers.ModelSerializer):
    srv_prof_id = prof_name()
    class Meta:
        model=models.agg_hhc_professional_sub_services
        fields=('srv_prof_id','srv_id')         


#-----------------------------------------------------------------------------------------------------------------
class get_gender(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_gender
        fields = ['gender_id','name']

class get_doctor_consultant(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_doctors_consultants
        fields = ['doct_cons_id','cons_fullname','mobile_no']

class add_enquiry_patient_by_form_serializer(serializers.ModelSerializer):
    # gender_id = get_gender()
    # doct_cons_id = get_doctor_consultant()
    class Meta:
        model = models.agg_hhc_patient_list_enquiry
        fields = ['pt_id','name','phone_no','Age','gender_id','refer_by','Patient_status_at_present','doct_cons_id','address','suffered_from']

class add_caller_by_form_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_callers
        fields = ['caller_id','caller_fullname','phone']

class create_plane_of_care_serializer(serializers.ModelSerializer):
    # srv_id = get_service
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['srv_id','start_date']

class add_service_get_event_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_events
        fields = '__all__'

class add_service_get_POC_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_poc_id','srv_id']#,'sub_srv_id','actual_StartDate_Time','actual_EndDate_Time','prof_prefered','remark']
class Purpose_of_call(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_purpose_call
        fields = ['purp_call_id','name']

class add_service_get_caller_serializer(serializers.ModelSerializer):
    purp_call_id = Purpose_of_call()
    class Meta:
        model = models.agg_hhc_callers
        fields = ['caller_id','caller_fullname','purp_call_id','phone']

class agg_hhc_get_state_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_state
        fields = ['state_id','state_name']

class agg_hhc_get_city(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_city
        fields = ['city_id','city_name']

class add_service_get_patient_serializer(serializers.ModelSerializer):
    gender_id = get_gender()
    preferred_hosp_id=hospital_serializer()
    doct_cons_id = agg_hhc_doctors_consultants_serializer()
    state_id = agg_hhc_get_state_serializers()
    city_id = agg_hhc_get_city()
    prof_zone_id = patient_professional_zone_serializer()
    class Meta:
        model = models.agg_hhc_patient_list_enquiry
        fields = ['pt_id','name','gender_id','Age','preferred_hosp_id','Suffered_from','phone_no','patient_email_id','doct_cons_id','state_id','city_id','prof_zone_id','address']
        # fields = ['pt_id','name','gender_id','Age','preferred_hosp_id']#,'Suffered_from','phone_no','patient_email','doct_cons_id','state_id','city_id','prof_zone_id','address']

class prof_allocate_get_callerID_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_callers
        fields = ['caller_id']     

class prof_allocate_get_patientID_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_patients
        fields = ['agg_sp_pt_id','city_id']

class prof_allocate_get_POCID_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.agg_hhc_event_plan_of_care
        fields = ['eve_poc_id']