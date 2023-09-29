from rest_framework import serializers
<<<<<<< HEAD
from hhcweb import models as webmodel
class agg_hhc_service_professionals_serializer(serializers.Serializer):
    class Meta:
        model=webmodel.agg_hhc_service_professionals
        fields = '__all__'
    def create(self,validated_data):
        return webmodel.agg_hhc_service_professionals.objects.create(**validated_data)

class professional_role(serializers.ModelSerializer):
    class Meta:
        model = webmodel.agg_hhc_services
        fields = ['service_title','srv_id']

class agg_hhc_document_list_serializer(serializers.ModelSerializer):
    professional_role = professional_role()
    class Meta:
        model = webmodel.agg_hhc_documetns_list
        fields = ['doc_li_id','Documents_name','professional_role']

class agg_hhc_add_document_serializer(serializers.ModelSerializer):
    class Meta:
        model = webmodel.agg_hhc_professional_documents
        fields = ['prof_doc_id','professional_id','doc_li_id','professional_document']
=======
from hhcweb import models as webmodels
from hhcweb.models import agg_com_colleague
class agg_hhc_service_professionals_serializer(serializers.Serializer):
    class Meta:
        model=webmodels.agg_hhc_service_professionals
        # fields = '__all__'
        fields = ['srv_prof_id','phone_no', 'OTP']

    def validate(self, data):
        return data
        
    def create(self,validated_data):
        pro_obj = webmodels.agg_hhc_service_professionals.objects.create(**validated_data)
        return pro_obj
    

class UserRegistrationSerializer2(serializers.ModelSerializer):
    class Meta:
        model  = agg_com_colleague
        fields = ['pk','clg_mobile_no', 'clg_otp']

    def validate(self, data):
        return data
>>>>>>> 427c65131da3fdc2ccdbecbca89763431f9d3363
