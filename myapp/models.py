from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore
from django.core.validators import FileExtensionValidator

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
    tool = models.ForeignKey(Tools, related_name='tool',on_delete=models.CASCADE)
    collection = models.ForeignKey(Collections, related_name='illustrations', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} _ {self.tool} _ {self.description}"
    
    
class Video(models.Model):
    file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])])
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    illustration = models.ForeignKey(Illustration, related_name='videos', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class User(AbstractUser):
    collections = models.ManyToManyField(Collections, blank= True, related_name="myapp_user")

    avatar = models.ImageField(null=True, default= 'avatar.png' )


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE) 
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body


