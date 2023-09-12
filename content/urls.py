from django.urls import path
from content.views import getContent

urlpatterns = [
    path('',  getContent),
]