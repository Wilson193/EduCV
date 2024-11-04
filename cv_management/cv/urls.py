from django.urls import path
from .views import index, create_cv

urlpatterns = [
    path('', index, name='cv'),
    path('create/', create_cv , name='cv'),
]