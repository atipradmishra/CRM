from dataclasses import field
from random import choices
from colorama import Style
from django.forms import ModelForm

from customers.models import Customer_communication
from .models import Lead, lead_activity , lead_communication,quotation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2' ]

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'agent',
            'size',
            'location',
            'phone_number',
            'designation',
            'email',
            'source',
            'stage',
            'status',
            'pincode',
        )
        widgets = {
            'email' : forms.EmailInput(attrs={'id' : 'email' , 'class':"box" , 'style':'left: 100px;top: 400px;', 'placeholder' : 'Emai**'}),
            'phone_number' : forms.NumberInput(attrs={'class':"box" , 'style':'left: 781px;top: 400px;', 'placeholder' : 'Phone Number**' , 'max_length': '10'}),
            'first_name' : forms.TextInput(attrs={'class':'box', 'style':'top: 220px; left: 101px;', 'placeholder' : 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':"box", 'style':'left: 781px; top: 220px;','placeholder' : 'Last Name'}),
            'agent' : forms.Select(choices=['test'],attrs={'class':'box', 'style':'top: 320px; left: 101px;', 'placeholder' : 'First Name'}),
            'size': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 670px;'}),
            'location': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 490px;'}),
            'designation': forms.TextInput(attrs={'class':"box" , 'style':'left: 781px;top: 670px;'}),
            'source': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 580px;'}),
            'stage': forms.TextInput(attrs={'class':"box" , 'style':'left: 781px;top: 580px;'}),
            'status': forms.TextInput(attrs={'class':"box", 'style':'left: 781px;top: 310px;'}),
            'pincode': forms.TextInput(attrs={'class':"box", 'style':'left: 781px;top: 490px;'}),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'is_converted' ,
        )

class Lead_communication_form(forms.ModelForm):
    class Meta:
        model = lead_communication 
        fields = (
            'message',
            ) 

        widgets = {
            'message' : forms.Textarea(attrs={ 'id' : 'message', 'placeholder': 'Your Conversation here*', 'class' : 'box', 'cols': '50', 'rows': '5' }),
        }



class Lead_activity_form(forms.ModelForm):
    class Meta:
        model = lead_activity
        fields = (
            'activity_name',
            'scheduled_date',
            'actual_date',
            'demo_status',
            )   
        widgets = {
            'scheduled_date' : forms.DateInput(attrs={'type' :"date"}),
            'activity_name' : forms.Select(choices=['ACTIVITY_CHOICES']),
            'actual_date' : forms.DateInput(attrs={'type' :"date"}),
            'demo_status' : forms.Select(choices=['STATUS_CHOICE']), 
        }




class pdf_form(forms.ModelForm):
    class Meta:
        model = quotation
        fields = (
            'lead_id',
            'quotation_file_name',
            'Quantity',
            'product_id',
            'price_offered',
            )   
        widgets = {
            'lead_id' : forms.HiddenInput(attrs={'id' : 'lead_id'}),
            'price_offered': forms.TextInput(attrs={'id':"p_id"}),
        }


class Customer_communication_form(forms.ModelForm):
    class Meta:
        model = Customer_communication
        fields = (
            'message',
            )
        widgets = {
            'message' : forms.Textarea(attrs={ 'id' : 'message', 'placeholder': 'Your Conversation here*', 'class' : 'box', 'cols': '50', 'rows': '5' }),
        }