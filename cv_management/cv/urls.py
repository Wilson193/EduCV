from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='cv'),
    path('register/', register , name='register'),
    path('modify/', modify, name='modify'),
    path('modifyPrivacy/', modify_privacy, name='modify_privacy'),
    path('consult/', consult , name='consult'),
    path('list_cvs/', list_cvs , name='list_cvs'),
]