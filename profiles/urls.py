from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('profile/<int:pk>/', views.profiles, name='profile'),
    path('profile/change/<int:id>/', views.change_avatar, name='change_avatar'),

]
