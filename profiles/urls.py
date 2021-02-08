from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('account/', views.account, name='account'),
    path('profile_detail/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('upload/', views.image_upload_view),
]
