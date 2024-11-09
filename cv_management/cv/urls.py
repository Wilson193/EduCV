from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='cv'),
    path('create/', create , name='create'),
    path('update/', update, name='update'),
    path('modifyPrivacy/', modify_privacy, name='modify_privacy'),
    path('consult/', consult , name='consult'),
    path('teachers/', teachers , name='teachers'),
    path('register_experience/', register_experience , name='register_experience'),
    path('remove_experience/<int:experiencia_id>/', remove_experience , name='remove_experience'),
    path('register_academic_background/', register_academic_background, name='register_academic_background'),
    path('remove_academic_background/<int:formacion_id>/', remove_academic_background , name='remove_academic_background'),
    path('register_academic_production/', register_academic_production, name='register_academic_production'),
    path('remove_academic_production/<int:produccion_id>/', register_academic_production , name='register_academic_production'),
    path('consult/<int:docente_id>/',generate_curriculum, name='nombre_de_la_vista_del_pdf'),
]