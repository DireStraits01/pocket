from django.shortcuts import render, redirect
from direct.models import Message
from profiles.models import Profile
from direct.forms import MessageForm
from django.http import HttpResponseRedirect

def message(request, id=0):
    message_form = MessageForm()
    req_user = Profile.objects.get(user=request.user)
    recipients = Profile.objects.get(id=id)
    messages = recipients.recipient.all()
    if request.method == 'POST':
        message_form = MessageForm(request.POST, request.FILES)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.sender = req_user
            message.recipient = recipients
            message.save()
            return redirect('messages', id=id)
    context = {'message_form':message_form,'req_user':req_user,
     'recipients':recipients, 'messages':messages}
    return render(request, 'direct/messages.html', context)
