from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Lead

class LeadCreationForm(forms.ModelForm):

    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='ZA'), required=False
    ) 

    mobile_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='ZA'), required=False
    ) 

    company_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='ZA'), required=False
    ) 

    class Meta:
        model = Lead
        fields = '__all__'
        
