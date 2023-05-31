# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from hhcapp import models
# from hhcapp import serializer
"""
# Create your views here.
class CourseListView(APIView):
    def post(self,request):
        courseSerializer = serializers.CourseSerializer(data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)
"""    


# class agg_hhc_app_caller_register_api(APIView):
#     def post(self,request):
#         register=serializers.agg_hhc_app_caller_register_Serializer(data=request.data)
#         if register.is_valid():
#             register.save()
#             return Response(register.data,status=status.HTTP_201_CREATED)
#         return Response(register.errors)
#     def get(self,request):
#         reg=models.agg_hhc_app_caller_register.objects.all()
#         #ref=serializers.
        

# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcapp.serializer import *
from datetime import datetime, timedelta
import requests
import random
from .models import *
import pytz
import io
from rest_framework.parsers import JSONParser
from rest_framework import request
from hhcspero.settings import AUTH_KEY


def send_otp(mobile,msg):
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
        print(da)
        msg = f"Use {otp} as your verification code on Spero Application. The OTP expires within 10 mins, {otp} Team Spero"
        print(da['phone'])
        print(otp)
        user_available=agg_hhc_app_caller_register.objects.filter(phone=da['phone']).first()
        if(user_available):#(old user data )
            compl=agg_hhc_app_caller_register()
            compl.phone=da['phone']
            compl.otp=otp
            compl.otp_expire_time=datetime.now()+timedelta(minutes=10)
            compl.app_call_reg_id=user_available.app_call_reg_id
            print(compl.otp)
            print(compl.otp_expire_time)
            print()
            compl.save()
            send_otp(da['phone'],msg)
            da['otp']=otp
            da['otp_expire_time']=datetime.now()+timedelta(minutes=10)
            se=webserializers(data=da)
            if se.is_valid():
                return Response(se.data)
        else:#(new user registration)
            agg_hhc_app_caller_register.objects.create(phone=da['phone'],otp=otp,otp_expire_time=datetime.now()+timedelta(minutes=2))
            se=webserializers(data=da)
            if(se.is_valid()):
                se.save()
                send_otp(da['phone'],msg)
                return Response(se.data)
    def get(self,request):
        user=agg_hhc_app_caller_register.objects.all()
        ser=webserializers(user,many=True)
        return Response(ser.data)
    
    
class OTPCHECK(APIView):
    def post(self,request):
        number=request.body
        ja=io.BytesIO(number)
        da=JSONParser().parse(ja)#we are converting our data in dictionary
        now_time=datetime.now()
        now_time=now_time.replace(tzinfo=pytz.utc)
        #print(da['mobile_number'])
        user_available=agg_hhc_app_caller_register.objects.filter(phone=da['phone']).first()
        print(user_available)
        print("user_available.otp",user_available.otp)
        if(user_available.otp==da['otp'] and user_available.otp_expire_time>now_time):
            return Response({"message":"login sucessfully"})
        else:
            return Response({"message":"wrong otp or OTP expired"})