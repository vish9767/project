from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcweb.serializers import *
from hhcweb.models import *
import json
from django.db.models import Q
from rest_framework import status,permissions
from django.utils import timezone
# from hhcweb.serializers import UserRegistrationSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from hhcweb.renders import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# from .models import agg_hhc_service_professionals, agg_hhc_professional_sub_services
# from .serializers import AggHHCServiceProfessionalSerializer
# from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import generics
# from .models import agg_hhc_service_professionals
# from .serializers import AggHHCServiceProfessionalSerializer
from rest_framework.decorators import api_view


# Create your views here.





#-----------------------------------------------jwt login and register api---------------------------

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    group = str(user.grp_id)
    if group:
            incs= agg_mas_group.objects.get(grp_id=group)
            group = incs.grp_name
    return {
        "refresh" : str(refresh),
        "access" : str(refresh.access_token),
        "colleague": {
                'id': user.id,
                'first_name': user.clg_first_name,
                'last_name': user.clg_last_name,
                'email': user.clg_work_email_id,
                'phone_no': user.clg_mobile_no,
                'profile_photo_path':user.clg_profile_photo_path,
                'address':user.clg_address,
                'designation':user.clg_designation,
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





#---------------------------------------------------Api's Starts------------------------------     
class agg_hhc_caller_relation_api(APIView):
    def get(self,request):
        courses =  agg_hhc_caller_relation.objects.filter(status=1)
        serializer = agg_hhc_caller_relation_serializer(courses, many=True)
        return Response(serializer.data)    

class agg_hhc_locations_api(APIView):
    def get(self,request):
        courses =  agg_hhc_locations.objects.filter(status=1)
        serializer = agg_hhc_locations_serializer(courses, many=True)
        return Response(serializer.data)

class agg_hhc_services_api(APIView):
    def get(self,request):
        call= agg_hhc_services.objects.filter(status=1)
        serializer=agg_hhc_services_serializer(call,many=True)
        return Response(serializer.data)

class agg_hhc_sub_services_api(APIView):
    def get(self,request,pk,format=None):
        sub_service= agg_hhc_sub_services.objects.filter(srv_id=pk)
        serializer= agg_hhc_sub_services_serializer(sub_service,many=True)
        return Response(serializer.data)
    

#------------------------------------------------------------------------------
class agg_hhc_purpose_call_api(APIView):
    def get(self,request):
        call= agg_hhc_purpose_call.objects.filter(status=1) 
        serializer= agg_hhc_purpose_call_serializer(call,many=True)
        return Response(serializer.data)
    

class agg_hhc_gender_api(APIView):
    def get(self,request):
        ge= agg_hhc_gender.objects.filter(status=1)
        serializer= agg_hhc_gender_serializer(ge,many=True)
        return Response(serializer.data)

class agg_hhc_patients_api(APIView):
    def post(self,request):
        phone = request.data.get('phone_no')
        print("this is my phone_no",phone)
        old_patient= agg_hhc_patients.objects.filter(phone_no=phone).first()
        print("this is old patients",old_patient)
        if(old_patient is None):
            serializer= agg_hhc_patients_serializer(data=request.data)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            print(" patient is not available ")
            #print("old patient hhc_no",old_patient.hhc_code)
            # agg_hhc_patients.objects.create(phonehhc_code=old_patient.hhc_code,name=request.data.get('name'),first_name=request.data.get('first_name'),middle_name=request.data.get('middle_name'),Age=request.data.get('Age'),Gender=request.data.get('Gender'),email_id=request.data.get('email_id')otp_expire_time=datetime.now()+timedelta(minutes=2))
            se= agg_hhc_patients_serializer(data=request.data)
            if(se.is_valid()):
                se.validated_data['hhc_code'] =old_patient.hhc_code #old_patient.hhc_code
                se.save()
                return Response(se.data)
            return Response({'patient available with that number':phone})
    def get(self,request):
        reg= agg_hhc_patients.objects.filter(status=1)
        ref= agg_hhc_patients_serializer(reg,many=True)
        return Response(ref.data)
    

#_________________________________________get_latest_patient_record_from_caller_id__________________
class get_latest_patient_record_from_caller_id_api(APIView):
    def get_object(self,pk):
        try:
            a= agg_hhc_patients.objects.filter(caller_id=pk).latest('pk')
            # print("this is last patient ",a)
            return a
        except  agg_hhc_patients.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, pk, format=None):
        snippet= self.get_object(pk)
        serialized = get_latest_patient_record_from_caller_id(snippet)
        return Response(serialized.data)

######___________________________agg_hhc_callers_Api__________________#########

class agg_hhc_callers_api(APIView):
    def get(self,request):
        record= agg_hhc_callers.objects.filter(status=1)
        serailized= agg_hhc_callers_seralizer(record,many=True)
        return Response(serailized.data)
    def post(self,request):
        serialized= agg_hhc_callers_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class AddPatientOrCheckCallerExist(APIView):
#     def post(self, request):
#         serialized =  serializers.AddPatientOrCheckCallerExistSerializer.model1
####_______________________________agg_hhc_patinet_list_enquiry_______________##

# class agg_hhc_patinet_list_enquiry_api(APIView):
#     def post(self,request):
#         serialized= agg_hhc_patinet_list_enquiry_serializer(data=request.data)
#         if(serialized.is_valid()):
#             serialized.save()
#             return Response(serialized.data,status=status.HTTP_201_CREATED)
#         return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
#     def get(self,request):
#         record= agg_hhc_patient_list_enquiry.objects.all()
#         serialized= agg_hhc_patinet_list_enquiry_serializer(record,many=True)
#         return Response(serialized.data)
    
class agg_hhc_patinet_list_enquiry_put(APIView):
    def get_object(self,request,pk):
        try:
            return  agg_hhc_patient_list_enquiry.objects.filter(pk=pk)
        except  agg_hhc_patient_list_enquiry.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk):
        obj=self.get_object(pk)
        serialized= agg_hhc_patinet_list_enquiry_serializer(obj)
        return Response(serialized.data)
    def put(self,request,pk):
        obj=self.get_object(pk)
        serialized= agg_hhc_patinet_list_enquiry_serializer(obj,data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)

# ------------------------------ Sandip Shimpi ---------------------------------------------- 
class agg_hhc_patient_by_HHCID(APIView):

    def get_patient(self,pk):
        try:
            return agg_hhc_patients.objects.get(hhc_code=pk)
        except agg_hhc_patients.DoesNotExist:
            return status.HTTP_404_NOT_FOUND        

    def get(self,request,pk):
        patient = self.get_patient(pk)
        patient=Patient_by_HHCID_Serializer(patient)
        return Response(patient.data)
    
