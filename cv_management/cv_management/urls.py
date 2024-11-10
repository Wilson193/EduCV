from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings

from . import views

#handler404 = 'cv_management.views.custom_404_view'

urlpatterns = [
    path('cv/', include('cv.urls')),
    path('academic_coordinator/', include('coordinador_academico.urls')),
    path('teacher/', include('docente.urls')),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset/', views.resetpassword, name='reset-password'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)