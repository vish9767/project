from rest_framework import serializers
from hhcweb.models import *
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from decimal import Decimal


class agg_hhc_service_professionals_serializer(serializers.Serializer):
    class Meta:
        model=agg_hhc_service_professionals
        # fields = '__all__'
        fields = ['srv_prof_id','phone_no', 'OTP']

    def validate(self, data):
        return data
        
    def create(self,validated_data):
        pro_obj = agg_hhc_service_professionals.objects.create(**validated_data)
        return pro_obj
    

class UserRegistrationSerializer2(serializers.ModelSerializer):
    class Meta:
        model  = agg_com_colleague
        fields = ['pk','clg_mobile_no', 'clg_otp']

    def validate(self, data):
        return data
    
    
class agg_hhc_professional_location_serializer(serializers.ModelSerializer):

    class Meta:
        model  = agg_hhc_professional_location

        fields = ['prof_loc_id','srv_prof_id', 'name']
        
    def validate(self, data):
        return data


class agg_hhc_professional_location_details_serializer(serializers.ModelSerializer):
    class Meta:
        model  = agg_hhc_professional_location_details
        fields = ['prof_loc_dt_id','lattitude', 'longitude', 'prof_loc_id']

    def validate(self, data):
        return data
    

    
    

# ---------------------------------------- Professional Register ---------------------------
from hhcweb.models import Professional_status
class reg_prof_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_service_professionals
        fields = ['srv_id', 'title','prof_fullname','dob','gender','email_id','phone_no','alt_phone_no','eme_contact_no','eme_contact_relation',
                  'eme_conact_person_name','mode_of_service','availability_status','prof_zone_id','state_name','city','pin_code_id',
                  'prof_sub_srv_id','Education_level','cv_file','certificate_registration_no','availability']
    
    def create(self, validated_data):
        # You can set the enum value you want here
        validated_data['professinal_status'] = Professional_status.Info_Submitted

        instance = super(reg_prof_api_serializer, self).create(validated_data)
        return instance
    

# ------------------------------Professional document upload -------------------------------------------
class agg_hhc_add_document_serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_professional_documents
        fields = ['prof_doc_id','professional_id','doc_li_id','professional_document']

class professional_role(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_services
        fields = ['service_title','srv_id']

class agg_hhc_document_list_serializer(serializers.ModelSerializer):
    professional_role = professional_role()
    class Meta:
        model = agg_hhc_documents_list
        fields = ['doc_li_id','Documents_name','professional_role']

class agg_hhc_add_location_serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_professional_location
        fields = ['prof_loc_id','srv_prof_id','location_name']

class agg_hhc_add_dtl_location_serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_professional_location_details
        fields = ['prof_loc_dt_id','lattitude','longitude','prof_loc_id']
# -----------------------mayank-----------------------------app----------------------

class Upcoming_service_app(serializers.ModelSerializer):
    # service_title = serializers.CharField(source='agg_hhc_services.service_title')

    class Meta:
        model= agg_hhc_event_plan_of_care
        fields = ['start_date','end_date','srv_prof_id', 'eve_id','status','srv_id','pt_id']

    def to_representation(self, instance):
       # Serialize the instance using the default representation
       data = super().to_representation(instance)
       
       # Add the "service_title" field from the related "agg_hhc_services" instance
       data['service_title'] = instance.srv_id.service_title
       data['address'] = instance.pt_id.address
       data['name'] = instance.pt_id.name
       return data
    
    # def to_representation(self, instance):
    #    # Serialize the instance using the default representation
    #    data = super().to_representation(instance)
       
    #    data['address'] = instance.pt_id.address
    #    return data

# ----------------------------PROfessional app feedback----------------------

class agg_hhc_get_role_serializer(serializers.ModelSerializer):
   class Meta:
        model = agg_hhc_services
        fields = ['srv_id','service_title']


class Pro_app_feedback_serializer(serializers.ModelSerializer):
    models = agg_hhc_Professional_app_feedback
    fields = "__all__"







    # ----------------------------  Professional Ongoing service and session  --------------
class get_total_amt(serializers.ModelSerializer):
    class Meta:
        model = agg_hhc_events
        fields = []


class Ongoing_srv_sess_serializer(serializers.ModelSerializer):
    srv_id = professional_role()
    Total_amount = serializers.SerializerMethodField()
    Pending_amount = serializers.SerializerMethodField()
    

    class Meta:
        model = agg_hhc_event_plan_of_care
        fields = ['srv_prof_id', 'eve_id', 'srv_id', 'start_date', 'end_date', 'Total_amount',
                  'Pending_amount']

    def get_Total_amount(self, obj):
       
        event_id = obj.eve_id_id 
        total_amt = agg_hhc_events.objects.filter(eve_id=event_id).aggregate(Sum('final_amount'))['final_amount__sum']

        return total_amt if total_amt is not None else 0
    
    def get_Pending_amount(self, obj):
      
        event_id = obj.eve_id_id 

        total_amt_agg = agg_hhc_events.objects.filter(eve_id=event_id).aggregate(Sum('final_amount'))
        total_paid_agg = agg_hhc_payment_details.objects.filter(eve_id=event_id).aggregate(Sum('amount_paid'))

        total_amt = total_amt_agg['final_amount__sum']
        total_paid = total_paid_agg['amount_paid__sum']

        if total_amt is None:total_amt = 0.0 

        if total_paid is None:total_paid = 0.0  
        print(total_amt)
        print(total_paid)
        
        Pending_amt = total_amt - total_paid
        return Pending_amt
        