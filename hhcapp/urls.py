from django.urls import path
from hhcapp import views
from hhcweb import views as webviews

urlpatterns=[
    path('agg_hhc_app_caller_register_api',views.agg_hhc_app_caller_register_api.as_view(),name="agg_hhc_app_caller_register_api"),
    path('OTPLOGIN',views.OTPLOGIN.as_view(),name="OTPLOGIN"),
    path('OTPCHECK',views.OTPCHECK.as_view(),name="OTPCHECK"),
    path('agg_hhc_app_services_api',views.agg_hhc_app_services_api.as_view()),
    path('add_family_member',views.add_family_member.as_view()),
    path('add_multiple_address_api', views.add_multiple_address_api.as_view()),
    path('agg_hhc_app_caller_relation_api', webviews.agg_hhc_caller_relation_api.as_view()),
    path('agg_hhc_app_patient_by_caller_api/<int:pk>/', views.agg_hhc_app_patient_by_caller_api.as_view()),
    path('agg_hhc_app_address_by_caller_api/<int:pk>/',views.agg_hhc_app_address_by_caller_api.as_view()),
    path('agg_hhc_app_befered_by',views.agg_hhc_app_befered_by.as_view()),
    path('agg_hhc_app_prefered_consultant',views.agg_hhc_app_prefered_consultant.as_view()),
    path('agg_hhc_app_caller_register_api/<int:pk>/',views.agg_hhc_app_caller_register_put_api.as_view()),
    path('agg_hhc_state_api',views.agg_hhc_state_api.as_view()),
    path('agg_hhc_app_address_get_put_delete_api/<int:pk>/',views.agg_hhc_app_address_get_put_delete_api.as_view()),
    path('agg_hhc_sub_services_from_service/<int:pk>',views.agg_hhc_sub_services_from_service.as_view()), #this api will de used in web as well as app
    path('agg_hhc_patient_doc_detail', views.agg_hhc_patient_doc_detail.as_view())
]

