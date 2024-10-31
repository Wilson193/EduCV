from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('CV/', include('cv.urls')),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('teachers/', views.teachers, name='teachers'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
]