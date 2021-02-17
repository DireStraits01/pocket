from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comments
from profiles.models import Profile
from .forms import CommentForm
from django.http import HttpResponseRedirect





def comments(request, id):
    comm_form = CommentForm() 
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
            return HttpResponseRedirect(f'/posts/comments/{id}')
            # return HttpResponseRedirect(f'/comments/{id}')
    else:
        context = {'comm_post': comm_post, 'comments': comments,
                   'comm_form': comm_form}
        return render(request, 'posts/comments.html', context)


def delete_post(request, id):
    delete_post = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        user=request.user
        delete_post.delete()
        return redirect('profile',  id = user.id)
    context = { 'delete_post':  delete_post}
    return render(request, 'posts/delete_post.html', context)    


def delete_com(request, id):
    delete_com = get_object_or_404(Comments, id=id)
    post = delete_com.post
    if request.method == 'POST': 
        delete_com.delete()
        return redirect('comments', id = post.id )
    context = { 'delete_com':  delete_com}
    return render(request, 'posts/delete_com.html', context)       