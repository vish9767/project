from rest_framework import serializers
from hhcweb import models



class agg_hhc_caller_relation_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_caller_relation
        fields = ['relation']           

class agg_hhc_locations_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_locations
        fields = ['location'] 


class agg_hhc_services_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_services
        fields = ['service_title'] 

class agg_hhc_sub_services_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_sub_services
        fields = ['recommomded_service'] 

 

# -------------------------------------------------------------------------------------------------------------
class agg_hhc_purpose_call_serializer(serializers.ModelSerializer):#25
    class Meta:
        model=models.agg_hhc_purpose_call
        fields='__all__'
        


class agg_hhc_gender_serializer(serializers.ModelSerializer):#112
    class Meta:
        model=models.agg_hhc_gender
        fields='__all__'

