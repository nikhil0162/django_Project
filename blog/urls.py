from django.urls import path
from . import views
# from .views import CarPostDetailView, CarPostListView, FormAndListView
from .views import CarPostCreateView, CarPostListView, CarPostDetailView

urlpatterns=[
    path('', views.home, name="blog-home"),
    path('search_post/', views.search, name="search_it"),
    # path('search_users/', views.search_users, name="search-users"),
    path('car_posts/', CarPostListView.as_view(), name="blog-cars"),
    path('car_posts/new/', CarPostCreateView.as_view(), name="blog-create"),
    # path('car_posts/', FormAndListView.as_view(), name="blog-cars"),
    path('carposts_details/<int:pk>/', CarPostDetailView.as_view(), name="car_details"),
]
