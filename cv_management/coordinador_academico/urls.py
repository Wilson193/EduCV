from django.urls import path
from .views import *

urlpatterns = [
    path('settings/', settings, name='settings'),
    path('update_coordinator/', update_coordinator, name='update_coordinator'),
    path('reset_password/', reset_password, name='reset_password'),
]