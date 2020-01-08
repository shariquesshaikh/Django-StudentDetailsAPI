from django.urls import path
from studentApp.views import studentView

urlpatterns = [
    path('students/', studentView.as_view(),name='students'),
]