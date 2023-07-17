from django.urls import path
from hhcweb import views

urlpatterns = [
    path('agg_hhc_purpose_call_api',views.agg_hhc_purpose_call_api.as_view()),#done
    path('agg_hhc_caller_relation_api',views.agg_hhc_caller_relation_api.as_view()),#done
    path('agg_hhc_locations_api',views.agg_hhc_locations_api.as_view()),
    path('agg_hhc_services_api',views.agg_hhc_services_api.as_view()),
    path('agg_hhc_sub_services_api/<int:pk>',views.agg_hhc_sub_services_api.as_view()),
    path('agg_hhc_gender_api',views.agg_hhc_gender_api.as_view()),#done
    path('agg_hhc_patients_api',views.agg_hhc_patients_api.as_view()),
    path('get_latest_patient_record_from_caller_id_api/<int:pk>/',views.get_latest_patient_record_from_caller_id_api.as_view()),
    # path('agg_hhc_add_'),
    path('agg_hhc_patinet_list_enquiry_api',views.agg_hhc_patinet_list_enquiry_api.as_view()),#done
    path('agg_hhc_patinet_list_enquiry_put/<int:pk>/',views.agg_hhc_patinet_list_enquiry_put.as_view()),
    path('agg_hhc_callers_api',views.agg_hhc_callers_api.as_view()),#done
    path('agg_hhc_patient_from_callers_phone_no/<str:pk>/',views.agg_hhc_callers_phone_no.as_view()),#done
    path('agg_hhc_add_service_details_api', views.agg_hhc_add_service_details_api.as_view()),
    path('agg_hhc_hospitals_api',views.agg_hhc_hospitals_api.as_view()),#done
    path('agg_hhc_callers_phone_no_status_mobile_api',views.agg_hhc_callers_phone_no_status_mobile_api.as_view()),
    path('agg_hhc_callers_phone_no_status_web_api',views.agg_hhc_callers_phone_no_status_web_api.as_view()),
    path('agg_hhc_callers_phone_no_status_walking_api',views.agg_hhc_callers_phone_no_status_walking_api.as_view()),
    path('agg_hhc_callers_phone_no_status_calling_api',views.agg_hhc_callers_phone_no_status_calling_api.as_view()),
    path('agg_hhc_pincode_api',views.agg_hhc_pincode_api.as_view()),#all pincode get api
    path('agg_hhc_pincode_api/<str:pin>',views.agg_hhc_pincode_number_api.as_view()),#find state and city from pincode number
    path('agg_hhc_city_from_state_api/<str:state>',views.agg_hhc_city_from_state_api.as_view()),#find all city from state name
    path('agg_hhc_pincode_from_city_api/<str:city>',views.agg_hhc_pincode_from_city_api.as_view()),#find all findcode from city name 
    path('Caller_details_api/<int:pk>', views.Caller_details_api.as_view()),
    path('Caller_details_api/<int:pk>', views.Caller_details_api.as_view()),
    path('patient_detail_info_api/<int:pk>', views.patient_detail_info_api.as_view()),
    path('agg_hhc_service_professionals_api',views.agg_hhc_service_professionals_api.as_view()),#this display professional name and skills
    path('calculate_total_amount',views.calculate_total_amount.as_view()),
    path('calculate_discount_api',views.calculate_discount_api.as_view())

]
