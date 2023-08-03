from django.urls import path
from hammer_test.authorization import views

urlpatterns = [
    path('', views.authorization, name='authorization'),
    path('enter_code/', views.enter_code, name='enter_code')
]