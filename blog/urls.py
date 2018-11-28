from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="blog-home"),
    path('car_posts/', views.post, name="blog-cars"),
]
