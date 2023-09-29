from django.urls import path
from hhcweb import views
from hhcweb.views import UserRegistrationView, UserLoginView, LogoutView,combined_info
# from .views import AggHHCServiceProfessionalAPIView


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
    # path('agg_hhc_patinet_list_enquiry_api',views.agg_hhc_patinet_list_enquiry_api.as_view()),#done
    path('agg_hhc_patinet_list_enquiry_put/<int:pk>/',views.agg_hhc_patinet_list_enquiry_put.as_view()),
    path('agg_hhc_callers_api',views.agg_hhc_callers_api.as_view()),#done
    path('agg_hhc_patient_from_callers_phone_no/<int:pk>/',views.agg_hhc_callers_phone_no.as_view()),#find all patients from caller number 
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
    path('Service_requirment_api/<int:pk>', views.Service_requirment_api.as_view()),
    path('agg_hhc_service_professionals_api',views.agg_hhc_service_professionals_api.as_view()),#this display professional name and skills
    path('calculate_total_amount/<int:cost>/<str:start_date>/<str:end_date>/',views.calculate_total_amount.as_view()),
    path('calculate_discount_api/<int:dtype>/<int:damount>/<int:total_amt>',views.calculate_discount_api.as_view()),
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
    path('agg_hhc_zone_api/<int:pk>',views.agg_hhc_zone_api.as_view()),# Display List of Zones
    path('agg_hhc_sub_srv/',views.agg_hhc_sub_srv.as_view()),# Display List of Sub Services
    path('agg_hhc_event_professional_api/',views.agg_hhc_service_professional_api.as_view()), # Display List of Professionals (all) OR (with filter:- Services, Zones)
    path('agg_hhc_detailed_event_plan_of_care/',views.agg_hhc_detailed_event_plan_of_care_api.as_view()), # Display All Events against perticular professional 
    path('agg_hhc_detailed_event_plan_of_care_per_day/',views.agg_hhc_detailed_event_plan_of_care_per_day_api.as_view()),# Display all the TOADY'S events against perticular professional 
    #-------------------------------------------mohin---------------------------------------------------------
    path('service_request/',views.combined_info.as_view()),
    #-----------------------------mayank-----------------------------
    # path('service-professionals/', AggHHCServiceProfessionalAPIView.as_view(), name='service-professional-api'),
    path('total_services/', views.total_services, name='total-services-list'),
    path('create_payment/', views.create_payment_url, name='create_payment_url'),
    path('cashfree-webhook/', views.cashfree_webhook, name='cashfree_webhook'),
    path('payment-detail/',views.PaymentDetailAPIView.as_view(), name='payment-detail-api'),
    path('jjob-type-count/<int:period>/', views.JjobTypeCountAPIView.as_view(), name='job-type-count'),


    # -------------------- vinayak ------------------

    path('ongoing_service', views.OngoingServiceView.as_view()),
    path('service_reschedule/<int:eve_id>/',views.service_reschedule_view.as_view()),
    path('prof_reschedule/<int:eve_id>/', views.Professional_Reschedule_Apiview.as_view()),
    path('service_cancellation/<int:eve_id>', views.ServiceCancellationView.as_view()),
    path('professional_availability_api/<int:srv_id>/',views.get_all_avail_professionals.as_view()),

    path('srv_cancel_count_dash/<int:id>', views.srv_canc_count.as_view()),
    path('srv_dtl_dash/<int:id>', views.srv_dtl_dash.as_view()),    

    #-------------------------------------------Amit---------------------------------------------------------
    path('Follow_Up_combined_table/', views.agg_hhc_service_enquiry_list_combined_table_view.as_view()),
    path('previous_follow_up/<int:event_id>/', views.agg_hhc_enquiry_previous_follow_up_APIView.as_view()),
    path('Add_follow_up/', views.agg_hhc_enquiry_Add_follow_up_APIView.as_view()),
    path('cancellation_reason_follow_up_list/<int:pk>', views.agg_hhc_enquiry_followUp_cancellation_api.as_view()),
    path('cancel_follow_up/', views.agg_hhc_enquiry_Add_follow_up_Cancel_by_APIView.as_view()),
    path('create_service_follow_up/', views.agg_hhc_enquiry_Add_follow_up_create_service_APIView.as_view()),
    # path('previous_follow_up/', views.agg_hhc_enquiry_previous_follow_up_APIView.as_view()),

    # path('cancel_spero_follow_up/', views.agg_hhc_enquiry_Add_follow_up_Cancel_by_Spero_APIView.as_view()),
    # path('cancel_patent_follow_up/', views.agg_hhc_enquiry_Add_follow_up_Cancel_by_Patent_APIView.as_view()),    
# ------------------------------------------Sandip-------------------------------------------------
    path('agg_hhc_add_service_details_api/', views.agg_hhc_add_service_details_api.as_view()),
    path('agg_hhc_add_service_form_api/', views.agg_hhc_add_service_form_api.as_view()),
    path('agg_hhc_add_service_details_api/<int:pk>', views.agg_hhc_add_service_details_api.as_view()),
    path('agg_hhc_consultant_api/',views.agg_hhc_consultant_api.as_view()),
    path('agg_hhc_state_api',views.agg_hhc_state_api.as_view()),
    path('agg_hhc_city_api/<int:pk>',views.agg_hhc_city_api.as_view()),
    path('agg_hhc_patient_by_HHCID/<str:pk>',views.agg_hhc_patient_by_HHCID.as_view()),
    path('agg_hhc_srv_req_prof_allocate/<int:pk>',views.agg_hhc_srv_req_prof_allocate.as_view()),
    path('get_payment_details/<int:pk>',views.get_payment_details.as_view()),
    

#------------------------------------------Vishal-----------------------------------------------_
    path('coupon_code_post_api/<str:code>/<int:total_amt>',views.coupon_code_post_api.as_view()),
    path('coupon_code_api',views.coupon_code_api.as_view()),
    path('allocate_api',views.allocate_api.as_view()),
    path('Dashboard_enquiry_count_api/<int:id>',views.Dashboard_enquiry_count_api.as_view()),
    path('Dashboard_enquiry_status_count_api/<int:id>',views.Dashboard_enquiry_status_count_api.as_view()),
]

