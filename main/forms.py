from django import forms
from django.forms import inlineformset_factory

from .models import DataUnit


class DataUnitCreateForm(forms.ModelForm):
    class Meta:
        model = DataUnit
        fields = '__all__'
        widgets = {
            'creator': forms.HiddenInput,
            'customers': forms.HiddenInput,
            'archivated': forms.HiddenInput,
        }

