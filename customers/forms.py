from django import forms

from .models import Customer

class customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'org_name',
            'contact_name',
            'phone_number',
            'email', 
            'conversation_date',
            'renewal_date',
            'start_date',
            'subscription_used_date',
            'payment_cycle',
            'gst_no',
            )
        widgets = {
            'conversation_date' : forms.DateInput(attrs={'type' :"date"}),
            'renewal_date' : forms.DateInput(attrs={'type' :"date"}),
            'start_date' : forms.DateInput(attrs={'type' :"date"}),
            'subscription_used_date' : forms.DateInput(attrs={'type' :"date"}),
        }          