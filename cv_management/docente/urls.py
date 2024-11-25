from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_teacher/', update_teacher, name='update_teacher'),
    path('<int:docente_id>/curriculum/',generate_curriculum, name='generate_curriculum_editable'),
    path('settings_teacher/', settings_teacher, name='settings_teacher'),
    path('reset_password_teacher/', reset_password_teacher, name='reset_password_teacher'),
    path('update_picture_teacher/', update_picture_teacher, name='update_picture_teacher'),
]