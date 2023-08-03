from django.urls import path
from hammer_test.user import views

urlpatterns = [
    path('<str:phone>/', views.user_profile, name='user_profile'),
]