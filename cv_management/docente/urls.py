from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_teacher/', update_teacher, name='update_teacher'),
    path('update_picture', update_picture, name= 'update_picture'),
    path('<int:docente_id>/curriculum/',generate_curriculum, name='generate_curriculum_editable'),
    
]