class agg_hhc_add_service_details_api(APIView):
    
    def get_event(self,pk):
        try:
            event = agg_hhc_events.objects.get(eve_id=pk)
            return Response(event)
        except agg_hhc_events.DoesNotExist:
            return Response('please enter valid event id',status.HTTP_404_NOT_FOUND)
        
        
    def get_caller(self,phone):
        try:
            return agg_hhc_callers.objects.get(phone=phone)
        except agg_hhc_callers.DoesNotExist:
            return None

    def get_patient(self,phone_no):
        try:
            return agg_hhc_patients.objects.get(phone_no=phone_no)
        except agg_hhc_patients.DoesNotExist:
            return None


    def get(self,request,pk):
        event = self.get_event(pk)
        if not event:
            return Response(status.HTTP_404_NOT_FOUND)
        callerserializer =  add_service_get_caller_serializer(event.data.caller_id)
        patientserializer = add_service_get_patient_serializer(event.data.pt_id)
        plan_of_care = agg_hhc_event_plan_of_care.objects.filter(eve_id=pk)
        plan_of_care_serializer = add_service_get_POC_serializer(plan_of_care,many=True)
        return Response({'caller_details':callerserializer.data,'patient_details':patientserializer.data,'POC':plan_of_care_serializer.data})

    def post(self,request):  
        patientID=None  
        caller = agg_hhc_callers.objects.filter(phone=request.data['phone']).first()
        # print('1')
        if caller:
            callerSerializer= agg_hhc_callers_serializer(caller,data= request.data)
            if callerSerializer.is_valid():
                callerID=callerSerializer.save()
                callerID=callerID.caller_id
                # print('2')
            else:
                return Response(callerSerializer.errors)
            # caller.update(caller_fullname=request.data['caller_fullname'], caller_rel_id=request.data['caller_rel_id'], purp_call_id=request.data['purp_call_id'], caller_status=3)
            # callerID = caller.first().caller_id 
        else:  
            callers= agg_hhc_callers_serializer(data= request.data)
            if callers.is_valid():
                # callers.validated_data['caller_status']=3
                callerID=callers.save().caller_id
                # print('3')
            else:
                return Response([callers.errors])
        # print(callerID,'llllsecond')
        if request.data['purp_call_id']==1:
            # print('4')
            patient= agg_hhc_patients.objects.filter(phone_no=request.data['phone_no']).first()
            if patient:
                # patient.update(name=request.data['name'], phone_no=request.data['phone_no'],caller_id=callerID,Age=request.data['Age'] )
                # patientID=patient.first().agg_sp_pt_id 
                request.data['caller_id']=callerID
                patientSerializer = agg_hhc_patients_serializer(patient,data=request.data)
                if patientSerializer.is_valid():
                    # patientSerializer.validated_data['caller_id']=callerID
                    patientID=patientSerializer.save().agg_sp_pt_id
                    # print('5')
                else: return Response(patientSerializer.errors)
            else:
                patient = agg_hhc_patients_serializer(data=request.data)
                request.data['caller_id']=callerID
                if patient.is_valid():
                    # print(patient,'pppppppppppppp')
                    # patient.validated_data['caller_id']=callerID
                    patientID=patient.save().agg_sp_pt_id
                    # patientID=patientID.agg_sp_pt_id
                else:
                    return Response([patient.errors])
                # print('4.6')                
        elif request.data['purp_call_id']==2:
            patient= agg_hhc_patient_list_enquiry.objects.filter(phone_no=request.data['phone_no']).first()
            request.data['caller_id']=callerID
            if patient:
                # print(patient,'7')
                patientSerializer = agg_hhc_patient_list_serializer(patient,data=request.data)
                if patientSerializer.is_valid():
                    # patientSerializer.validated_data['caller_id']=callerID
                    # print(patientSerializer)
                    # print('pppppppppppppppppppppppppp')
                    patientID=patientSerializer.save().pt_id
                    # for items in patientID:

                    # print(patientID.eve_id)
                    #     items.pt_id
                    # patientID=patientID.pt_id

                    # saved_patients = []
                    # for patient_instance in patientSerializer.save():
                    #     saved_patients.append(patient_instance)
                else:
                    # print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
                    return Response(patientSerializer.errors)
                # patient.update(name=request.data['name'], phone_no=request.data['phone_no'],caller_id=callerID,Age=request.data['Age'] )
                # patientID=patient.first().pt_id 
            else:
                request.data['caller_id']=callerID
                patient = agg_hhc_patient_list_serializer(data=request.data)
                # print('9')
                if patient.is_valid():
                    patientID=patient.save()
                    patientID=patientID.pt_id
                    # print('10')
                else:
                    return Response([patient.errors])

        # else:
        #     patient=models.agg_hhc_patient_list_enquiry.objects.filter(phone_no=request.data['phone_no'])
        # # if patient:
        # #     patient.update(name=request.data['name'], phone_no=request.data['phone_no'],caller_id=callerID )
        # #     patientID=patient.first().agg_sp_pt_id 
        # else:
        #     patient = serializers.agg_hhc_patients_serializer(data=request.data)
        #         # patient = serializers.agg_hhc_patient_list_serializer(data=request.data)
        #     if patient.is_valid():
        #         # patient.validated_data['caller_id']=callerID
        #         # print(patient.validated_data['caller_id'],';;;;;;;;;;;;;;;;;;;;;;;;')
        #         patientID=patient.save()
        #         patientID=patientID.agg_sp_pt_id

        #     else:
        #         return Response(patient.errors)
        # print(callerID,'ll;;;l')
        # print(patientID,'ll;;;l')
        request.data['event_status']=1
        event= agg_hhc_event_serializer(data=request.data)
        if event.is_valid():
            eventID=event.save().eve_id
            request.data.pop('event_status')
        else:
            return Response([event.errors])
        event= agg_hhc_events.objects.filter(eve_id=eventID)
        if request.data['purp_call_id']==1:
            # print('spero service')
            event.update(agg_sp_pt_id=patientID,caller_id=callerID,patient_service_status=3)
        elif request.data['purp_call_id']==2:
            # print('enquiry')
            event.update(pt_id=patientID,caller_id=callerID)
        # data=request.data['sub_srv_id']
        start_date = datetime.strptime(str(request.data['start_date']), '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(str(request.data['end_date']), '%Y-%m-%d %H:%M:%S')
        diff = ((end_date.date() - start_date.date()).days)
        a=[request.data['sub_srv_id']]
        # for sub_srv in request.data['sub_srv_id']:    for multiple sub services
        event_plane_of_care=[]
        for sub_srv in a:
            request.data['sub_srv_id']=sub_srv 
                # request.data['start_date']=request.data['actual_StartDate_Time']
                # request.data['end_date']=request.data['actual_EndDate_Time']
            add_service= agg_hhc_create_service_serializer(data=request.data)
            if add_service.is_valid():
                service=add_service.save().eve_poc_id
                # print(service)
            else:
                return Response([add_service.errors])
            plan_O_C= agg_hhc_event_plan_of_care.objects.filter(eve_poc_id=service)
            plan_O_C.update(eve_id=eventID)
            event_plane_of_care.append(service)
            if request.data['purp_call_id']==1:
                for i in range(0,(diff+1)):
                    start_date_string=start_date+timedelta(days=i)
                    request.data['actual_StartDate_Time']=start_date_string
                    request.data['actual_EndDate_Time']=datetime.combine(start_date_string.date(),end_date.time())
                    detailPlaneofcare= agg_hhc_add_detail_service_serializer(data=request.data)
                    if detailPlaneofcare.is_valid():
                        # detailPlaneofcare.eve_poc_id=service
                        # detailPlaneofcare.eve_id=eventID
                        # detailPlaneofcare.index_of_Session=(i+1)
                        detail_plan=detailPlaneofcare.save().agg_sp_dt_eve_poc_id
                    else:
                        return Response([detailPlaneofcare.errors])
                    data1= agg_hhc_detailed_event_plan_of_care.objects.filter(agg_sp_dt_eve_poc_id=detail_plan)
                    data1.update(eve_poc_id=service,eve_id=eventID,index_of_Session=(i+1))
        if request.data['purp_call_id']==1: 
            # return Response({"Service Created Event Code":[eventID,eventID.agg_sp_pt_id]})
            event=agg_hhc_events.objects.get(eve_id=eventID)
            events=agg_hhc_event_response_serializer(event)
            return Response({"Service Created Event Code":[{"event_id":eventID},events.data,{"event_plan_of_care_id":event_plane_of_care}]})

        else:
            return Response({"Service Created Event Code":eventID})
        
    def get_event(self,pk):
        try:
            event = agg_hhc_events.objects.filter(eve_id=pk)[0]
            return Response(event)
        except agg_hhc_events.DoesNotExist:
            return Response('please enter valid event id',status.HTTP_404_NOT_FOUND)
        
        
    def get_caller(self,phone):
        try:
            return agg_hhc_callers.objects.get(phone=phone)
        except agg_hhc_callers.DoesNotExist:
            return None

    def get_patient(self,phone_no):
        try:
            return agg_hhc_patients.objects.get(phone_no=phone_no)
        except agg_hhc_patients.DoesNotExist:
            return None


    def put(self,request,pk):    
        # event=self.get_event(pk)
        caller = self.get_caller(phone=request.data['phone'])
        # print(caller.__dict__.items(),'llklll')
        # print(';')
        if caller:
            # caller.update(caller_fullname=request.data['caller_fullname'], caller_rel_id=request.data['caller_rel_id'], purp_call_id=request.data['purp_call_id'], caller_status=3)
            # caller.update(caller_fullname=request.data['caller_fullname'], caller_rel_id=request.data['caller_rel_id'], purp_call_id=request.data['purp_call_id'], caller_status=3)
            # callerID = caller.first().caller_id 
            callerSerializer= agg_hhc_callers_serializer(caller,data= request.data)
            if callerSerializer.is_valid():
                callerID=callerSerializer.save().caller_id
            else:
                return Response(callerSerializer.errors)
        else:  
            callers= agg_hhc_callers_serializer(data= request.data)
            if callers.is_valid():
                # callers.validated_data['caller_status']=3
                callerID=callers.save().caller_id
            else:
                return Response([callers.errors])   
        # # print(callerID,'llllsecond')
        # if request.data['purp_call_id']==1:
        # print('l')
        patient=self.get_patient(phone_no=request.data['phone_no'])
        # print(patient,';;;;;;;;;;;;;;;')
        if patient:
            # patient.update(name=request.data['name'], phone_no=request.data['phone_no'],caller_id=callerID,Age=request.data['Age'] )
            # patientID=patient.first().agg_sp_pt_id 
            patientSerializer= agg_hhc_patients_serializer(patient,data=request.data)
            if patientSerializer.is_valid():
                patientID=patientSerializer.save().agg_sp_pt_id
                # print(patientID,';;;;;;;;;;;;;;;;;;')
                # return Response(patientSerializer.data)
            else:
                return Response(patientSerializer.errors)
            
        else:
            patient = agg_hhc_patients_serializer(data=request.data)
            if patient.is_valid():
                patient.validated_data['caller_id']=callerID
                patientID=patient.save()
                patientID=patientID.agg_sp_pt_id
            else:
                return Response([patient.errors])
        # else:
        #     patient=models.agg_hhc_patient_list_enquiry.objects.filter(Q(phone_no=request.data['phone_no'])|Q())
        #     if patient:
        #         patient.update(name=request.data['name'], phone_no=request.data['phone_no'],caller_id=callerID,Age=request.data['Age'] )
        #         patientID=patient.first().pt_id 
        #     else:
        #         patient = serializers.agg_hhc_patient_list_serializer(data=request.data)
        #         if patient.is_valid():
        #             patientID=patient.save()
        #             patientID=patientID.pt_id
        #         else:
        #             return Response([patient.errors,'7'])

        # if event.is_valid():
        #     eventID=event.save().eve_id
        # else:
        #     return Response([event.errors,'8'])
        print(pk,'llllllllllll')
        event=self.get_event(pk)
        # if request.data['purp_call_id']==1:
        data={'agg_sp_pt_id':patientID,'caller_id':callerID,'status':1}
        eventSerializer= agg_hhc_updateIDs_event_serializer(event.data,data=data)
        if eventSerializer.is_valid():
           eventID=eventSerializer.save().eve_id
            # print(eventSerializer.validated_data)
            # eventSerializer.save()
        else:
            return Response(eventSerializer.errors)

            
        # event.update(agg_sp_pt_id=patientID,caller_id=callerID)
        # eventID=event.first().eve_id
        # print(eventID)
        # print(callerID)
        # else:
        #     event.update(pt_id=patientID,caller_id=callerID)
        start_date = datetime.strptime(str(request.data['start_date']), '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(str(request.data['end_date']), '%Y-%m-%d %H:%M:%S')
        diff = ((end_date.date() - start_date.date()).days)
        a=[request.data['sub_srv_id']]
        event_plane_of_care=[]
        for sub_srv in a:
            request.data['sub_srv_id']=sub_srv 
            add_service= agg_hhc_create_service_serializer(data=request.data)
            if add_service.is_valid():
                service=add_service.save().eve_poc_id
            else:
                return Response([add_service.errors])
            plan_O_C= agg_hhc_event_plan_of_care.objects.filter(eve_poc_id=service)
            plan_O_C.update(eve_id=eventID)
            event_plane_of_care.append(service)
            if request.data['purp_call_id']==1:
                for i in range(0,(diff+1)):
                    start_date_string=start_date+timedelta(days=i)
                    request.data['actual_StartDate_Time']=start_date_string
                    request.data['actual_EndDate_Time']=datetime.combine(start_date_string.date(),end_date.time())
                    detailPlaneofcare= agg_hhc_add_detail_service_serializer(data=request.data)
                    if detailPlaneofcare.is_valid():
                        detailPlaneofcare.eve_poc_id=service
                        detailPlaneofcare.eve_id=eventID
                        detail_plan=detailPlaneofcare.save().agg_sp_dt_eve_poc_id
                    else:
                        return Response([detailPlaneofcare.errors,'000'])
                    data1= agg_hhc_detailed_event_plan_of_care.objects.filter(agg_sp_dt_eve_poc_id=detail_plan)
                    data1.update(eve_poc_id=service,eve_id=eventID,index_of_Session=(i+1))                
        # return Response({"Service Created Event Code"})
        if request.data['purp_call_id']==1: 
            event=agg_hhc_events.objects.get(eve_id=eventID)
            events=agg_hhc_event_response_serializer(event)
            return Response({"Service Created Event Code":[{"event_id":eventID},events.data,{"event_plan_of_care_id":event_plane_of_care}]})
        else:
            return Response({"Service Created Event Code":eventID})




# =================================================================================================================

class agg_hhc_add_service_form_api(APIView):
    def post(self,request):  
        patientID=None  
        caller = agg_hhc_callers.objects.filter(phone=request.data['phone']).first()
        if caller:
            callerSerializer= add_caller_by_form_serializer(caller,data= request.data)
            if callerSerializer.is_valid():
                callerID=callerSerializer.save()
                callerID=callerID.caller_id
            else:
                return Response(callerSerializer.errors)
        else:  
            callers= add_caller_by_form_serializer(data= request.data)
            if callers.is_valid():
                callerID=callers.save().caller_id
            else:
                return Response([callers.errors])
            patient= agg_hhc_patient_list_enquiry.objects.filter(phone_no=request.data['phone_no']).first()
            request.data['caller_id']=callerID
            if patient:
                patientSerializer = add_enquiry_patient_by_form_serializer(patient,data=request.data)
                if patientSerializer.is_valid():
                    patientID=patientSerializer.save().pt_id
                else:
                    return Response(patientSerializer.errors)
            else:
                request.data['caller_id']=callerID
                patient = add_enquiry_patient_by_form_serializer(data=request.data)
                if patient.is_valid():
                    patientID=patient.save()
                    patientID=patientID.pt_id
                else:
                    return Response([patient.errors])
        request.data['event_status']=1
        event= agg_hhc_event_serializer(data=request.data)
        if event.is_valid():
            eventID=event.save().eve_id
            request.data.pop('event_status')
        else:
            return Response([event.errors])
        event= agg_hhc_events.objects.filter(eve_id=eventID) 
        event.update(pt_id=patientID,caller_id=callerID,patient_service_status=2)
        # start_date = datetime.strptime(str(request.data['start_date']), '%Y-%m-%d %H:%M:%S')
        # end_date = datetime.strptime(str(request.data['end_date']), '%Y-%m-%d %H:%M:%S')
        # diff = ((end_date.date() - start_date.date()).days)
        # a=[request.data['sub_srv_id']]
        add_service= create_plane_of_care_serializer(data=request.data)
        if add_service.is_valid():
            service=add_service.save().eve_poc_id
        else:
            return Response([add_service.errors])
        plan_O_C= agg_hhc_event_plan_of_care.objects.filter(eve_poc_id=service)
        plan_O_C.update(eve_id=eventID)
        return Response({"Service Created Event Code":eventID})
# =================================================================================================================

    
class agg_hhc_state_api(APIView):
    def get(self,request,format=None):
        reason= agg_hhc_state.objects.all()
        serializer= agg_hhc_get_state_serializer(reason,many=True)
        return Response(serializer.data)
    
class agg_hhc_city_api(APIView):
    def get(self,request,pk,format=None):
        reason= agg_hhc_city.objects.filter(state_id=pk)
        serializer= agg_hhc_get_city_serializer(reason,many=True)
        return Response(serializer.data)

class agg_hhc_consultant_api(APIView):
    def get(self,request):
        consultant= agg_hhc_doctors_consultants.objects.filter(status=1)
        consultantSerializer= agg_hhc_doctors_consultants_serializer(consultant,many=True)
        return Response(consultantSerializer.data)
# ----------------------------------------------------------------------------------------------------

        

class agg_hhc_service_professional_details(APIView):
    def get(self,request):
        records= agg_hhc_service_professional_details.all()
        serializer= agg_hhc_service_professional_details_serializer(records,many=True)
        return Response(serializer.data)
    
#--------------------------get all patients from caller id -----------------------------

class agg_hhc_callers_phone_no(APIView):
    def get_object(self,pk):
        try:
            queryset =  agg_hhc_callers.objects.get(phone=pk)#.values_list('caller_id',flat=True)
            query_id=queryset.caller_id
            #print('this is query:',list(queryset))
            return query_id #8888888888
        except agg_hhc_callers.DoesNotExist:
            return None
    def get(self,request,pk,format=None):
        snippet=self.get_object(pk)
        caller_record= agg_hhc_callers.objects.get(pk=snippet)
        record= agg_hhc_patients.objects.filter(caller_id=snippet)
        print(record)
        serialized_caller= agg_hhc_callers_details_serializer(caller_record)
        serialized= agg_hhc_app_patient_by_caller_phone_no(record,many=True)
        return Response({"caller": serialized_caller.data, "patients": serialized.data})

#----------patients from callers_enum status---------------------
class agg_hhc_callers_phone_no_status_mobile_api(APIView):#staus=1
    def get(self,request):
        record= agg_hhc_callers.objects.filter(caller_status=1)
        print(record)
        serialized= agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

class agg_hhc_callers_phone_no_status_web_api(APIView):#staus=2
    def get(self,request):
        record= agg_hhc_callers.objects.filter(caller_status=2)
        print(record)
        serialized= agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

class agg_hhc_callers_phone_no_status_walking_api(APIView):#staus=3
    def get(self,request):
        record= agg_hhc_callers.objects.filter(caller_status=3)
        print(record)
        serialized= agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

class agg_hhc_callers_phone_no_status_calling_api(APIView):#staus=4
    def get(self,request):
        record= agg_hhc_callers.objects.filter(caller_status=4)
        print(record)
        serialized= agg_hhc_patients_serializer(record,many=True)
        return Response(serialized.data)

#---------------------------get all hospital names-----------------------------------

class agg_hhc_hospitals_api(APIView):
    def get(self,request):
        hospital= agg_hhc_hospitals.objects.filter(status=1)
        hospital_names=agg_hhc_hospitals_serializer(hospital,many=True)
        return Response(hospital_names.data)

#-------------------------get address by pincode-------------------------------------
class agg_hhc_pincode_api(APIView):
    def get(self,request):
        pincode= agg_hhc_pincode.objects.all()
        serialized= agg_hhc_pincode_serializer(pincode,many=True)
        return Response(serialized.data)

class agg_hhc_pincode_number_api(APIView):
    def get_object(self,pin):
        try:
            return  agg_hhc_pincode.objects.get(pincode_number=pin)
        except  agg_hhc_pincode.DoesNotExist:
            raise Response(status.HTTP_404_NOT_FOUND)
    def get(self,request,pin):
        obj=self.get_object(pin)
        serialized= agg_hhc_pincode_serializer(obj)
        return Response(serialized.data)

class agg_hhc_city_from_state_api(APIView):
    def get_object(self,state,formate=None):
        try:
            return  agg_hhc_city.objects.filter(state_id=state)
        except  agg_hhc_city.DoesNotExist:
            raise Response(status.HTTP_404_NOT_FOUND)
        
    def get(self,request,state):
        state_obj=self.get_object(state)
        serialized= agg_hhc_city(state_obj,many=True)
        return Response(serialized.data)

class agg_hhc_pincode_from_city_api(APIView):
    def get_object(self,city,formate=None):
        try:
            a= agg_hhc_pincode.objects.filter(city_name=city)
            return  agg_hhc_pincode.objects.filter(city_name=city)
        except  agg_hhc_pincode.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,city):
        pincode_obj=self.get_object(city)
        serialized= agg_hhc_pincode_serializer(pincode_obj,many=True)
        return Response(serialized.data)
class Caller_details_api(APIView):
    def get_object(self,pk):
        return  agg_hhc_callers.objects.get(caller_id=pk)
            
    def get_relation(self,pk):
        return  agg_hhc_caller_relation.objects.get(caller_rel_id=pk)
             
    def get(self,request,pk):  
        caller = self.get_object(pk)
        if caller:
            serializer =  Caller_details_serializer(caller)
            relation=(self.get_relation(serializer.data['caller_rel_id']))
            relations= relation_serializer(relation)
            return Response({"caller":serializer.data,"relation":relations.data})
        else:
            return Response({"error": 'user not found'})
        
    def put(self,request,pk):
        caller = self.get_object(pk)
        callerSerializer =  Caller_details_serializer(caller,data = request.data)
        if callerSerializer.is_valid():
            callerSerializer.validated_data['last_modified_date']=timezone.now()
            callerSerializer.save()
            return Response(callerSerializer.data)
        return Response(callerSerializer.errors)
    
class patient_detail_info_api(APIView):
    def get_patient(self,pk):
        return  agg_hhc_patients.objects.get(agg_sp_pt_id=pk)
    
    def get_hospital(self, pk):
        return  agg_hhc_hospitals.objects.get(hosp_id=pk)
    
    def get(self, request, pk):
        patient = self.get_patient(pk)
        if patient:
            serializer =  patient_detail_serializer(patient)
            hospital = self.get_hospital(serializer.data['preferred_hosp_id'])
            if hospital:
                hospitals =  hospital_serializer(hospital)
                return Response({"patient": serializer.data, "hospital": hospitals.data})

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        patient = self.get_patient(pk)
        serializer =  patient_detail_serializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['last_modified_date'] = timezone.now() #old_patient.hhc_code
        serializer.save()
        return Response(serializer.data)

# ----------------------------------------------professional availability details name and skills -----
class  agg_hhc_service_professionals_api(APIView):
    def get(self,request,formate=None):
        professional= agg_hhc_service_professionals.objects.filter(status=1)
        serialized= agg_hhc_service_professionals_serializer(professional,many=True)
        return Response(serialized.data)
    

class calculate_discount_api(APIView):
    def get(self, request,dtype,damount,total_amt):#dtype,amount,total_amt
        dtype=dtype
        amount=damount
        total_amt=total_amt
        if dtype == 1:
            final= (total_amt-(total_amt*amount)/100)
            return Response({"final_amount":final})
        elif dtype == 2:
            final = (total_amt-amount)
            return Response({"final_amount":final})
        else: return Response({"final_amount":total_amt})


class calculate_total_amount(APIView):
    def get(self,request,cost,start_date,end_date):
        # start_date_string = request.data['start_date']
        # end_date_string = request.data['end_date'] 
        start_date_string = start_date
        end_date_string = end_date
        start_date_string = start_date_string.replace('T',' ') 
        end_date_string = end_date.replace('T',' ')
        print(start_date_string)     
        try:
            start_date = datetime.strptime(str(start_date_string), '%Y-%m-%d %H:%M').date()
            end_date = datetime.strptime(str(end_date_string), '%Y-%m-%d %H:%M').date()            
            diff = (end_date - start_date).days 
            total = (diff+1) * cost          
            return Response({'days_difference': total})
        except ValueError:
            return Response({'error': 'Invalid date format'}, status=400)
        
class Service_requirment_api(APIView):
    def get_service(self,pk):
        return  agg_hhc_event_plan_of_care.objects.get(eve_poc_id=pk)
    def get(self,request,pk):
        service = self.get_service(pk)
        if service:
            services =  agg_hhc_add_service_serializer(service)
            return Response({"services":services.data})
        else:
            return Response({"error":"user service not found"})
        
    def put(self, request, pk):
        service = self.get_service(pk)
        serializer =  agg_hhc_add_service_serializer(service, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#------------------------------agg_hhc_professional_scheduled---used to display professional booked services --this will be used to display professiona record in calander

class agg_hhc_professional_scheduled_api(APIView):
    def get_object(self,prof_sche_id,formate=None):
        try:
            return  agg_hhc_professional_scheduled.objects.filter(srv_prof_id=prof_sche_id,status=1)
        except  agg_hhc_professional_scheduled.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,prof_sche_id):
        timeobject=self.get_object(prof_sche_id)
        serialized= agg_hhc_professional_scheduled_serializer(timeobject,many=True)
        return Response(serialized.data)

#--------------------------agg_hhc_professional_scheduled_api---used to display professional booked services in professional Avalibility

class agg_hhc_professional_time_availability_api(APIView):
    def get_object(self,prof_sche_id,formate=None):
        try:
            return  agg_hhc_professional_scheduled.objects.filter(srv_prof_id=prof_sche_id,status=1,scheduled_date=timezone.now())
        except  agg_hhc_professional_scheduled.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,prof_sche_id):
        dateobject=self.get_object(prof_sche_id)
        serialized= agg_hhc_professional_scheduled_serializer(dateobject,many=True)
        return Response(serialized.data)
    
