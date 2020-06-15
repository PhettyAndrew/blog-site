from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
            'message': forms.TextInput(attrs={'placeholder': 'We appreciate your Feedback...'}),
        }
        fields = ['name', 'email', 'receive_newsletter', 'message']