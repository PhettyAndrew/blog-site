from django import forms
from .models import Contact, ImagePost, VideoPost, YoutubePost


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
        }
        fields = ['name', 'email', 'receive_newsletter', 'message']


class TextPostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of Post'}),
            'description': forms.TextInput(attrs={'placeholder': 'A brief description of Post'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author of Post'}),
        }
        fields = ['image', 'category', 'title', 'description', 'author', 'story']


class VideoPostForm(forms.ModelForm):
    class Meta:
        model = VideoPost
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of Post'}),
            'description': forms.TextInput(attrs={'placeholder': 'A brief description of Post'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author of Post'}),
        }
        fields = ['video', 'category', 'title', 'description', 'author', 'story']


class YoutubePostForm(forms.ModelForm):
    class Meta:
        model = YoutubePost
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'Url of Video'}),
            'title': forms.TextInput(attrs={'placeholder': 'Title of Post'}),
            'description': forms.TextInput(attrs={'placeholder': 'A brief description of Post'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author of Post'}),
        }
        fields = ['url', 'category', 'title', 'description', 'author', 'story']
