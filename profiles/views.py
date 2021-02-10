from django.shortcuts import render, get_object_or_404
from .models import Profile
from posts.models import Article, Comments
from django.http import HttpResponseRedirect
from .forms import AvatarForm
from posts.forms import ArticleForm, CommentForm



def list_users(request):
    users = Profile.objects.all()
    context = {'users':users}
    return render(request, 'profiles/list_users.html', context)


    
def profiles(request, pk=0):
    post_form = ArticleForm()
    now_user = Profile.objects.get(user=request.user) # require user
    posts = Article.objects.filter(author=now_user) # posts require users
    profile = Profile.objects.get(id=pk) # users not require 
    posts_other = profile.author.all() # posts not require users
    if request.method == "POST":
        post_form = ArticleForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            now_user = Profile.objects.get(user=request.user)
            new_post.author = now_user
            new_post.save()
            return HttpResponseRedirect(f'/profile/{pk}')
    context = {  'profile':profile, 
                 'posts_other':posts_other,
                 'post_form' : post_form,
                 'posts' : posts
                 }
    return render(request, 'profiles/account.html', context)





def image_upload_view(request):
    """Process images uploaded by users"""
    pass