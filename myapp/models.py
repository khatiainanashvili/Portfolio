from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore


class Collections(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Tools(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Illustration(models.Model):
    image = models.ImageField(upload_to='illustrations/')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collections, related_name='illustrations', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} _ {self.tool} _ {self.description}"

class User(AbstractUser):
    collections = models.ManyToManyField(Collections, blank= True, related_name="myapp_user")

