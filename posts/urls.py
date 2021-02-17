from django.urls import path
from . import views
from .feeds import LatestPostsFeed 

urlpatterns = [

  path('feed/', LatestPostsFeed(), name='post_feed'),
  path('comments/<int:id>/', views.comments, name='comments'),
  path('delete_post/<int:id>/', views.delete_post, name='delete_post'), 
  path('delete_com/<int:id>/', views.delete_com, name='delete_com'), 

    
]