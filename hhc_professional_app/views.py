from django.shortcuts import render
from hhcweb import models as webmodel
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializer
import random
import requests,random,pytz,io
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class professional_OTPLOGIN(APIView):
    def post(self,request):
        number = request.data.get('phone_no')
        professional_found=webmodel.agg_hhc_service_professionals.objects.filter(phone_no=number).first()
        otp=str(random.randint(1000 , 9999))
        msg = f"Use {otp} as your verification code on Spero Application. The OTP expires within 10 mins, {otp} Team Spero"
        if professional_found :
            professional_found.OTP=otp
            professional_found.otp_expire_time=datetime.now()+timedelta(minutes=10)
            professional_found.save()
            print("otp for this is ",otp)
            return Response({'phone_no':number,'OTP':otp})  
        else:
            professional_serializer=serializer.agg_hhc_service_professionals_serializer(data=request.data)
            if professional_serializer.is_valid():
                print("this is otp ",otp)
                phone=professional_serializer.validated_data['phone_no']=number
                otp=professional_serializer.validated_data['OTP']=otp#.validated_data['OTP']=otp
                professional_serializer.validated_data['otp_expire_time']=datetime.now()+timedelta(minutes=10)#validated_data['otp_expire_time']=datetime.now()+timedelta(minutes=10)
                professional_serializer.validated_data['OTP_count']=1
                professional_serializer.save()
                return Response({"phone_no":phone,"OTP":otp})
            
class agg_hhc_document_list(APIView):
    def get(self,request,pk):
        call= webmodel.agg_hhc_documetns_list.objects.filter(professional_role=pk)
        serializers=serializer.agg_hhc_document_list_serializer(call,many=True)
        doc_list_ID = [{'doc_list_ID': item['doc_li_id'],'Documents_name':item['Documents_name'],'professional_role':item['professional_role']} for item in serializers.data]

        response_data={
            'doc_list_ID':doc_list_ID
        }
        return Response(response_data)

class agg_hhc_add_document(APIView):    
    def post(self,request):
        serialized= serializer.agg_hhc_add_document_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'message':'sucessful'},status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        data=webmodel.agg_hhc_professional_documents.objects.all()
        serializers = serializer.agg_hhc_add_document_serializer(data,many=True)
        doc_list_ID = [{'prof_doc_id': item['prof_doc_id'],'professional_id':item['professional_id'],'doc_list_id':item['doc_li_id'],'professional_document':item['professional_document']} for item in serializers.data]

        response_data={
            'doc_list_ID':doc_list_ID
        }
            # data.append(data1)
        return Response(response_data)