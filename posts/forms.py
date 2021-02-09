from django.forms import ModelForm
from .models import Article, Comments

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ( 'body',)


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)       