from django.urls import path
from .views import *

urlpatterns = [
    path('home', index, name='index'),
    path('post/<int:id>/', index, name='post_detail'),
]