from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Message

@login_required
def inbox(request):
    messages_received = Message.objects.filter(receiver=request.user)

    return render(request, 'messenger/inbox.html', {
        'messages': messages_received
    })


@login_required
def send_message(request):
    users = User.objects.exclude(id=request.user.id)
    receiver_id = request.GET.get('to')

    if request.method == 'POST':
        receiver = User.objects.get(id=request.POST['receiver'])
        content = request.POST['content']
        

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content,
            
        )

        messages.success(request, '📨 Mensaje enviado correctamente')
        return redirect('messenger:inbox')

    return render(request, 'messenger/send_message.html', {
        'users': users,
        'receiver_id': receiver_id
    })
    
@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id, receiver=request.user)
    message.delete()
    messages.success(request, '🗑️ Mensaje eliminado')
    return redirect('messenger:inbox')