#-------------------------agg_hhc_service_professional_zone_api-------------------

class agg_hhc_professional_zone_api(APIView):
    def get(self,request):
        zones = agg_hhc_professional_zone.objects.all()
        serialized=  agg_hhc_professional_zone_serializer(zones, many=True)
        return Response(serialized.data)
    
#-------------------------agg_hhc_feedback_answers----------------------------

class agg_hhc_feedback_answers_api(APIView):
    def get_obj(self,agg_sp_pt_id):
        try:
            obj= agg_hhc_events.objects.get(agg_sp_pt_id=agg_sp_pt_id)
            return  agg_hhc_feedback_answers.objects.get(eve_id=obj.eve_id)
        except  agg_hhc_feedback_answers.DoesNotExist:
            raise Response(status.HTTP_404_NOT_FOUND)
    def get(self,request,agg_sp_pt_id):
        feedback_answer=self.get_obj(agg_sp_pt_id)
        serialized= agg_hhc_feedback_answers_serializer(feedback_answer)
        return Response(serialized.data)



#------------------------agg_hhc_state_and_city from zone id----------------------

class agg_hhc_city_state_from_zone_api(APIView):
    def get_object(self,city_id):
        return  agg_hhc_city.objects.filter(status=1,city_id=city_id)
    def get(self,request,city_id):
        city_state=self.get_object(city_id)
        serialized= agg_hhc_city(city_state,many=True)
        return Response(serialized.data)
    

