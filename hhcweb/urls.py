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
]