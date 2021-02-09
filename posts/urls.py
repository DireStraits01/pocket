from django.urls import path
from . import views
from .feeds import LatestPostsFeed 

urlpatterns = [
 
  path('feed/', LatestPostsFeed(), name='post_feed'),
  path('comments/<int:id>/', views.comments, name='comments'),
    
]