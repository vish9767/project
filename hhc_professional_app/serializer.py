from rest_framework import serializers
from hhcweb.models import *

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
    pt_id = agg_hhc_patients

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



class Pro_app_feedback_serializer(serializers.ModelSerializer):
    models = agg_hhc_Professional_app_feedback
    fields = "__all__"