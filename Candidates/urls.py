from django.urls import path
from .views import candidate_list

urlpatterns=[
    path('list/view/',candidate_list,name='candidate-list')#http://localhost:8000/
]