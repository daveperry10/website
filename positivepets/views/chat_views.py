from positivepets.models import Pet, Chat, CustomUser, Mail
from datetime import datetime
from django.shortcuts import render
from .colors import color_map

import time
def chat_message_create(request):
    model = Chat
    fields = ['comment']
    if request.method == 'POST':
        msg = Chat()
        msg.timestamp = datetime.now()
        msg.user = request.user
        msg.comment = request.POST['textbox']
        msg.save()
    comment_list = Chat.objects.all().order_by('-timestamp')[:15] #no neg indexing

    now = datetime.now()

    context = {'comment_list': comment_list,'user':request.user, 'now': now, 'color':request.user.color}
    context['button_text_color'] = color_map[request.user.color.lower()]['button_text_color']
    return render(request, 'positivepets/chat_form.html', context)
