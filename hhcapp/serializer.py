from rest_framework import serializers
from . import models

class agg_hhc_app_caller_register_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.agg_hhc_app_caller_register
        fields='__all__'