from django.urls import path
from hhcweb import views
from hhcweb.views import UserRegistrationView, UserLoginView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
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
    path('agg_hhc_city_state_from_zone_api/<int:city_id>',views.agg_hhc_city_state_from_zone_api.as_view()),#this table is used to get city name and state name
    path('agg_hhc_pincode_from_city_api/<str:city>',views.agg_hhc_pincode_from_city_api.as_view()),#find all findcode from city name 
    path('Caller_details_api/<int:pk>', views.Caller_details_api.as_view()),
    path('patient_detail_info_api/<int:pk>', views.patient_detail_info_api.as_view()),
    path('agg_hhc_service_professionals_api',views.agg_hhc_service_professionals_api.as_view()),#this display professional name and skills
    path('calculate_total_amount/<int:cost>/<str:start_date>/<str:end_date>/',views.calculate_total_amount.as_view()),
    path('calculate_discount_api/<int:dtype>/<int:damount>/<int:total_amt>',views.calculate_discount_api.as_view()),
    path('Service_requirment_api', views.Service_requirment_api.as_view()),
    path('agg_hhc_feedback_answers_api/<int:agg_sp_pt_id>',views.agg_hhc_feedback_answers_api.as_view()),#this display rating and review from patient id
    path('last_patient_service_info/<int:pt_id>',views.last_patient_service_info.as_view()),#this is to display patient last service name and last start and end service date
    path('agg_hhc_professional_zone_api',views.agg_hhc_professional_zone_api.as_view()),
    path('agg_hhc_professional_scheduled_api/<int:prof_sche_id>',views.agg_hhc_professional_scheduled_api.as_view()),#To display professional time in calander as well as in professional availability
    path('agg_hhc_professional_time_availability_api/<int:prof_sche_id>',views.agg_hhc_professional_time_availability_api.as_view()),#used to display professional booked services in professional Avalibility
    path('total_services/<int:service_professional_id>/', views.total_services, name='total_services'),#this display total services for Professionals
    path('agg_hhc_service_professionals/', views.AggHHCServiceProfessionalListAPIView.as_view(),name='agg_hhc_service_professional-list'),#mayank
    #--------------------------------------------Dashboard------------Api--------------------------------------
    path('service_details_today_total_services',views.service_details_today_total_services.as_view()),
    #-----------------------------------------nikita_p--------------------------------------
    path('agg_hhc_zone_api',views.agg_hhc_zone_api.as_view()),
    path('agg_hhc_event_professional_api/<zone>/',views.agg_hhc_service_professional_api.as_view()),
    path('agg_hhc_detailed_event_plan_of_care/<zone>/',views.agg_hhc_detailed_event_plan_of_care_api.as_view()),
]

