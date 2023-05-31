from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hhcapp import models
from hhcapp import serializer
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


class agg_hhc_app_caller_register_api(APIView):
    def post(self,request):
        register=serializers.agg_hhc_app_caller_register_Serializer(data=request.data)
        if register.is_valid():
            register.save()
            return Response(register.data,status=status.HTTP_201_CREATED)
        return Response(register.errors)
    def get(self,request):
        reg=models.agg_hhc_app_caller_register.objects.all()
        #ref=serializers.
        

# Create your views here.