#-----------------------------------agg_hhc_event_plan_of_care--------------------------------

class service_details_today_total_services(APIView):
    def get(self,request):
       total_services =  agg_hhc_event_plan_of_care.objects.filter(added_date=timezone.now().date()).count()
       return Response({'total_services': total_services})


#----------------------------------last patient service name and start date end date--------------------------

class last_patient_service_info(APIView):
    def get_object(self,pt_id):
        return  agg_hhc_events.objects.filter(agg_sp_pt_id=pt_id)#.latest('added_date')
    def get(self, request,pt_id):
        try:
            patient_objects = self.get_object(pt_id)
        except  agg_hhc_events.DoesNotExist:
             return Response({"error": "Patient not found"},status=404)
        latest_patient_object = patient_objects.first()  # Get the latest object from the queryset
        eve_id = latest_patient_object.eve_id
        patient_date= agg_hhc_event_plan_of_care.objects.filter(eve_id=eve_id)
        patient_date=patient_date.first()
        patient_date_serialized= agg_hhc_event_plan_of_care_serializer(patient_date)
        print('this is patient _sat',patient_date)
        print('this is patient',str(patient_date.srv_id))
        patient_service_serialized= agg_hhc_services.objects.filter(srv_id=str(patient_date.srv_id)).first()
        print(';;;;;;',patient_service_serialized.service_title)

        # print('this is latest patient service',latest_patient_service)
        # print('this is service ',latest_patient_service.srv_id)
        # patient_obj= agg_hhc_services.objects.get(srv_id=latest_patient_service)
        # patient_obj_serialized= agg_hhc_services_serializer(patient_obj)
        return Response({'Date':patient_date_serialized.data,'service':patient_service_serialized.service_title})
        


