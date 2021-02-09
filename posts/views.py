from django.shortcuts import render




def index(request):
    return render(request, 'posts/index.html')

''' if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid:
            new_comment = form.save(commit=False)
            now_user = Profile.objects.get(user=request.user)
            new_comment.author = now_user
            new_comment.save()
            return HttpResponseRedirect(f'/profile/profile_detail/{pk}')'''
