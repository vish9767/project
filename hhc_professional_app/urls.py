from django.urls import path
from . import views

urlpatterns=[
    path('pro_login',views.ProfessionalOTPLogin.as_view()),
    path('pro_otp_chk',views.OTPCHECK.as_view()),
    path('pro_avb',views.add_professional_avb.as_view()),
    path('date_wise_location_details/<str:da>/',views.date_wise_location_details.as_view()),
]