from django import forms
from .models import Docente
#wilson
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
