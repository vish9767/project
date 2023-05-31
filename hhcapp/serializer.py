from rest_framework import serializers
from . import models

class agg_hhc_app_caller_register_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_app_caller_register
        fields='__all__'

class webserializers(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_app_caller_register
        fields=['phone']
    def create(self,validated_data):
        return models.agg_hhc_app_caller_register.objects.create(**validated_data)
