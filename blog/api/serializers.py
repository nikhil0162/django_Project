from rest_framework import serializers
from blog.models import CarPost


class CarSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(
		view_name = 'blog-api:detail',
		lookup_field = 'pk',
		)
	class Meta:
		model = CarPost
		fields = ('url', 'id', 'model_name', 'image', 'launched_date')


class CarDetailSerializer(serializers.HyperlinkedModelSerializer):
	delete_url = serializers.HyperlinkedIdentityField(
		view_name = 'blog-api:delete',
		lookup_field = 'pk',
		)
	update_url = serializers.HyperlinkedIdentityField(
		view_name = 'blog-api:update',
		lookup_field = 'pk',
		)
	class Meta:
		model = CarPost
		fields = ('update_url', 'delete_url', 'id', 'company_name', 'model_name', 'image', 'launched_date')


class CarDeleteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CarPost
		fields = ('id', 'company_name', 'model_name', 'image', 'launched_date')


class CarCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarPost
		fields = ('company_name', 'model_name', 'launched_date')










"""

from blog.api.serializers import CarDeleteSerializer, CarCreateUpdateSerializer, CarSerializer, CarDetailSerializer
from blog.models import CarPost


obj = CarPost.objects.get(id=14)
data = {
	"company_name": "Lamborghini",
    "model_name": "Land Cruiser",
    "image": "http://localhost:8000/media/carpost_pics/15667.jpg",
    "launched_date": "2019-01-10"
}

new_item = CarCreateUpdateSerializer(obj, data=data)


"""