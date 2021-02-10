from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('profile/<int:pk>/', views.profiles, name='profile'),
    path('upload/', views.image_upload_view),
 
]