#------------------------------mayank---------------------------------------

@api_view(['GET'])
def total_services(request, service_professional_id):  # Adjust the parameter name here
    try:
        total_services =  agg_hhc_event_plan_of_care.objects.filter(srv_prof_id=service_professional_id).count()  # Adjust the field name here
        return Response({"total_services": total_services}, status=status.HTTP_200_OK)
    except agg_hhc_event_plan_of_care.DoesNotExist:
        return Response({"error": "Service Professional not found."}, status=status.HTTP_404_NOT_FOUND)
    
class AggHHCServiceProfessionalListAPIView(generics.ListAPIView):
    queryset = agg_hhc_service_professionals.objects.all()
    serializer_class = AggHHCServiceProfessionalSerializer



#--------------------------------------Nikita P-----------------------------------------------
class agg_hhc_zone_api(APIView): # List of Zones

    def get(self, request, pk, format=None):
        print(pk)
        groups =  agg_hhc_professional_zone.objects.filter(city_id=pk)
        print(groups)
        if groups:
            serializer = agg_hhc_professional_zone_serializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class agg_hhc_sub_srv(APIView): # List of Sub-Services

    def get(self, request, format=None):
        sub_srvs =  agg_hhc_sub_services.objects.all()
        if sub_srvs:
            serializer = agg_hhc_sub_services_serializer(sub_srvs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class agg_hhc_service_professional_api(APIView): # List of professionals
    def get(self, request, format=None):
        zone = request.GET.get('zone')
        title = request.GET.get('title')
        pro = request.GET.get('pro')
        sub_srv = request.GET.get('srv')
        # zone = agg_hhc_service_professionals.objects.filter(prof_zone_id=zone)
        # if zone == None or title == None or pro == None:
        if zone or title:
            zone = agg_hhc_service_professionals.objects.filter(Q(prof_zone_id=zone) | Q(title=title) | Q(srv_id=sub_srv))
        elif pro:
            zone = agg_hhc_service_professionals.objects.filter(srv_prof_id=pro)
        else:
            zone = agg_hhc_service_professionals.objects.all()
        if zone:
            serializer = agg_hhc_service_professional_serializer(zone, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class agg_hhc_detailed_event_plan_of_care_api(APIView):
    def get(self, request, format=None):
        pro = request.GET.get('pro')
        pro =  agg_hhc_detailed_event_plan_of_care.objects.filter(srv_prof_id=pro)# To display all past & upcoming events.

        if pro:
            serializer = agg_hhc_detailed_event_plan_of_care_serializer(pro, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class agg_hhc_detailed_event_plan_of_care_per_day_api(APIView):
    def get(self, request, format=None):
        pro = request.GET.get('pro')
        # time = datetime.date.today()
        current_datetime = timezone.now()
        time = current_datetime.strftime("%Y-%m-%d")
        # time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Filter:- {time}")
        pro =  agg_hhc_detailed_event_plan_of_care.objects.filter(srv_prof_id=pro, service_status=2, actual_StartDate_Time__icontains=time)
        if pro:
            serializer = agg_hhc_detailed_event_plan_of_care_serializer(pro, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, format=None):
        json_data = json.loads(request.body)
        evt = json_data['agg_sp_dt_eve_poc_id']
        if evt is not None:
            # print(f"evt: {evt}")
            evt =  agg_hhc_detailed_event_plan_of_care.objects.get(agg_sp_dt_eve_poc_id=evt)
            serializer = agg_hhc_detailed_event_plan_of_care_serializer(evt, data=json_data)
            # print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CashfreeCreateOrder(APIView):

    def post(self, request, format=None):
        # serializer = PatientSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     patient = serializer.save()
        if request.data:
            print(request.data)
            return Response({'msg':'Payment Successfully added'},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    # def post(self, request):
    #     url = f"{settings.CASHFREE_API_URL}/payout/v1/order/create"
    #     # url = f"https://api.cashfree.com/payout/v1/order/create"
    #     payload = {
    #     "orderId": "0001",
    #     "orderAmount": "1",
    #     "orderCurrency": "INR",
    #     "orderNote": "Your order description or note",
    #     "customerName": "Nikita Pawar",
    #     "customerPhone": "7057662056",
    #     "customerEmail": "john.doe@example.com",
    #     "returnUrl": "https://example.com/payment-success",  # URL to redirect after successful payment
    #     "notifyUrl": "https://example.com/payment-notify",  # URL to receive payment notifications (webhooks)
    #     "source": "web",  # The source of the payment (web, mobile, etc.)
    #     "paymentModes": "card,upi,netbanking",  # Supported payment modes for the order
    #     # Add other required parameters specific to your use case here
    # }
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {settings.CASHFREE_SECRET_KEY}",
    #     }

    #     response = requests.post(url, json=payload, headers=headers)

    #     if response.status_code == status.HTTP_200_OK:
    #         # Successful response from Cashfree API
    #         data = response.json()
    #         # Process the data and return a success response to the client
    #         return Response(data, status=status.HTTP_200_OK)
    #     else:
    #         # Handle error response from Cashfree API
    #         error_data = response.json()
    #         # Handle the error data and return an error response to the client
    #         return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------#######-----------------------------------------------








#---------------------------Mohin-----------------------


class combined_info(APIView):
    def get(self,request):
        if request.method == 'GET':
            event_data= agg_hhc_events.objects.filter(Q(event_status=1) | Q(event_status=4))
            agg_hhc_eve= agg_hhc_events_serializers1(event_data,many=True)
            event=[]
            for i in agg_hhc_eve.data:
                event_code=i['event_code']#i['eve_id']
                patient_no=i['agg_sp_pt_id']
                patient= agg_hhc_patients.objects.get(agg_sp_pt_id=patient_no)
                pat_ser= agg_hhc_patients_serializer(patient)
                patient_name=pat_ser.data.get('name')
                patient_number=pat_ser.data.get('phone_no')
                patient_zone_id=pat_ser.data.get('prof_zone_id')
                patient_zone=agg_hhc_professional_zone.objects.get(prof_zone_id=patient_zone_id)
                caller_id=pat_ser.data.get('caller_id')
                caller_status= agg_hhc_callers.objects.get(caller_id=caller_id)
                caller_seri= agg_hhc_callers_seralizer(caller_status)
                caler_status=i['patient_service_status']
                event_plan_of_care =  agg_hhc_event_plan_of_care.objects.filter(eve_id=i['eve_id']).latest('eve_id')
                event_plan_of_care_serialzer= agg_hhc_create_service_serializer(event_plan_of_care)
                event_start_date=event_plan_of_care_serialzer.data.get('start_date')
                event_end_date=event_plan_of_care_serialzer.data.get('end_date')
                professional_prefered=event_plan_of_care_serialzer.data.get('prof_prefered')
                service_id=event_plan_of_care_serialzer.data.get('srv_id')
                service= agg_hhc_services.objects.get(srv_id=service_id)
                service_serializer= agg_hhc_services_serializer(service)
                service_name=service_serializer.data.get('service_title')
                even={'event_id':i['eve_id'],'event_code':event_code,'patient_name':patient_name,'patient_number':patient_number,'patient_zone':patient_zone.Name,'event_start_date':event_start_date,'event_end_date':event_end_date,'service_name':service_name,'caller_status':caler_status,'professional_prefered':professional_prefered}
                event.append(even)
            return Response({'event_code':event,})#'patient_name':patient.name,'patient_number':patient.phone_no,'service_name':service_name.service_title})#add zone from agg_hhc_patient_table







#####--------------------------------------logout------------------------------------------#
class LogoutView(APIView):
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'msg':'Token is blacklisted successfully.'},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'msg':'Bad Request'},status=status.HTTP_400_BAD_REQUEST)


#--------------------------------mayank--------------------------------------------

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import agg_hhc_service_professionals, agg_hhc_event_plan_of_care
# from .serializers import AggHHCServiceProfessionalSerializer

@api_view(['GET'])
def total_services(request):
    try:
        service_professionals = agg_hhc_service_professionals.objects.all()
        data = []
        for professional in service_professionals:
            total_services_count = agg_hhc_event_plan_of_care.objects.filter(srv_prof_id=professional.srv_prof_id).count()
            serializer = AggHHCServiceProfessionalSerializer(professional)
            professional_data = serializer.data
            professional_data['total_services'] = total_services_count
            data.append(professional_data)
        return Response(data, status=status.HTTP_200_OK)
    except agg_hhc_service_professionals.DoesNotExist:
        return Response({"error": "Service Professionals not found."}, status=status.HTTP_404_NOT_FOUND)
    




#---------------- ongoing service ------------------------



# from . models import agg_hhc_event_professional,agg_hhc_events,agg_hhc_payments
# from . serializers import OngoingServiceSerializer


class OngoingServiceView(APIView):
    serializer_class = OngoingServiceSerializer

    def get(self, request, format=None):
        data =  agg_hhc_events.objects.all()
        serializer = self.serializer_class(data, many=True)  
        filtered_data = [item for item in serializer.data if item is not None]
        return Response(filtered_data)
    
# -------------------------------------Amit Rasale---------------------------------------------------------------
class agg_hhc_enquiry_previous_follow_up_APIView(APIView):
    def get(self, request, event_id=None):
        queryset =  agg_hhc_enquiry_follow_up.objects.all()
        if event_id is not None:
            queryset = queryset.filter(event_id=event_id)
        serializer =  agg_hhc_enquiry_previous_follow_up_serializer(queryset, many=True)
        return Response(serializer.data)
    
class agg_hhc_enquiry_Add_follow_up_APIView(APIView):
    def post(self, request):
        serializer =  agg_hhc_enquiry_Add_follow_up_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class agg_hhc_enquiry_Add_follow_up_Cancel_by_Spero_APIView(APIView):
     def get(self,request,pk,format=None):
        reason= agg_hhc_enquiry_follow_up_cancellation_reason.objects.filter(cancel_by_id=pk)
        serializer= agg_hhc_enquiry_follow_up_cancellation_reason_spero_serializer(reason,many=True)
        return Response(serializer.data)
    
class agg_hhc_enquiry_followUp_cancellation_api(APIView):
    def get(self,request,pk,format=None):
        reason= agg_hhc_enquiry_follow_up_cancellation_reason.objects.filter(cancel_by_id=pk)
        serializer= agg_hhc_enquiry_follow_up_cancellation_reason_spero_serializer(reason,many=True)
        return Response(serializer.data)
   
class agg_hhc_enquiry_Add_follow_up_Cancel_by_APIView(APIView):   
    def post(self, request):
        serializer =  agg_hhc_enquiry_Add_follow_up_Cancel_by_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class agg_hhc_enquiry_Add_follow_up_create_service_APIView(APIView):
    def post(self, request):
        serializer =  agg_hhc_enquiry_Add_follow_up_create_service_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class agg_hhc_service_enquiry_list_combined_table_view(APIView):
    def get(self, request, eve_id=None, *args, **kwargs):
        queryset =  agg_hhc_events.objects.filter(purp_call_id=2)
        if eve_id is not None:
            queryset = queryset.filter(eve_id=eve_id)
        serializer =  agg_hhc_service_enquiry_list_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
#------------------------------------coupon--code----------------------------------------------------------
 
class coupon_code_post_api(APIView):
    def get_object(self,code,format=None):
        try:
            return  agg_hhc_coupon_codes.objects.filter(coupon_code=code,coupon_code_status=1).first()
        except  agg_hhc_coupon_codes.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,code,total_amt,format=None):
        queryset=self.get_object(code)
        if(queryset==None):
            return Response({'total_amt':total_amt})
        else:
            serialized= agg_hhc_coupon_code_serializers(queryset)
            percentage=serialized.data.get('coupon_code_discount_Percentage')
            amount=percentage
            total_amt=total_amt
            final= (total_amt-(total_amt*amount)/100)
            return Response({"final_amount":final})
        #return Response(serialized.data.get('coupon_code_discount_Percentage'))

