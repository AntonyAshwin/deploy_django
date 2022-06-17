from django import forms
from .models import FormModel


class FinalForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'
