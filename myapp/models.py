from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore


class Tools(models.Model):
    name = models.CharField(max_length= 50)
    def __str__(self):
        return self.name


class Collections(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Illustration(models.Model):
    name = models.CharField(max_length=20)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE, related_name='illustrations')
    tools = models.ManyToManyField(Tools, blank=True, related_name="tools")
    image = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True)
    tags = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name} - {self.collection.title}"




class User(AbstractUser):
    collections = models.ManyToManyField(Collections, blank= True, related_name="myapp_user")

