from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcweb import serializers
from hhcweb import models
# Create your views here.
    
class agg_hhc_caller_relation_api(APIView):
    def get(self,request):
        courses = models.agg_hhc_caller_relation.objects.filter(status=1)
        serializer = serializers.agg_hhc_caller_relation_serializer(courses, many=True)
        return Response(serializer.data)
    
class agg_hhc_locations_api(APIView):
    def get(self,request):
        courses = models.agg_hhc_locations.objects.filter(status=1)
        serializer = serializers.agg_hhc_locations_serializer(courses, many=True)
        return Response(serializer.data)

class agg_hhc_services_api(APIView):
    def get(self,request):
        call=models.agg_hhc_services.objects.filter(status=1)
        serializer=serializers.agg_hhc_services_serializer(call,many=True)
        return Response(serializer.data)
    
class agg_hhc_sub_services_api(APIView):
    def get(self,request):
        call=models.agg_hhc_sub_services.objects.filter(status=1) 
        serializer=serializers.agg_hhc_sub_services_serializer(call,many=True)
        return Response(serializer.data)
#------------------------------------------------------------------------------
class agg_hhc_purpose_call_api(APIView):
    def get(self,request):
        call=models.agg_hhc_purpose_call.objects.filter(status=1) 
        serializer=serializers.agg_hhc_purpose_call_serializer(call,many=True)
        return Response(serializer.data)
    

class agg_hhc_gender_api(APIView):
    def get(self,request):
        ge=models.agg_hhc_gender.objects.filter(status=1)
        serializer=serializers.agg_hhc_gender_serializer(ge,many=True)
        return Response(serializer.data)












































































