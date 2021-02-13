from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor_uploader.fields import RichTextUploadingField



class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name  = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, blank=True)
    country = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(default = 'avatar.svg', upload_to = 'avatars/%Y/%m/%d', blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


    

