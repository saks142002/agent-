
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiV1/',include('chatbot.urls')),
    path('',include('users.urls'))
]
