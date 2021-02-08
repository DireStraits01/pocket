from django.shortcuts import render
from .models import Profile, Article
from django.http import HttpResponseRedirect
from .forms import ArticleForm, AvatarForm, CommentForm

def list_users(request):
    users = Profile.objects.all()
    context = {'users':users}
    return render(request, 'profiles/list_users.html', context)

def account(request):
    form = ArticleForm
    now_user = Profile.objects.get(user=request.user)
    posts = Article.objects.filter(author=now_user)
    if request.method == "POST":
            #if request.user == item.user:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect('/profile/account')
    context = {'form': form, 'posts':posts }
    return render(request, 'profiles/account.html', context)


def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    posts = profile.author.all()
    p_comments = Article.objects.get(id=pk)
    comments = p_comments.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid:
            new_comment = form.save(commit=False)
            now_user = Profile.objects.get(user=request.user)
            new_comment.author = now_user
            new_comment.save()
            return HttpResponseRedirect(f'/profile/profile_detail/{pk}')

    context = {'profile':profile, 'posts':posts, 'form': form, 'comments':comments}
    return render(request, 'profiles/profile_detail.html', context)        



def image_upload_view(request):
    """Process images uploaded by users"""
    pass