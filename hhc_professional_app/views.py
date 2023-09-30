from django.shortcuts import render
from hhcweb import models as webmodel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from hhc_professional_app.serializer import *
from hhcspero.settings import AUTH_KEY
import random
import requests,random,pytz,io
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh" : str(refresh),
        "access" : str(refresh.access_token),
        "colleague": {
                'id': user.id
            }
    }


# Create your views here.

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
            msg = f"Use {otp} as your verification code on Spero Application. The OTP expires within 10 mins, {otp} Team Spero"
            professional_found = webmodel.agg_com_colleague.objects.filter(clg_Work_phone_number=number).first()

            if number != None:

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
                        send_otp(number,msg)

                    # print("OTP for this is ", otp)
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
                        # print("Clg id: ",clg.id)

                    if professional_serializer.is_valid():
                        professional_serializer.validated_data['phone_no'] = number
                        professional_serializer.validated_data['OTP'] = otp
                        professional_serializer.validated_data['otp_expire_time'] = otp_expire_time
                        professional_serializer.validated_data['OTP_count'] = 1
            
                        pro = professional_serializer.save()
                        send_otp(number,msg)
                        # print("Prof id: ",pro.srv_prof_id)

                    return Response({"phone_no": number, "OTP": otp})
            else:
                return Response({'msg':'Phone number is not present. Please enter valid phone number.'},status=status.HTTP_400_BAD_REQUEST)
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
                token = get_tokens_for_user(user_available)
                return Response({'token':token, "message": "Login successfully"})
            else:
                return Response({"message": "Wrong OTP"})

        except Exception as e:
            # Handle any other exceptions here
            return Response({"message": "An error occurred: {}".format(str(e))})
        
class LogoutView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'msg':'Token is blacklisted successfully.'},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'msg':'Token is not correct. Please try again with correct token.'},status=status.HTTP_400_BAD_REQUEST)
        

class AddZoneView(APIView):

    def post(self, request, format=None):
        serializer = agg_hhc_professional_location_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            id = serializer.save()
            # id = str(id)
            # id = [id]
            print(id)
            return Response({'id':id,'msg':'Ems Incident Added Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




# ------------------------------- professional register API view -------------------------------

class Register_professioanl_for_interview(APIView):
    serializer_class = reg_prof_api_serializer

    def get_object(self, srv_prof_id):
        try:
            return agg_hhc_service_professionals.objects.get(srv_prof_id=srv_prof_id)
        except agg_hhc_service_professionals.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def post(self, request,srv_prof_id):
        # srv_prof_id = request.data.get('srv_prof_id')  # Assuming the ID is provided in the request data
        instance = self.get_object(srv_prof_id)
        serializer = self.serializer_class(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# ---------------------------- Professional document upload and check ---------------------------


class agg_hhc_document_list(APIView):
    def get(self,request,pk):
        call= webmodel.agg_hhc_documents_list.objects.filter(professional_role=pk)
        serializers=agg_hhc_document_list_serializer(call,many=True)
        doc_list_ID = [{'doc_list_ID': item['doc_li_id'],'Documents_name':item['Documents_name'],'professional_role':item['professional_role']} for item in serializers.data]

        response_data={
            'doc_list_ID':doc_list_ID
        }
        return Response(response_data)

class agg_hhc_add_document(APIView):    
    def post(self,request):
        serialized= agg_hhc_add_document_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'message':'sucessful'},status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk):
        data=webmodel.agg_hhc_professional_documents.objects.filter(professional_id=pk)
        serializers = agg_hhc_add_document_serializer(data,many=True)
        doc_list_ID = [{'prof_doc_id': item['prof_doc_id'],'professional_id':item['professional_id'],'doc_list_id':item['doc_li_id'],'professional_document':item['professional_document']} for item in serializers.data]

        response_data={
            'doc_list_ID':doc_list_ID
        }
            # data.append(data1)
        return Response(response_data)