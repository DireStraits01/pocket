from django.urls import path
from . import views

urlpatterns = [
    path('messages/<int:id>/', views.message, name='messages')
]
