from django.shortcuts import render, get_object_or_404
from .models import Article, Comments
from profiles.models import Profile
from .forms import CommentForm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'posts/index.html')


def comments(request, id):
    comm_form = CommentForm() 
    #profiles = get_object_or_404(Profile, id=id)
   # comm_post = profiles.author.get(Article_id=id)
    comm_post = get_object_or_404(Article, id=id)
    comments = comm_post.comments_post.filter()
    if request.method == "POST":
        comm_form = CommentForm(request.POST, request.FILES)
        if  comm_form.is_valid():
            new_comment = comm_form.save(commit=False)
            now_user = Profile.objects.get(user=request.user)
            new_comment.author = now_user
            new_comment.post = comm_post
            new_comment.save()
            return HttpResponseRedirect(f'/comments/{id}')
            # return HttpResponseRedirect(f'/comments/{id}')
    else:
        comm_form = CommentForm()
        context = {'comm_post': comm_post, 'comments': comments,
                   'comm_form': comm_form}
        return render(request, 'posts/comments.html', context)


