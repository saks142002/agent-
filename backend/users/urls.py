from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from . import views
from django.http import JsonResponse

from .api_views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('health/', csrf_exempt(lambda request: JsonResponse({"status": "Server is running"}, status=200)), name='health_check'),

]