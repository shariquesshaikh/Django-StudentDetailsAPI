# Super User details when I created this file
# name : not_a_smartUser
# password: 123123123

from django.contrib import admin
from django.urls import path,include
from studentDetailsAPI.views import index,Message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studentApp.urls')),
]
