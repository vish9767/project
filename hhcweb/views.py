import datetime
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcweb import serializers
from hhcweb import models
import json
from rest_framework import status,permissions
from django.utils import timezone
from hhcweb.serializers import UserRegistrationSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from hhcweb.renders import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.







# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    group = str(user.grp_id)
    if group:
            incs=models.agg_mas_group.objects.get(grp_id=group)
            group = incs.grp_name
    return {
        "refresh" : str(refresh),
        "access" : str(refresh.access_token),
        "colleague": {
                'id': user.id,
                'first_name': user.clg_first_name,
                'last_name': user.clg_last_name,
                'email': user.clg_email,
                'clg_group': group
            },
        "user_group" :group,
    } 

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            print(token)
            return Response({'token':token,'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            clg_ref_id = serializer.data.get('clg_ref_id')
            password = serializer.data.get('password')
            print(clg_ref_id, password)
            user = authenticate(clg_ref_id=clg_ref_id, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Logged in Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['UserId or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    
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
    def get(self,request,pk,format=None):
        sub_service=models.agg_hhc_sub_services.objects.filter(srv_id=pk)
        serializer=serializers.agg_hhc_sub_services_serializer(sub_service,many=True)
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
        phone = request.data.get('phone_no')
        print("this is my phone_no",phone)
        old_patient=models.agg_hhc_patients.objects.filter(phone_no=phone).first()
        print("this is old patients",old_patient)
        if(old_patient is None):
            serializer=serializers.agg_hhc_patients_serializer(data=request.data)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            print(" patient is not available ")
            #print("old patient hhc_no",old_patient.hhc_code)
            #models.agg_hhc_patients.objects.create(phonehhc_code=old_patient.hhc_code,name=request.data.get('name'),first_name=request.data.get('first_name'),middle_name=request.data.get('middle_name'),Age=request.data.get('Age'),Gender=request.data.get('Gender'),email_id=request.data.get('email_id')otp_expire_time=datetime.now()+timedelta(minutes=2))
            se=serializers.agg_hhc_patients_serializer(data=request.data)
            if(se.is_valid()):
                se.validated_data['hhc_code'] =old_patient.hhc_code #old_patient.hhc_code
                se.save()
                return Response(se.data)
            return Response({'patient available with that number':phone})
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
    def get(self,request):
        record=models.agg_hhc_callers.objects.filter(status=1)
        serailized=serializers.agg_hhc_callers_seralizer(record,many=True)
        return Response(serailized.data)
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

class agg_hhc_add_service_details_api(APIView):
    def post(self,request,pk):
        serialized=serializers.agg_hhc_add_service_serializer(data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
class agg_hhc_service_professional_details(APIView):
    def get(self,request):
        records=models.agg_hhc_service_professional_details.all()
        serializer=serializers.agg_hhc_service_professional_details_serializer(records,many=True)
        return Response(serializer.data)
    
#--------------------------get all patients from caller id -----------------------------

class agg_hhc_callers_phone_no(APIView):
    def get_object(self,pk):
        queryset = models.agg_hhc_callers.objects.get(phone=pk)#.values_list('caller_id',flat=True)
        print("This is get:",queryset.caller_id)
        query_id=queryset.caller_id
        #print('this is query:',list(queryset))
        return query_id #8888888888
    def get(self,request,pk,format=None):
        snippet=self.get_object(pk)
        caller_record=models.agg_hhc_callers.objects.get(pk=snippet)
        record=models.agg_hhc_patients.objects.filter(caller_id=snippet)
        serialized_caller=serializers.agg_hhc_callers(caller_record)
        serialized=serializers.agg_hhc_app_patient_by_caller_phone_no(record,many=True)
        return Response({"caller": serialized_caller.data, "patients": serialized.data})

#----------patients from callers_enum status---------------------
class agg_hhc_callers_phone_no_status_mobile_api(APIView):#staus=1
    def get(self,request):
        record=models.agg_hhc_callers.objects.filter(caller_status=1)
        print(record)
        serialized=serializers.agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

class agg_hhc_callers_phone_no_status_web_api(APIView):#staus=2
    def get(self,request):
        record=models.agg_hhc_callers.objects.filter(caller_status=2)
        print(record)
        serialized=serializers.agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

class agg_hhc_callers_phone_no_status_walking_api(APIView):#staus=3
    def get(self,request):
        record=models.agg_hhc_callers.objects.filter(caller_status=3)
        print(record)
        serialized=serializers.agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

class agg_hhc_callers_phone_no_status_calling_api(APIView):#staus=4
    def get(self,request):
        record=models.agg_hhc_callers.objects.filter(caller_status=4)
        print(record)
        serialized=serializers.agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

#---------------------------get all hospital names-----------------------------------

class agg_hhc_hospitals_api(APIView):
    def get(self,request):
        hospital=models.agg_hhc_hospitals.objects.filter(status=1)
        hospital_names=serializers.agg_hhc_hospitals_serializer(hospital,many=True)
        return Response(hospital_names.data)

#-------------------------get address by pincode-------------------------------------
class agg_hhc_pincode_api(APIView):
    def get(self,request):
        pincode=models.agg_hhc_pincode.objects.all()
        serialized=serializers.agg_hhc_pincode_serializer(pincode,many=True)
        return Response(serialized.data)

class agg_hhc_pincode_number_api(APIView):
    def get_object(self,pin):
        try:
            return models.agg_hhc_pincode.objects.get(pincode_number=pin)
        except models.agg_hhc_pincode.DoesNotExist:
            raise Response(status.HTTP_404_NOT_FOUND)
    def get(self,request,pin):
        obj=self.get_object(pin)
        serialized=serializers.agg_hhc_pincode_serializer(obj)
        return Response(serialized.data)

class agg_hhc_city_from_state_api(APIView):
    def get_object(self,state,formate=None):
        try:
            return models.agg_hhc_city.objects.filter(state_name=state)
        except models.agg_hhc_city.DoesNotExist:
            raise Response(status.HTTP_404_NOT_FOUND)
    def get(self,request,state):
        state_obj=self.get_object(state)
        serialized=serializers.agg_hhc_city(state_obj,many=True)
        return Response(serialized.data)

class agg_hhc_pincode_from_city_api(APIView):
    def get_object(self,city,formate=None):
        try:
            a=models.agg_hhc_pincode.objects.filter(city_name=city)
            return models.agg_hhc_pincode.objects.filter(city_name=city)
        except models.agg_hhc_pincode.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,city):
        pincode_obj=self.get_object(city)
        serialized=serializers.agg_hhc_pincode_serializer(pincode_obj,many=True)
        return Response(serialized.data)
class Caller_details_api(APIView):
    def get_object(self,pk):
        return models.agg_hhc_callers.objects.get(caller_id=pk)
            
    def get_relation(self,pk):
        return models.agg_hhc_caller_relation.objects.filter(pk=pk)
             
    def get(self,request,pk):   
        caller = self.get_object(pk)
        if caller:
            serializer = serializers.Caller_details_serializer(caller)
            relation=(self.get_relation(serializer.data['caller_rel_id']))[0]
            relations=serializers.relation_serializer(relation)
            return Response({"caller":serializer.data,"relation":relations.data})
        else:
            return Response({"error": 'user not found'})
        
    def put(self,request,pk):
        caller = self.get_object(pk)
        callerSerializer = serializers.Caller_details_serializer(caller,data = request.data)
        if callerSerializer.is_valid():
            callerSerializer.validated_data['last_modified_date']=timezone.now()
            callerSerializer.save()
            return Response(callerSerializer.data)
        return Response(callerSerializer.errors)
    
class patient_detail_info_api(APIView):
    def get_patient(self,pk):
        return models.agg_hhc_patients.objects.get(agg_sp_pt_id=pk)
    
    def get_hospital(self, pk):
        return models.agg_hhc_hospitals.objects.get(hosp_id=pk)
    
    def get(self, request, pk):
        patient = self.get_patient(pk)
        if patient:
            serializer = serializers.patient_detail_serializer(patient)
            hospital = self.get_hospital(serializer.data['hosp_id'])
            if hospital:
                hospitals = serializers.hospital_serializer(hospital)
                return Response({"patient": serializer.data, "hospital": hospitals.data})

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        patient = self.get_patient(pk)
        serializer = serializers.patient_detail_serializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['last_modified_date'] = timezone.now() #old_patient.hhc_code
        serializer.save()
        return Response(serializer.data)

# ----------------------------------------------professional availability details name and skills -----
class  agg_hhc_service_professionals_api(APIView):
    def get(self,request,formate=None):
        professional=models.agg_hhc_service_professionals.objects.filter(status=1)
        serialized=serializers.agg_hhc_service_professionals_serializer(professional,many=True)
        return Response(serialized.data)
    

class calculate_discount_api(APIView):
    def get(self, request):#dtype,amount,total_amt
        dtype=request.data['dtype']
        amount=request.data['amount']
        total_amt=request.data['total_amt']
        if dtype == 1:
            final= ((total_amt*amount)/100)-total_amt
            return Response({"final_amount":final})
        elif dtype == 2:
            final = (total_amt-amount)
            return Response({"final_amount":final})
        else: return Response({"final_amount":total_amt})



class calculate_total_amount(APIView):
    def get(self, request):
        print(request.data)
        start_date_string = request.data['start_date']
        end_date_string = request.data['end_date']  
        print(start_date_string)     
        try:
            start_date = datetime.datetime.strptime(str(start_date_string), '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(str(end_date_string), '%Y-%m-%d').date()            
            diff = (end_date - start_date).days 
            total = (diff+1) * request.data['srv_cost']           
            return Response({'days_difference': total})
        except ValueError:
            return Response({'error': 'Invalid date format'}, status=400)
        

#------------------------------agg_hhc_professional_scheduled---used to display professional booked services --this will be used to display professiona record in calander

class agg_hhc_professional_scheduled_api(APIView):
    def get_object(self,prof_sche_id,formate=None):
        try:
            return models.agg_hhc_professional_scheduled.objects.filter(srv_prof_id=prof_sche_id,status=1)
        except models.agg_hhc_professional_scheduled.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,prof_sche_id):
        timeobject=self.get_object(prof_sche_id)
        serialized=serializers.agg_hhc_professional_scheduled_serializer(timeobject,many=True)
        return Response(serialized.data)

#--------------------------agg_hhc_professional_scheduled_api---used to display professional booked services in professional Avalibility

class agg_hhc_professional_time_availability_api(APIView):
    def get_object(self,prof_sche_id,formate=None):
        try:
            return models.agg_hhc_professional_scheduled.objects.filter(srv_prof_id=prof_sche_id,status=1,scheduled_date=timezone.now())
        except models.agg_hhc_professional_scheduled.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,prof_sche_id):
        dateobject=self.get_object(prof_sche_id)
        serialized=serializers.agg_hhc_professional_scheduled_serializer(dateobject,many=True)
        return Response(serialized.data)
    
#-------------------------agg_hhc_event_professional_serializer-------------------

#class agg_hhc_event_professional_serializer(APIView):
#    def post(self,request):
#        try:









class LogoutView(APIView):
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'msg':'Token is blacklisted successfully.'},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'msg':'Bad Request'},status=status.HTTP_400_BAD_REQUEST)