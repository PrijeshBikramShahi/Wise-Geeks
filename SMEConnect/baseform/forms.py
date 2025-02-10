from django import forms
from .models import investor, startup

class InvForm(forms.ModelForm):
    class Meta:
        model = investor
        fields = '__all__'

class StartForm(forms.ModelForm):
    class Meta:
        model = startup
        fields = '__all__'