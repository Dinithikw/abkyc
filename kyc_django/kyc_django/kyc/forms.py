from django import forms
from .models import Kyc_Infotemp


class update_forms(forms.ModelForm):
    class Meta:
        model = Kyc_Infotemp
        fields = '__all__'
