from django.db import models
from profiles.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField



class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name = 'sender')
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='recipient')
    content = RichTextUploadingField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}"

