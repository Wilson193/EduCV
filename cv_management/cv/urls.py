from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='cv'),
    path('create/', create , name='create'),
    path('update/', update, name='update'),
    path('modifyPrivacy/', modify_privacy, name='modify_privacy'),
    path('consult/', consult , name='consult'),
    path('list_cvs/', list_cvs , name='list_cvs'),
    path('register_experience/', register_experience , name='register_experience'),
]