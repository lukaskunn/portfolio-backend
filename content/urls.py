from django.urls import path
from content.views import GetContent

urlpatterns = [
    path('',  GetContent.as_view()),
]