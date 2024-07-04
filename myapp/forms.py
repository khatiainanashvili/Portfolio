from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Collections, Illustration, Tools


class CollectionForm(ModelForm):
    class Meta: 
        model = Collections
        fields = '__all__'


class IllustrationForm(ModelForm):
    class Meta: 
        model = Illustration
        fields = '__all__'


class ToolsForm(ModelForm):
    class Meta: 
        model = Tools
        fields = '__all__'