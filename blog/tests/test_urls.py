from django.urls import resolve, reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from blog.views import CarPostListView
from mixer.backend.django import mixer
import pytest
from django import test

class TestUrls(test.TestCase):

	def test_blog_home(self):
		response = self.client.get(reverse('blog-home'))
		self.assertEqual(response.status_code, 200)


# @pytest.mark.django_db
# class TestViews:

# 	def test_event_detail(self):
# 		path = reverse('blog-cars')
# 		request = RequestFactory().get(path)
# 		request.user = mixer.blend(User)

# 		response = CarPostListView(RequestFactory)
# 		assert response.status_code == 200
