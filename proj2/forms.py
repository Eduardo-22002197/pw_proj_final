from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'input-field', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs = {'class': 'input-field', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs = {'class': 'input-field', 'placeholder': 'Phone'}),
            'email': forms.TextInput(attrs = {'class': 'input-field', 'placeholder': 'Email'}),
            'date_birth': forms.DateInput(attrs = {'class': 'input-field', 'placeholder': 'Date Birth'}),
        }

        labels = {
            'name': '',
            'last_name': '',
            'phone': '',
            'email': '',
            'date_birth': '',
        }