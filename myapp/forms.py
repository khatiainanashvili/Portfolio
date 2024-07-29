from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Collections, Illustration, Tools, User, Video


class CollectionForm(ModelForm):
    class Meta: 
        model = Collections
        fields = '__all__'

class IllustrationForm(forms.ModelForm):
    class Meta:
        model = Illustration
        fields = ['image', 'tool', 'collection']
        widgets = {
            'collection': forms.Select(attrs={'required': False}),
        }




class ToolsForm(ModelForm):
    class Meta: 
        model = Tools
        fields = '__all__'


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['avatar', 'username']


class CollectionUpdateForm(ModelForm):
    class Meta: 
        model = Collections 
        fields = '__all__'

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['file', 'name', 'illustration']
