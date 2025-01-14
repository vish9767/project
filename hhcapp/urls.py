from django.urls import path
from hhcapp import views
from hhcweb import views as webviews
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns=[
    path('agg_hhc_callers_api',views.agg_hhc_callers_api.as_view(),name="agg_hhc_callers_api"),
    path('OTPLOGIN',views.OTPLOGIN.as_view(),name="OTPLOGIN"),
    path('OTPCHECK',views.OTPCHECK.as_view(),name="OTPCHECK"),
    path('agg_hhc_app_services_api',views.agg_hhc_app_services_api.as_view()),
    path('add_family_member',views.add_family_member.as_view()),
    path('add_multiple_address_api', views.add_multiple_address_api.as_view()),
    path('agg_hhc_callers_relation_api', webviews.agg_hhc_caller_relation_api.as_view()),
    path('agg_hhc_app_patient_by_caller_api/<int:pk>/', views.agg_hhc_app_patient_by_caller_api.as_view()),
    path('agg_hhc_app_address_by_caller_api/<int:pk>/',views.agg_hhc_app_address_by_caller_api.as_view()),
    path('agg_hhc_app_befered_by',views.agg_hhc_app_befered_by.as_view()),
    path('agg_hhc_app_prefered_consultant',views.agg_hhc_app_prefered_consultant.as_view()),
    path('agg_hhc_callers_api/<int:pk>/',views.agg_hhc_callers_put_api.as_view()),
    path('agg_hhc_state_api',views.agg_hhc_state_api.as_view()),
    path('agg_hhc_app_address_get_put_delete_api/<int:pk>/',views.agg_hhc_app_address_get_put_delete_api.as_view()),
    path('agg_hhc_sub_services_from_service/<int:pk>',views.agg_hhc_sub_services_from_service.as_view()), #this api will de used in web as well as app
    path('agg_hhc_patient_doc_detail', views.agg_hhc_patient_doc_detail.as_view()),
     #=============================================================================
    path('register/<int:pk>/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('otp/', views.otpview.as_view(), name='otp'),
    path('ResendOTP/', views.ResendOTP.as_view()),
    path('VerifyPhoneNo/', views.VerifyPhoneNo.as_view())
    #=============================================================================
        
]