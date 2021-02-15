from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from profiles.models import Profile



class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = RichTextUploadingField(max_length=1000,verbose_name="post")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='author')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date_create}'
  
  

class Comments(models.Model):
      body = RichTextUploadingField(max_length=150, verbose_name='your comment:')
      post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_post')
      author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='comment_author')
      date_create = models.DateTimeField(auto_now_add=True)

      def __str__(self):
        return '%s - %s - %s' % (self.post, self.author, self.body)