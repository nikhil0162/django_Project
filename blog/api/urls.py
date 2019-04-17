from django.urls import path, include
from rest_framework import routers
from .views import CarListViewSet, CarDetailViewSet, CarDeleteViewSet, CarCreateViewSet, CarUpdateViewSet
from . import views
from blog.models import CarPost


# router = routers.DefaultRouter()
# router.register('carpost', CarListViewSet)

app_name = 'blog-api'
urlpatterns = [
	# path('', include(router.urls)),
	path('', CarListViewSet.as_view(), name='list'),
	# path('create/', CarCreateViewSet.as_view(), name='create'),
	path('<int:pk>/', CarDetailViewSet.as_view(), name='detail'),
	path('<int:pk>/delete/', CarDeleteViewSet.as_view(), name='delete'),
	path('<int:pk>/update/', CarUpdateViewSet.as_view(), name='update'),
]