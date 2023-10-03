from django.urls import path
from . import views

urlpatterns=[

# --------------------------------- Nikita P / Vishal ------------------------------------------
    path('pro_login/',views.ProfessionalOTPLogin.as_view()),
    path('pro_otp_chk/',views.OTPCHECK.as_view(),name="OTPCHECK"),
    path('pro_logout/',views.LogoutView.as_view(),name="LogoutView"),
    path('pro_add_zone/',views.AddZoneView.as_view(),name="AddZoneView"),


# --------------------------------- Sandip Shimpi -----------------------------------------------
    path('agg_hhc_document_list/<int:pk>/',views.agg_hhc_document_list.as_view()),
    path('agg_hhc_add_document/',views.agg_hhc_add_document.as_view()),
    path('agg_hhc_add_document/<int:pk>/',views.agg_hhc_add_document.as_view()),
    path('Add_Prof_location_api/',views.Add_Prof_location_api.as_view()),

    


# --------------------------------  Vinayak / Mayank -------------------------------------------

    path('reg_prof_Apiview/<int:srv_prof_id>', views.Register_professioanl_for_interview.as_view()),
]