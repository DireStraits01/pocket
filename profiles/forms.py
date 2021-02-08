from django.forms import ModelForm
from .models import Article, Profile, Comments
from django.contrib.auth import get_user_model

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ( 'body',)

class AvatarForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)       