class coupon_code_api(APIView):
    def get(self,request):
        codes= agg_hhc_coupon_codes.objects.filter(coupon_code_status=1,coupon_code_discount_Percentage__lte=10)
        serializered= agg_hhc_coupon_code_serializers(codes,many=True)
        return Response(serializered.data)





# ------------------ service reschedule  -------------

# from . serializers import Detailed_EPOC_serializer
from datetime import datetime, timedelta

class service_reschedule_view(APIView):
    def get(self, request, eve_id, format=None):
        queryset =  agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=eve_id)
        serializer = Detailed_EPOC_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  

    def patch(self, request, eve_id, format=None):
        start_date = datetime.strptime(request.data.get('start_date'), '%Y-%m-%dT%H:%M')
        end_date = datetime.strptime(request.data.get('end_date'), '%Y-%m-%dT%H:%M')

        # start_date_str = request.data.get('start_date')
        # end_date_str = request.data.get('end_date')

        # start_date = datetime.strptime(start_date_str, '%Y-%m-%d')  
        # end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # start_date = datetime.strptime(request.data.get('start_date'), '%Y-%m-%d').date()
        # end_date = datetime.strptime(request.data.get('end_date'), '%Y-%m-%d').date()
        remark = request.data.get('remark')

        try:
            queryset =  agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=eve_id)
            queryset2 =  agg_hhc_event_plan_of_care.objects.filter(eve_id=eve_id)
            queryset2.update(start_date=start_date, end_date=end_date, remark=remark)

            for i, obj in enumerate(queryset):
                new_start_date = start_date + timedelta(days=i)
                new_end_date = end_date + timedelta(days=i)
                obj.start_date = new_start_date
                obj.end_date = new_start_date
                obj.save()

        

            serializer = Detailed_EPOC_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except  agg_hhc_event_plan_of_care.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




