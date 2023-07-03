from django.urls import path
from hhcweb import views
urlpatterns = [
    path('agg_hhc_caller_relation_api',views.agg_hhc_caller_relation_api.as_view()),
    path('agg_hhc_purpose_call_api',views.agg_hhc_purpose_call_api.as_view()),
    path('agg_hhc_locations_api',views.agg_hhc_locations_api.as_view()),
    path('agg_hhc_services_api',views.agg_hhc_services_api.as_view()),
    path('agg_hhc_sub_services_api',views.agg_hhc_sub_services_api.as_view()),
    path('agg_hhc_gender_api',views.agg_hhc_gender_api.as_view()),
    path('agg_hhc_patients_api',views.agg_hhc_patients_api.as_view()),
    path('get_latest_patient_record_from_caller_id_api/<int:pk>/',views.get_latest_patient_record_from_caller_id_api.as_view()),
    # path('agg_hhc_add_'),
    path('agg_hhc_patinet_list_enquiry_api',views.agg_hhc_patinet_list_enquiry_api.as_view()),
    path('agg_hhc_patinet_list_enquiry_put/<int:pk>/',views.agg_hhc_patinet_list_enquiry_put.as_view()),
    path('agg_hhc_callers_api',views.agg_hhc_callers_api.as_view()),
    path('agg_hhc_patient_from_callers_phone_no/<str:pk>/',views.agg_hhc_callers_phone_no.as_view()),
    path('agg_hhc_add_service_details_api', views.agg_hhc_add_service_details_api.as_view()),
    path('agg_hhc_hospitals_api',views.agg_hhc_hospitals_api.as_view()),
    path('agg_hhc_callers_phone_no_status_mobile_api',views.agg_hhc_callers_phone_no_status_mobile_api.as_view()),
    path('agg_hhc_callers_phone_no_status_web_api',views.agg_hhc_callers_phone_no_status_web_api.as_view()),
    path('agg_hhc_callers_phone_no_status_walking_api',views.agg_hhc_callers_phone_no_status_walking_api.as_view()),
    path('agg_hhc_callers_phone_no_status_calling_api',views.agg_hhc_callers_phone_no_status_calling_api.as_view()),
    path('agg_hhc_record_api',views.agg_hhc_record_api.as_view()),

]
