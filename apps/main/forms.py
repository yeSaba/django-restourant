from django import forms
from .models import ContactUs, NewsLetter


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Subject"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Message"}),
        }

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }