from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcweb import serializers
from hhcweb import models
from rest_framework import status
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

class agg_hhc_patients_api(APIView):
    def post(self,request):
        serializer=serializers.agg_hhc_patients_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        reg=models.agg_hhc_patients.objects.filter(status=1)
        ref=serializers.agg_hhc_patients_serializer(reg,many=True)
        return Response(ref.data)
    

#_________________________________________get_latest_patient_record_from_caller_id__________________
class get_latest_patient_record_from_caller_id_api(APIView):
    def get_object(self,pk):
        try:
            a=models.agg_hhc_patients.objects.filter(caller_id=pk).latest('pk')
            print("this is last patient ",a)
            return a
        except models.agg_hhc_patients.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, pk, format=None):
        snippet= self.get_object(pk)
        serialized =serializers.get_latest_patient_record_from_caller_id(snippet)
        return Response(serialized.data)

######___________________________agg_hhc_callers_Api__________________#########

class agg_hhc_callers_api(APIView):
    def post(self,request):
        serialized=serializers.agg_hhc_callers_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)