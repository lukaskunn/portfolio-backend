from django.urls import path
from content.views import getContent, saveNewContent

urlpatterns = [
    path('',  getContent),
    path('save-new-content',  saveNewContent),
]