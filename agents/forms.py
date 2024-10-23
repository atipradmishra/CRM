from django import forms
from .models import agent


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = agent
        fields = (
            'user',
            'agent_name',
            'organisation',
            'phone_number',
            'email',
        )
        widgets = { 
            'user' : forms.Select(choices=['test'] ,attrs={'class':'box', 'style':'top: 220px; left: 100px;'}),
            'agent_name': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px; top: 310px;'}),
            'organisation': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px; top: 400px;'}),
            'phone_number' : forms.NumberInput(attrs={'class':"box" , 'style':'left: 100px; top: 490px;'}),
            'email': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 580px;'}),
        }


class agentupdateform(forms.ModelForm):
    class Meta:
        model = agent
        fields = (
            'user',
            'agent_name',
            'organisation',
            'phone_number',
            'email',
        )
        widgets = {
            'user' : forms.HiddenInput(attrs={'id' : 'agent_id'}),
            'email' : forms.EmailInput(attrs={'class':"box" , 'style':'left: 100px; top: 490px;'}),
            'agent_name' : forms.TextInput(attrs={'class':'box', 'style':'top: 220px; left: 101px;'}),
            'organisation': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px; top: 310px;'}),
            'phone_number': forms.NumberInput(attrs={'class':"box" , 'style':'left: 100px; top: 400px;'}),
        }