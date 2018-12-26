from django.urls import path
from . import views
# from .views import CarPostDetailView, CarPostListView, FormAndListView
from .views import CarPostListView, CarPostDetailView, CarPostCreateView, CarPostDeleteView
from django.conf.urls import url

urlpatterns=[
    path('', views.home, name="blog-home"),
    path('search_post/', views.search, name="search_it"),
    path('car_posts/', CarPostListView.as_view(), name="blog-cars"),
    path('car_posts/new/', CarPostCreateView.as_view(), name="blog-create"),
    # path('car_posts/new/', views.carPostCreate, name='blog-create'),
    path('carposts_details/<int:pk>/', CarPostDetailView.as_view(), name="car_details"),
    path('<int:pk>/carposts_delete', CarPostDeleteView.as_view(), name="car_delete"),
    url(r'^api/', views.apiJson)
]