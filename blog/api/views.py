from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from .serializers import CarSerializer, CarDeleteSerializer, CarDetailSerializer, CarCreateUpdateSerializer
from blog.models import CarPost
from rest_framework.permissions import (
								IsAuthenticatedOrReadOnly, 
								IsAdminUser,
								AllowAny,
								)  
from .permissions import IsOwnerOrReadOnly


class CarListViewSet(ListAPIView):
	queryset = CarPost.objects.all()
	serializer_class = CarSerializer
	# permission_classes = [IsAuthenticatedOrReadOnly]
	def perform_create(self, serializer):
		serializer.save(posted_by=self.request.user)


class CarDetailViewSet(RetrieveAPIView):
	queryset = CarPost.objects.all()
	serializer_class = CarDetailSerializer
	permission_classes = [AllowAny]


class CarDeleteViewSet(RetrieveDestroyAPIView):
	queryset = CarPost.objects.all()
	serializer_class = CarDeleteSerializer
	permission_classes = [IsOwnerOrReadOnly]


class CarCreateViewSet(CreateAPIView):
	queryset = CarPost.objects.all()
	serializer_class = CarCreateUpdateSerializer
	permission_classes = [AllowAny]


class CarUpdateViewSet(RetrieveUpdateAPIView):
	queryset = CarPost.objects.all()
	serializer_class = CarCreateUpdateSerializer
	permission_classes = [IsOwnerOrReadOnly]
