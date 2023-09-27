from rest_framework import serializers
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