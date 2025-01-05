from django import forms
from .models import Tirada

class TiradaForm(forms.ModelForm):
    class Meta:
        model = Tirada
        fields = '__all__'
        exclude = ['usuario']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
