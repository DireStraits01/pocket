from django.urls import path
from . import views 


urlpatterns = [

    path('', views.list_posts, name='list_posts'),
    path('profiles/', views.list_users, name='list_users'),
    path('profile/<int:id>/detail/', views.profileDetailView,  name='profile'),
    path('profile/change/<int:id>/', views.change_avatar, name='change_avatar'),
  
   
]
