from django.contrib import admin
from django.urls import path, include
from hammer_test import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('authorization/', include ('hammer_test.authorization.urls')),
    path('user/', include('hammer_test.user.urls')),
]
