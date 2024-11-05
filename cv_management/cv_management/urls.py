from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('CV/', include('cv.urls')),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('accounts/', include('accounts.urls')),
    path('settings/', views.settings, name='settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset/', views.resetpassword, name='reset-password'),
    path('admin/', admin.site.urls),
]