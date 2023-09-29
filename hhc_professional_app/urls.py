from django.urls import path
from . import views


urlpatterns=[
<<<<<<< HEAD
    path('professional_OTPLOGIN',views.professional_OTPLOGIN.as_view()),
    # path('profile/',views.profiles.as_view()),
    # path('agg_hhc_services_api',views.agg_hhc_services_api.as_view()),
    path('agg_hhc_document_list/<int:pk>/',views.agg_hhc_document_list.as_view()),
    path('agg_hhc_add_document/',views.agg_hhc_add_document.as_view()),
=======
    path('pro_login',views.ProfessionalOTPLogin.as_view()),
    path('pro_otp_chk',views.OTPCHECK.as_view()),
<<<<<<< HEAD
>>>>>>> 427c65131da3fdc2ccdbecbca89763431f9d3363
=======
    path('pro_avb',views.add_professional_avb.as_view())
>>>>>>> e7adb361bd5ab0f02d35ff4c67c7b33ce95b82e2
]