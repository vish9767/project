from django.urls import path
from . import views

urlpatterns=[
    path('professional_OTPLOGIN',views.professional_OTPLOGIN.as_view())
]