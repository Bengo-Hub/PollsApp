from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('candidate/register/',create_candidate,name="candidate_register"),
]