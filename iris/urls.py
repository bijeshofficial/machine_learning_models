from django.urls import path
from . import views

app_name = 'iris'

urlpatterns = [
    path('', views.iris,  name = 'iris'),
]
