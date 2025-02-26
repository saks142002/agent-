from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .controllers.chat_view_controller import chat_view_controller
from .helpers.load_data import load_data
from django.shortcuts import redirect

@login_required
@csrf_protect
def chat_view(request):
    return chat_view_controller(request)