# ------------------ Professional Reschedule ------------------

# from . models import Session_status_enum
class Professional_Reschedule_Apiview(APIView):
    # serializer_class =  Prof_Reschedule_serializer

    # def get(self, request, eve_id,index_of_session):
        
    #     data =  agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=eve_id,Session_status=Session_status_enum.Pending)
    #     serializer = self.serializer_class(data, many=True)
    #     return Response(serializer.data)
    
    # def get(self, request, eve_id, index_of_session):
    def get(self, request,eve_id):
        try:
            # record =  agg_hhc_detailed_event_plan_of_care.objects.get(eve_id=eve_id, index_of_Session=index_of_session,Session_status=Session_status_enum.Pending)
            record =  agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=eve_id,Session_status=Session_status_enum.Pending)
            serializer = self. Prof_Reschedule_serializer(record, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except  agg_hhc_detailed_event_plan_of_care.DoesNotExist:
            return Response({'error': 'No record found for the given eve_id and index_of_session'}, status=status.HTTP_404_NOT_FOUND)


    def patch(self, request, eve_id):
        try:
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            srv_prof_id = request.data.get('srv_prof_id')

            # If start_date and end_date are the same, update the specific record
            if start_date == end_date:
                record =  agg_hhc_detailed_event_plan_of_care.objects.get(
                    eve_id=eve_id, start_date=start_date, end_date=end_date
                )
                serializer = self.serializer_class(record, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
            else:
                
                service_professional =  agg_hhc_service_professionals.objects.get(pk=srv_prof_id)
                
                
                records_to_update =  agg_hhc_detailed_event_plan_of_care.objects.filter(
                    eve_id=eve_id, start_date__gte=start_date, end_date__lte=end_date
                )
                for record in records_to_update:
                    record.srv_prof_id = service_professional
                    record.save()

            return Response({'message': 'Records updated successfully'}, status=status.HTTP_200_OK)
        except  agg_hhc_detailed_event_plan_of_care.DoesNotExist:
            return Response({'error': 'No matching session found or session is less than date'}, status=status.HTTP_404_NOT_FOUND)


# -------------- Professional Allocation ----------

# class get_all_avail_professionals(APIView):
#     serializer_class =  avail_prof_serializer
#     def get(self,request,srv_id):

#         data =  agg_hhc_professional_sub_services.objects.filter(srv_id=srv_id)
#         serializer =  self.serializer_class(data,many=True)
#         return Response(serializer.data) 



#--------------------------------------cancellation service------------------

class ServiceCancellationView(APIView):
    serializer_class = ServiceCancellationSerializer

   

    serilizer_class2 = Event_Staus
    ev_serializer_class = Event_Plan_of_Care_Staus
    def get(self, request, eve_id):
        data = agg_hhc_events.objects.get(eve_id=eve_id)
        event_serializer = self.serilizer_class2(data)

        event_plan_data = agg_hhc_event_plan_of_care.objects.get(eve_id=eve_id)
        event_plan_serializer = self.ev_serializer_class(event_plan_data)

        response_data = {
            "event_data": event_serializer.data,
            "Service_date": event_plan_serializer.data
        }

        return Response(response_data)



    def post(self, request, eve_id):
        data1 = agg_hhc_events.objects.get(eve_id=eve_id)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
# ------------------------------------- Professional Availibilty for cancellation according to srv id -------------------
class get_all_avail_professionals(APIView):
    serializer_class = avail_prof_serializer
    def get(self,request,srv_id):

        data = agg_hhc_professional_sub_services.objects.filter(srv_id=srv_id)
        serializer =  self.serializer_class(data,many=True)
        return Response(serializer.data)

# ----- ----------------------------------------------------------------------

# This is allocation api .     
class allocate_api(APIView):
    def post(self,request):
        professional_id=request.data.get('srv_prof_id')
        try:
            event_id=agg_hhc_events.objects.get(eve_id=request.data.get('eve_id'))
            event_serializer=agg_hhc_updateIDs_event_serializer(event_id)
            event_id_is=event_serializer.data.get('eve_id')
            caller_id_is=event_serializer.data.get('caller_id')
            patient_id_is=event_serializer.data.get('agg_sp_pt_id')
        except:
            return Response({'message':'event not found'},status=404)
        try:
            service_id=agg_hhc_services.objects.get(srv_id=request.data.get('srv_id'))
        except:
            return Response({'message': 'Service not found'}, status=404)
        try:
            professional_instance = agg_hhc_service_professionals.objects.get(srv_prof_id=professional_id)
        except agg_hhc_service_professionals.DoesNotExist:
            return Response({'message': 'Professional not found'}, status=404)
        event_plan_of_care=agg_hhc_event_plan_of_care.objects.filter(eve_id=event_id).first()
        event_plan_of_care_serializer=agg_hhc_event_plan_of_care_serializer(event_plan_of_care)
        event_plan_of_care_id_is=event_plan_of_care_serializer.data.get('eve_poc_id')
        print("event name",event_plan_of_care)
        event_plan_of_care.srv_prof_id=professional_instance #to update and save new field here
        event_plan_of_care.save()
        event_professional=agg_hhc_event_professional.objects.create(eve_id=event_id,srv_prof_id=professional_instance,eve_poc_id=event_plan_of_care,srv_id=service_id,status=1)
        event_professional.save()
        try:
            detailed_event_poc=agg_hhc_detailed_event_plan_of_care.objects.filter(eve_id=request.data.get('eve_id'))
            print("detailed event plan of care",detailed_event_poc)
        except:
            return Response({'message':"detailed_event_plan_of_care not found"},status=404)
        for i in detailed_event_poc:
            i.srv_prof_id=professional_instance
            i.status=1
            print(i)
            i.save()
        event_id.event_status=2
        event_id.status=1
        event_id.save()
        return Response({'eve_id':event_id_is,'caller_id_is':caller_id_is,'agg_sp_pt_id':patient_id_is,'eve_poc_id':event_plan_of_care_id_is,'message':'professional Allocated sucessfully'})



class Dashboard_enquiry_count_api(APIView):
    def get(self,request,id):
        id=id
        if(id==1):
            time=timezone.now()
            print("this is time",time)
            enquiry=agg_hhc_patient_list_enquiry.objects.filter(added_date=timezone.now())
            enquiry_count=len(enquiry)
            App=0
            Social=0
            Calls=0
            Walk_in=0 
            for i in enquiry:
                caller_id=agg_hhc_events.objects.get(pt_id=i.pt_id)
                if(caller_id.patient_service_status==1):
                    App=App+1
                elif(caller_id.patient_service_status==2):
                    Social=Social+1
                elif(caller_id.patient_service_status==3):
                    Walk_in=Walk_in+1
                elif(caller_id.patient_service_status==4):
                    Calls=Calls+1
            if(enquiry_count>0):
                if(App>0):
                    App_percentage=int(Walk_in)/int(enquiry_count)
                    App_percentage*=100
                else:
                    App_percentage=0
                if(Social>0):
                    Social_percantage=int(Social)/int(enquiry_count)
                    Social_percantage*=100
                else:
                    Social_percantage=0
                if(Calls>0):
                    Calls_precentage=int(Calls)/int(enquiry_count)
                    Calls_precentage*=100
                else:
                    Calls_precentage=0
                if(Walk_in>0):
                    Walk_in_percentage=int(Walk_in)/int(enquiry_count)
                    Walk_in_percentage*=100
                else:
                    Walk_in_percentage=0
            else:
                App_percentage=0
                Social_percantage=0
                Calls_precentage=0
                Walk_in_percentage=0
            return Response({'Total_enquirys':enquiry_count,'App':App,'Socail':Social,'Calls':Calls,'Walk_in':Walk_in,"App_percentage":App_percentage,"Social_percantage":Social_percantage,"Calls_precentage":Calls_precentage,"Walk_in_percentage":Walk_in_percentage})
        elif(id==2):
            week_days=timezone.now()-timedelta(days=7)
            enquiry=agg_hhc_patient_list_enquiry.objects.filter(added_date__gte=week_days)
            enquiry_count=len(enquiry)
            App=0
            Social=0
            Calls=0
            Walk_in=0 
            for i in enquiry:
                caller_id=agg_hhc_events.objects.get(pt_id=i.pt_id)
                if(caller_id.patient_service_status==1):
                    App=App+1
                elif(caller_id.patient_service_status==2):
                    Social=Social+1
                elif(caller_id.patient_service_status==3):
                    Walk_in=Walk_in+1
                elif(caller_id.patient_service_status==4):
                    Calls=Calls+1
            if(enquiry_count>0):
                if(App>0):
                    App_percentage=int(Walk_in)/int(enquiry_count)
                    App_percentage*=100
                else:
                    App_percentage=0
                if(Social>0):
                    Social_percantage=int(Social)/int(enquiry_count)
                    Social_percantage*=100
                else:
                    Social_percantage=0
                if(Calls>0):
                    Calls_precentage=int(Calls)/int(enquiry_count)
                    Calls_precentage*=100
                else:
                    Calls_precentage=0
                if(Walk_in>0):
                    Walk_in_percentage=int(Walk_in)/int(enquiry_count)
                    Walk_in_percentage*=100
                else:
                    Walk_in_percentage=0
            else:
                App_percentage=0
                Social_percantage=0
                Calls_precentage=0
                Walk_in_percentage=0
            return Response({'Total_enquirys':enquiry_count,'App':App,'Socail':Social,'Calls':Calls,'Walk_in':Walk_in,"App_percentage":App_percentage,"Social_percantage":Social_percantage,"Calls_precentage":Calls_precentage,"Walk_in_percentage":Walk_in_percentage})
        elif(id==3):
            month=timezone.now()
            month=month.replace(day=1)
            enquiry=agg_hhc_patient_list_enquiry.objects.filter(added_date__gte=month)
            enquiry_count=len(enquiry)
            App=0
            Social=0
            Calls=0
            Walk_in=0 
            for i in enquiry:
                caller_id=agg_hhc_events.objects.get(pt_id=i.pt_id)
                if(caller_id.patient_service_status==1):
                    App=App+1
                elif(caller_id.patient_service_status==2):
                    Social=Social+1
                elif(caller_id.patient_service_status==3):
                    Walk_in=Walk_in+1
                elif(caller_id.patient_service_status==4):
                    Calls=Calls+1
            if(enquiry_count>0):
                if(App>0):
                    App_percentage=int(Walk_in)/int(enquiry_count)
                    App_percentage*=100
                else:
                    App_percentage=0
                if(Social>0):
                    Social_percantage=int(Social)/int(enquiry_count)
                    Social_percantage*=100
                else:
                    Social_percantage=0
                if(Calls>0):
                    Calls_precentage=int(Calls)/int(enquiry_count)
                    Calls_precentage*=100
                else:
                    Calls_precentage=0
                if(Walk_in>0):
                    Walk_in_percentage=int(Walk_in)/int(enquiry_count)
                    Walk_in_percentage*=100
                else:
                    Walk_in_percentage=0
            else:
                App_percentage=0
                Social_percantage=0
                Calls_precentage=0
                Walk_in_percentage=0
            return Response({'Total_enquirys':enquiry_count,'App':App,'Socail':Social,'Calls':Calls,'Walk_in':Walk_in,"App_percentage":App_percentage,"Social_percantage":Social_percantage,"Calls_precentage":Calls_precentage,"Walk_in_percentage":Walk_in_percentage})
class Dashboard_enquiry_status_count_api(APIView):
    def get(self,request,id):
        id=id
        if(id==1):
            enquiry_follow_up=agg_hhc_enquiry_follow_up.objects.filter(added_date=timezone.now())
            in_follow_up=0
            converted_to_service=0
            for i in enquiry_follow_up:
                if(i.follow_up==1):
                    in_follow_up+=1
                elif(i.follow_up==3):
                    converted_to_service+=1
            total=in_follow_up+converted_to_service
            if(total>0):
                if(in_follow_up>0):
                    in_follow_up_percentage=in_follow_up/total
                    in_follow_up_percentage*=100
                else:
                    in_follow_up_percentage=0
                if(converted_to_service>0):
                    converted_to_service_percentage=converted_to_service/total
                    converted_to_service_percentage*=100
                else:
                    converted_to_service_percentage=0
            else:
                in_follow_up_percentage=0
                converted_to_service_percentage=0
            return Response({'in_follow_up':in_follow_up,'converted_to_service':converted_to_service,'in_follow_up_percentage':in_follow_up_percentage,'converted_to_service_percentage':converted_to_service_percentage})    
            
        elif(id==2):
            week=timezone.now()-timedelta(days=7)
            enquiry_follow_up=agg_hhc_enquiry_follow_up.objects.filter(added_date__gte=week)
            in_follow_up=0
            converted_to_service=0
            for i in enquiry_follow_up:
                if(i.follow_up==1):
                    in_follow_up+=1
                elif(i.follow_up==3):
                    converted_to_service+=1
            total=in_follow_up+converted_to_service
            if(total>0):
                if(in_follow_up>0):
                    in_follow_up_percentage=in_follow_up/total
                    in_follow_up_percentage*=100
                else:
                    in_follow_up_percentage=0
                if(converted_to_service>0):
                    converted_to_service_percentage=converted_to_service/total
                    converted_to_service_percentage*=100
                else:
                    converted_to_service_percentage=0
            else:
                in_follow_up_percentage=0
                converted_to_service_percentage=0
            return Response({'in_follow_up':in_follow_up,'converted_to_service':converted_to_service,'in_follow_up_percentage':in_follow_up_percentage,'converted_to_service_percentage':converted_to_service_percentage})    
            
        elif(id==3):
            month=timezone.now()
            month=month.replace(day=1)
            print(month)
            enquiry_follow_up=agg_hhc_enquiry_follow_up.objects.filter(added_date__gte=month)
            in_follow_up=0
            converted_to_service=0
            for i in enquiry_follow_up:
                if(i.follow_up==1):
                    in_follow_up+=1
                elif(i.follow_up==3):
                    converted_to_service+=1
            total=in_follow_up+converted_to_service
            if(total>0):
                if(in_follow_up>0):
                    in_follow_up_percentage=in_follow_up/total
                    in_follow_up_percentage*=100
                else:
                    in_follow_up_percentage=0
                if(converted_to_service>0):
                    converted_to_service_percentage=converted_to_service/total
                    converted_to_service_percentage*=100
                else:
                    converted_to_service_percentage=0
            else:
                in_follow_up_percentage=0
                converted_to_service_percentage=0
            return Response({'in_follow_up':in_follow_up,'converted_to_service':converted_to_service,'in_follow_up_percentage':in_follow_up_percentage,'converted_to_service_percentage':converted_to_service_percentage})    
            
