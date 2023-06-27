from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcapp import serializer
from datetime import datetime, timedelta
import requests,random,pytz,io
from hhcweb import models as webmodels
from rest_framework.parsers import JSONParser
from hhcspero.settings import AUTH_KEY
from rest_framework import status
from hhcweb import models as webmodel


def send_otp(mobile,msg):
    pass
    url=(f"https://wa.chatmybot.in/gateway/waunofficial/v1/api/v1/sendmessage?access-token={AUTH_KEY}&phone={mobile}&content={msg}&fileName&caption&contentType=1")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        print("URL successfully hit!")
    except requests.exceptions.RequestException as e:
        print("Error occurred while hitting the URL:", e)

class OTPLOGIN(APIView):
    def post(self,request):
        number=request.body
        otp=str(random.randint(1000 , 9999))
        ja=io.BytesIO(number)
        da=JSONParser().parse(ja)#we are converting our data in dictionary
        msg = f"Use {otp} as your verification code on Spero Application. The OTP expires within 10 mins, {otp} Team Spero"
        user_available=webmodel.agg_hhc_callers.objects.filter(phone=da['phone']).first()
        if(user_available):#(old user data )
            compl=webmodel.agg_hhc_callers()
            compl.phone=da['phone']
            compl.otp=otp
            compl.otp_expire_time=datetime.now()+timedelta(minutes=10)
            compl.caller_id=user_available.caller_id
            compl.save()
            send_otp(da['phone'],msg)
            da['otp']=otp
            da['otp_expire_time']=datetime.now()+timedelta(minutes=10)
            se=serializer.webserializers(data=da)
            if se.is_valid():
                return Response(se.data)
        else:#(new user registration)
            webmodel.agg_hhc_callers.objects.create(phone=da['phone'],otp=otp,otp_expire_time=datetime.now()+timedelta(minutes=2))
            se=serializer.webserializers(data=da)
            if(se.is_valid()):
                send_otp(da['phone'],msg)
                return Response(se.data)
    def get(self,request):
        user=webmodel.agg_hhc_callers.objects.all()
        ser=serializer.webserializers(user,many=True)
        return Response(ser.data)
    
    
class OTPCHECK(APIView):
    def post(self,request):
        number=request.body
        ja=io.BytesIO(number)
        da=JSONParser().parse(ja)#we are converting our data in dictionary
        now_time=datetime.now()
        now_time=now_time.replace(tzinfo=pytz.utc)
        #print(da['mobile_number'])
        user_available=webmodel.agg_hhc_callers.objects.filter(phone=da['phone']).first()
        print(user_available)
        print("user_available.otp",user_available.otp)
        if(user_available.otp==da['otp'] and user_available.otp_expire_time>now_time):
            return Response({"message":"login sucessfully"})
        elif user_available.otp_expire_time>now_time:
            return Response({"message":"OTP expired"})
        else:
            return Response({"message":"wrong otp"})
#---------------------------------------------------------------

class agg_hhc_callers_api(APIView):
    def post(self,request):
        register=serializer.agg_hhc_callers_Serializer(data=request.data)
        if register.is_valid():
            register.save()
            return Response(register.data,status=status.HTTP_201_CREATED)
        return Response(register.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        reg=webmodel.agg_hhc_callers.objects.all()
        ref=serializer.agg_hhc_callers_Serializer(reg,many=True)
        return Response(ref.data)

class agg_hhc_app_services_api(APIView):
    def get(self,request):
        call=webmodels.agg_hhc_services.objects.filter(status=1)
        service=serializer.agg_hhc_app_services_serializer(call,many=True)
        return Response(service.data)

class add_family_member(APIView):
    def post(self,request):
        serilized = serializer.agg_hhc_app_family_details(data = request.data)
        if serilized.is_valid():
            serilized.save()
            return Response(serilized.data, status=status.HTTP_201_CREATED)
        return Response(serilized.errors,status=status.HTTP_400_BAD_REQUEST)
    
class add_multiple_address_api(APIView):
    def post(self,request):
        # print(request.data)
        serilized = serializer.add_multiple_address_serializer(data = request.data)
        # print(serilized)
        if serilized.is_valid():
            serilized.save()
            return Response(serilized.data, status=status.HTTP_201_CREATED)
        return Response(serilized.errors,status=status.HTTP_400_BAD_REQUEST)
################################################_______get patients record from caller id____###############    
class agg_hhc_app_patient_by_caller_api(APIView):
    def get_object(self,pk):
        try:
            #print("this is my id ",pk)
            #print("this is my data",webmodel.agg_hhc_patients.objects.filter(caller_id=pk))
            return webmodel.agg_hhc_patients.objects.filter(caller_id=pk,status=1)
        except webmodel.agg_hhc_patients.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, pk, format=None):
        #print("this is inside get",pk)
        snippet= self.get_object(pk)
        serialized =serializer.agg_hhc_app_patient_by_caller_id(snippet,many=True)
        return Response(serialized.data)
    

