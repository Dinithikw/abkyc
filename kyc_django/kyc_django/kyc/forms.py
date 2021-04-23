from django import forms
from .models import Kyc_Infotemp, Kyc_Info


class update_forms(forms.ModelForm):
    class Meta:
        model = Kyc_Infotemp
        fields = '__all__'

class accept_form(forms.ModelForm):
    class Meta:
        model = Kyc_Info
        fields = '__all__'