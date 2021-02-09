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
        return f"{self.user}-{self.created}"
    
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()



class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = RichTextUploadingField(max_length=1000, blank=True, null=True, verbose_name="post")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='author')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
  
  

class Comments(models.Model):
      body = RichTextUploadingField(max_length=150, blank=True, null=True, verbose_name='comments')
      post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True,blank=True)
      author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='comment_author')
      date_create = models.DateTimeField(auto_now_add=True)

      def __str__(self):
        return '%s - %s - %s' % (self.post, self.author, self.body)