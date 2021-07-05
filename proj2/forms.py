from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Contact, Comment

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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'complete_name': forms.TextInput(attrs = {'class': 'input-field', 'placeholder': 'Complete Name'}),
            'rating_website': forms.NumberInput(attrs = {'class': 'input-field', 'placeholder': '1 to 5 rating...', 'min': 0, 'max': 5}),
            'final_comment': forms.Textarea(attrs = {'class': 'textarea-field input-field', 'placeholder': 'Your comment...'}),
        } 

        labels = {
            'complete_name': '',
            'rating_website': '',
            'final_comment': '',
            'comment_date': ''
        }