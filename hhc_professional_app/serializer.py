from rest_framework import serializers
from hhcweb import models as webmodels
class agg_hhc_service_professionals_serializer(serializers.Serializer):
    class Meta:
        model=webmodels.agg_hhc_service_professionals
        fields = '__all__'
    def create(self,validated_data):
        return webmodels.agg_hhc_service_professionals.objects.create(**validated_data)