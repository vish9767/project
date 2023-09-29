from django.shortcuts import render
from hhcweb import models as webmodel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from hhc_professional_app.serializer import *
from hhcspero.settings import AUTH_KEY
import random
from django.core.exceptions import ObjectDoesNotExist
import requests,random,pytz,io
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

<<<<<<< HEAD
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
=======
def send_otp(mobile,msg):
    url=(f"https://wa.chatmybot.in/gateway/waunofficial/v1/api/v1/sendmessage?access-token={AUTH_KEY}&phone={mobile}&content={msg}&fileName&caption&contentType=1")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    except requests.exceptions.RequestException as e:
        print("Error occurred while hitting the URL:", e)


class ProfessionalOTPLogin(APIView):
    def post(self, request):
        try:
            number = request.data.get('phone_no')
            otp = str(random.randint(1000, 9999))
            otp_expire_time = timezone.now() + timezone.timedelta(minutes=10)
            print('this is otp expire time',otp_expire_time)
            now_time=timezone.now()
            print('now time',now_time)
            now_time=now_time.replace(tzinfo=pytz.utc)
            time=datetime.now()
            professional_found = webmodel.agg_com_colleague.objects.filter(clg_Work_phone_number=number).first()
            if professional_found:
                professional_found.clg_otp = otp
                professional_found.clg_otp_count += 1
                professional_found.clg_otp_expire_time = otp_expire_time
                professional_found.save()
                service_professional = webmodel.agg_hhc_service_professionals.objects.filter(phone_no=number).first()
                if service_professional:
                    service_professional.OTP = otp
                    service_professional.OTP_count += 1
                    service_professional.otp_expire_time = otp_expire_time
                    service_professional.save()
                print("OTP for this is ", otp)
                return Response({'phone_no': number, 'OTP': otp})
            else:
                professional_colleague_serializer = UserRegistrationSerializer2(data=request.data)
                professional_serializer = agg_hhc_service_professionals_serializer(data=request.data)

                if professional_colleague_serializer.is_valid():
                    professional_colleague_serializer.validated_data['clg_Work_phone_number'] = number
                    professional_colleague_serializer.validated_data['clg_otp'] = otp
                    professional_colleague_serializer.validated_data['clg_otp_expire_time'] = otp_expire_time
                    professional_colleague_serializer.validated_data['clg_otp_count'] = 1
                    clg = professional_colleague_serializer.save()
                    print("Clg id: ",clg.id)

                if professional_serializer.is_valid():
                    professional_serializer.validated_data['phone_no'] = number
                    professional_serializer.validated_data['OTP'] = otp
                    professional_serializer.validated_data['otp_expire_time'] = otp_expire_time
                    professional_serializer.validated_data['OTP_count'] = 1
                    pro = professional_serializer.save()
                    print("Prof id: ",pro.srv_prof_id)
                return Response({"phone_no": number, "OTP": otp})
        except Exception as e:
            return Response({'error': str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class OTPCHECK(APIView):
    def post(self, request):
        try:
            number = request.data.get('phone_no')
            otp = request.data.get('otp')
            time = timezone.now()
            print("time", time)

            try:
                user_available = webmodel.agg_com_colleague.objects.get(clg_Work_phone_number=number)
            except ObjectDoesNotExist:
                return Response({"message": 'User not found with this number'})
            if user_available.clg_otp == otp and user_available.clg_otp_expire_time > time:
                return Response({"message": "Login successfully"})
            else:
                return Response({"message": "Wrong OTP"})

        except Exception as e:
<<<<<<< HEAD
            # Handle any other exceptions here
            return Response({"message": "An error occurred: {}".format(str(e))})
>>>>>>> 427c65131da3fdc2ccdbecbca89763431f9d3363
=======
            return Response({"message": "An error occurred: {}".format(str(e))})
        


#-------------------------vishal is working on it

class add_professional_avb(APIView):
    def post(self,request):
        print("data is not ")
        print("data inside ",request.data)
>>>>>>> e7adb361bd5ab0f02d35ff4c67c7b33ce95b82e2
