from django.urls import path
from . import views
# from .views import CarPostDetailView, CarPostListView, FormAndListView
from .views import CarPostListView, CarPostDetailView, CarPostCreateView, CarPostDeleteView, CarPostUpdateView
from django.conf.urls import url
from .views import send_mail_by_me
# from django.contrib import admin
# from django.contrib.auth import views as auth_views


urlpatterns=[
	# path('admin/', auth_views.admin, name="admin"),
    path('', views.home, name="blog-home"),
    path('mail_me/', send_mail_by_me, name="sending_mail"),
    path('search_post/', views.search, name="search_it"),
    path('car_posts/', CarPostListView.as_view(), name="blog-cars"),
    path('car_posts/new/', CarPostCreateView.as_view(), name="blog-create"),
    # path('car_posts/new/', views.carPostCreate, name='blog-create'),
    path('carposts_details/<int:pk>/', CarPostDetailView.as_view(), name="car_details"),
    path('<int:pk>/carposts_delete/', CarPostDeleteView.as_view(), name="car_delete"),
    path('<int:pk>/carpost_update/', CarPostUpdateView.as_view(), name="car_update"),
    url(r'^api/', views.apiJson)
]