from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum_page, name='forum_page'),
]