#####____________________get All Address from caller id_____________####
class agg_hhc_app_address_by_caller_api(APIView):
    def get_object(self,pk):
        try:
            return  
        except webmodel.agg_hhc_app_add_address.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk,format=None):
        address=self.get_object(pk)
        serialized=serializer.agg_hhc_app_address_by_caller_id(address,many=True) 
        return Response(serialized.data) 
    
###_____________________get All Address from caller id_____________####
class agg_hhc_app_address_by_caller_api(APIView):
    def get_object(self,pk):
        try:
            return webmodel.agg_hhc_app_add_address.objects.filter(app_call_reg_id=pk)
        except webmodel.agg_hhc_app_add_address.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk,format=None):
        address=self.get_object(pk)
        serialized=serializer.agg_hhc_app_address_by_caller_id(address,many=True) 
        return Response(serialized.data)

class agg_hhc_app_befered_by(APIView):
    
    def get(self,request):
        hospitals=webmodels.agg_hhc_hospitals.objects.filter(status=1)
        serializers=serializer.agg_hhc_app_refered_by_serializer(hospitals,many=True)
        return Response(serializers.data)
    
class agg_hhc_app_prefered_consultant(APIView):

    def get(self, request):
        consultants = webmodels.agg_hhc_doctors_consultants.objects.filter(status=1)
        serializers=serializer.agg_hhc_prefered_consultants_serializer(consultants, many=True)
        return Response(serializers.data)

# class agg_hhc_app_
###____________________________put_request_agg_hhc_callers_________###
class agg_hhc_callers_put_api(APIView):
    def get_object(self,pk):
        try:
            return webmodel.agg_hhc_callers.objects.get(caller_id=pk)
        except webmodel.agg_hhc_callers.DoesNotExist:
            return status.HTTP_400_BAD_REQUEST
    def put(self,request,pk,format=None):
        record=self.get_object(pk)
        serialized=serializer.agg_hhc_callers_Serializer(record,data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        record=self.get_object(pk)
        serialized=serializer.agg_hhc_callers_Serializer(record)
        return Response(serialized.data)

#__________________________________state api________________

class agg_hhc_state_api(APIView):
    def get(self,request):
        state=webmodels.agg_hhc_state.objects.all()
        serialized=serializer.agg_hhc_state_serializer(state,many=True)
        return Response(serialized.data)
    

class agg_hhc_app_address_get_put_delete_api(APIView):
    def get_object(self,pk):
        try:
            return webmodel.agg_hhc_app_add_address.objects.get(address_id=pk)
        except webmodel.agg_hhc_app_add_address.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk,format=None):
        address=self.get_object(pk)
        serialized=serializer.add_multiple_address_serializer(address) 
        return Response(serialized.data)
    def put(self,request,pk,format=None):
        record=self.get_object(pk)
        serialized=serializer.add_multiple_address_serializer(record,data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        record = self.get_object(pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class agg_hhc_sub_services_from_service(APIView):
    def get_object(self,pk):
        try:
            return webmodel.agg_hhc_sub_services.objects.filter(srv_id=pk)
        except webmodel.agg_hhc_sub_services.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk,format=None):
        record=self.get_object(pk)
        serialized=serializer.agg_hhc_sub_services_serializer(record,many=True)
        return Response(serialized.data)
        
class agg_hhc_patient_doc_detail(APIView):
    def post(self,request):
        # print(request.data)
        serilized = serializer.agg_hhc_patient_doc_details_serializer(data = request.data)
        # print(serilized)
        if serilized.is_valid():
            serilized.save()
            return Response(serilized.data, status=status.HTTP_201_CREATED)
        return Response(serilized.errors,status=status.HTTP_400_BAD_REQUEST)

