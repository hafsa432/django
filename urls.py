
from django.contrib import admin
from django.urls import path
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
    path('aboutus/', views.about),
    path('userinput/', views.userinput),
    path('viewdata/', views.viewdata, name='viewdata'),
]
