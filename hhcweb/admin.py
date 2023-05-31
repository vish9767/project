from django.contrib import admin
# Register your models here.
from . models import *
# Register your models here.
admin.site.register(agg_hhc_patinet_list_enquiry)#1
admin.site.register(agg_hhc_assessment_patient)#2
admin.site.register(agg_hhc_assessment_patient_details)#3
admin.site.register(agg_hhc_assessment_patient_list)#4
admin.site.register(agg_hhc_patients)#6
#admin.site.register(agg_hhc_webinar_patient_table)#7
admin.site.register(agg_hhc_detailed_event_plan_of_care)#8
admin.site.register(agg_hhc_events)#9
admin.site.register(agg_hhc_event_consultant_call)#10
admin.site.register(agg_hhc_event_doctor_mapping)#11
admin.site.register(agg_hhc_event_follow_up)#12
admin.site.register(agg_hhc_event_job_summary)#13
admin.site.register(agg_hhc_event_other_call)#14
admin.site.register(agg_hhc_event_plan_of_care)#15
admin.site.register(agg_hhc_event_professional)#16
admin.site.register(agg_hhc_event_requirements)#17
admin.site.register(agg_hhc_event_share_hcm)#18
admin.site.register(agg_hhc_log_for_event)#19
admin.site.register(agg_hhc_callers)#20
admin.site.register(agg_hhc_caller_relation)#21
admin.site.register(agg_hhc_conference_call)#22
admin.site.register(agg_hhc_sp_incoming_call)#23
admin.site.register(agg_hhc_outgoing_call)#24
#class admin_agg_hhc_purpose_call(admin.ModelAdmin):#25
#    list_display=['name','status']
admin.site.register(agg_hhc_purpose_call)#25admin.site.register(agg_hhc_purpose_call,admin_agg_hhc_purpose_call)
admin.site.register(agg_hhc_extend_service)#26
admin.site.register(agg_hhc_no_reason_for_service)#27
admin.site.register(agg_hhc_professional_services)#28
admin.site.register(agg_hhc_professional_sub_services)#29
admin.site.register(agg_hhc_services)#30
admin.site.register(agg_hhc_service_membership_registration)#31
admin.site.register(agg_hhc_service_professionals)#32
admin.site.register(agg_hhc_service_professional_details)#33
admin.site.register(agg_hhc_sub_services)#34
admin.site.register(agg_hhc_jobclosure_detail_datewise)#35
#admin.site.register(agg_hhc_jobclosure_detail_datewise_old)#36
admin.site.register(agg_hhc_job_closure)#37
admin.site.register(agg_hhc_job_closure_consumption_mapping)#38
admin.site.register(agg_hhc_feedbackform1)#39
admin.site.register(agg_hhc_feedback_answers)#40
admin.site.register(agg_hhc_feedback_form)#41
admin.site.register(agg_hhc_feedback_for_app)#42
admin.site.register(agg_hhc_feedback_options)#43
admin.site.register(agg_hhc_assisted_living_schedule)#44
admin.site.register(agg_hhc_membership_schedule_detail)#45
admin.site.register(agg_hhc_professional_scheduled)#46
admin.site.register(agg_hhc_reschedule_session)#47
admin.site.register(agg_hhc_payments_received_by_professional)#48
admin.site.register(agg_hhc_professional_availability)#49
admin.site.register(agg_hhc_professional_availability_detail)#50
admin.site.register(agg_hhc_professional_device_info)#51
admin.site.register(agg_hhc_professional_documents)#52
admin.site.register(agg_hhc_professional_location)#53
admin.site.register(agg_hhc_professional_location_details)#54
admin.site.register(agg_hhc_professional_location_preferences)#55
admin.site.register(agg_hhc_professional_media)#56
admin.site.register(agg_hhc_professional_notification)#57
admin.site.register(agg_hhc_professional_password)#58
admin.site.register(agg_hhc_professional_weekoff)#59
admin.site.register(agg_hhc_admin_users)#60
admin.site.register(agg_hhc_admin_users_modules)#61
admin.site.register(agg_hhc_admin_user_hospital_mapping)#62
admin.site.register(agg_hhc_assisted_living_booking)#63
admin.site.register(agg_hhc_attendance_details)#64
admin.site.register(agg_hhc_avaya_extensions)#65
admin.site.register(agg_hhc_bank_details)#66
admin.site.register(agg_hhc_cancellation_history)#67
admin.site.register(agg_hhc_change_status)#68
admin.site.register(agg_hhc_cheque_images)#69
admin.site.register(agg_hhc_city)#70
admin.site.register(agg_hhc_consent_agree_form)#71
admin.site.register(agg_hhc_consumables)#72
admin.site.register(agg_hhc_content)#73
admin.site.register(agg_hhc_dash_count_details)#74
admin.site.register(agg_hhc_device_version_info)#75
admin.site.register(agg_hhc_doctors_consultants)#76
admin.site.register(agg_hhc_documetns_list)#77
admin.site.register(agg_hhc_doc_con)#78
admin.site.register(agg_hhc_employees)#79
admin.site.register(agg_hhc_emp_spero)#80
admin.site.register(agg_hhc_enquiry_follow_up)#81
admin.site.register(agg_hhc_enquiry_requirements)#82
admin.site.register(agg_hhc_hospitals)#83
admin.site.register(agg_hhc_hospital_ips)#84
admin.site.register(agg_hhc_knowledge_base_documents)#85
admin.site.register(agg_hhc_locations)#86
admin.site.register(agg_hhc_log_location_for_session)#87
admin.site.register(agg_hhc_manager_spero)#88
#admin.site.register()#89
#admin.site.register()#90
admin.site.register(agg_hhc_modules)#91
admin.site.register(agg_hhc_ongoing_remark_history)#92
admin.site.register(agg_hhc_payments)#93
admin.site.register(agg_hhc_payment_details)#94
#admin.site.register()#95
#admin.site.register()#96
#admin.site.register()#97
admin.site.register(agg_hhc_restriction_for_session_complete)#98
admin.site.register(agg_hhc_session)#99
admin.site.register(agg_hhc_sms_response)#100
admin.site.register(agg_hhc_source_of_enquiry)#101
admin.site.register(agg_hhc_specialty)#102
admin.site.register(agg_hhc_tc_examination)#103
admin.site.register(agg_hhc_teleconsultation_enquiry)#104
admin.site.register(agg_hhc_user_activity)#105
admin.site.register(agg_hhc_vc_diagnosis)#106
admin.site.register(agg_hhc_vc_fam_his)#107
admin.site.register(agg_hhc_vc_investigation)#108
admin.site.register(agg_hhc_vc_med_his)#109
admin.site.register(sp_vc_prescription)#110
admin.site.register(agg_hhc_video_consulting)#111
admin.site.register(agg_hhc_gender)#112