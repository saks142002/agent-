from django.contrib import admin
from django.urls import path, include
from . import views
from .api_views import ChatAPIView, LoadDataView

urlpatterns = [
    path('', views.chat_view, name="chatAPI"),
    path('chat/', ChatAPIView.as_view(), name='chat-api'),
    path('load-data/', LoadDataView.as_view(), name="loadData"),
]