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
            # print("this is last patient ",a)
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
    
class AddPatientOrCheckCallerExist(APIView):
    def post(self, request):
        serialized = serializers.AddPatientOrCheckCallerExistSerializer.model1
####_______________________________agg_hhc_patinet_list_enquiry_______________##

class agg_hhc_patinet_list_enquiry_api(APIView):
    def post(self,request):
        serialized=serializers.agg_hhc_patinet_list_enquiry_serializer(data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        record=models.agg_hhc_patinet_list_enquiry.objects.all()
        serialized=serializers.agg_hhc_patinet_list_enquiry_serializer(record,many=True)
        return Response(serialized.data)
    
class agg_hhc_patinet_list_enquiry_put(APIView):
    def get_object(self,request,pk):
        try:
            return models.agg_hhc_patinet_list_enquiry.objects.filter(pk=pk)
        except models.agg_hhc_patinet_list_enquiry.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk):
        obj=self.get_object(pk)
        serialized=serializers.agg_hhc_patinet_list_enquiry_serializer(obj)
        return Response(serialized.data)
    def put(self,request,pk):
        obj=self.get_object(pk)
        serialized=serializers.agg_hhc_patinet_list_enquiry_serializer(obj,data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
class agg_hhc_service_professional_details(APIView):
    def get(self,request):
        records=models.agg_hhc_service_professional_details.all()
        serializer=serializers.agg_hhc_service_professional_details_serializer(records,many=True)
        return Response(serializer.data)

class agg_hhc_callers_api(APIView):
    def get(self,request):
        record=models.agg_hhc_callers.objects.filter(status=1)
        serailized=serializers.agg_hhc_callers_seralizer(record,many=True)
        return Response(serailized.data)
    

class agg_hhc_web_patient_by_caller_phone_no(APIView):
    def get_object(self,pk):
        try:
            #print("this is my id ",pk)
            #print("this is my data",webmodel.agg_hhc_patients.objects.filter(app_user_id=pk))
            return models.agg_hhc_patients.objects.filter(caller_id=pk)
        except models.agg_hhc_patients.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, pk, format=None):
        #print("this is inside get",pk)
        snippet= self.get_object(pk)
        serialized =serializers.agg_hhc_app_patient_by_caller_phone_no(snippet,many=True)
        return Response(serialized.data)
    

class agg_hhc_callers_phone_no(APIView):
    def get_object(self,pk):
        queryset = models.agg_hhc_callers.objects.get(phone_no=pk)#.values_list('caller_id',flat=True)
        #blogs = queryset.values_list('caller_id', flat=True)
        print("This is get:",queryset.caller_id)
        query_id=queryset.caller_id
        #print('this is query:',list(queryset))
        return query_id #8888888888
    def get(self,request,pk,format=None):
        snippet=self.get_object(pk)
        record=models.agg_hhc_patients.objects.filter(caller_id=snippet)
        print("this is snippet",snippet)
        serialized=serializers.agg_hhc_app_patient_by_caller_phone_no(record,many=True)
        return Response(serialized.data)