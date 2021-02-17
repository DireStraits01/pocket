from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import Profile
from posts.models import Article, Comments
from django.http import HttpResponseRedirect
from .forms import AvatarForm
from posts.forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required



def list_users(request):
    users = Profile.objects.all()
    context = {'users':users}
    return render(request, 'profiles/list_users.html', context)


def list_posts(request):
    posts = Article.objects.all()[::-1]
    context = {'posts':posts}
    return render(request, 'profiles/list_posts.html', context)


    
def profileDetailView(request, id):
    post_form = ArticleForm()
    profile = Profile.objects.get(id=id)
    now_user = Profile.objects.get(user=request.user) # require user
    posts = Article.objects.filter(author=now_user) # posts require users
    posts_other = profile.author.all() # posts not require users

   
    # count comment for request user
    if request.method == "POST":
        post_form = ArticleForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            now_user = Profile.objects.get(user=request.user)
            new_post.author = now_user
            new_post.save()
            return redirect(f'/profile/{id}/detail/')

 
    context = {  'profile':profile, 
                 'posts_other':posts_other,
                 'post_form' : post_form,
                 'posts' : posts,
                
                 }
    return render(request, 'profiles/account.html', context)




def change_avatar(request,id=0):
    now_user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        ava_form = AvatarForm(request.POST, instance=now_user)
        if ava_form.is_valid():
            ava_form.save()
            if request.FILES.get('avatar', None) != None:
                try:
                    os.remove(now_user.avatar.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                now_user.avatar = request.FILES['avatar']
                now_user.save()
            return redirect('change_avatar', id=now_user.id)        
    ava_form = AvatarForm(instance=now_user)        
    return render(request, 'profiles/change_avatar.html', {'ava_form':ava_form})
