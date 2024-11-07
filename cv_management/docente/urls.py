from django.urls import path
from .views import *

urlpatterns = [
    path('update_teacher/', update_teacher, name='update_teacher')
]