from django.urls import path
from . import views
urlpatterns=[
#    path('agg_hhc_app_caller_register_api',views.agg_hhc_app_caller_register_api.as_view(),name="agg_hhc_app_caller_register_api")
    path('OTPLOGIN',views.OTPLOGIN.as_view(),name="OTPLOGIN"),
    path('OTPCHECK',views.OTPCHECK.as_view(),name="OTPCHECK")
]