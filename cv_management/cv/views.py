from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
  template = loader.get_template('users.html')
  return HttpResponse(template.render())

def create_cv(request):
  template = loader.get_template('teachers.html')
  return HttpResponse(template.render())


def register(request):
    return render(request, 'register.html')
  
def consult(request):
    return render(request, 'consult.html')

def modify(request):
    return render(request, 'modify.html')

def modify_privacy(request):
    return render(request, 'modify-privacy.html')


@login_required
def privacidad(request):
    return render(request, 'pages/privacidad.html')
# Create your views here.
