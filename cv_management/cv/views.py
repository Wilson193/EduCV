from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('users.html')
  return HttpResponse(template.render())

def create_cv(request):
  template = loader.get_template('teachers.html')
  return HttpResponse(template.render())