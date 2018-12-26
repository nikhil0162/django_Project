from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class CarPost(models.Model):
	company_name = models.CharField(max_length=50)
	model_name = models.CharField(max_length=40)
	image = models.ImageField(upload_to='carpost_pics/', null=True, blank=True)
	launched_date = models.DateTimeField(blank=True, null=True)
	date_posted = models.DateTimeField(default=timezone.now)
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.company_name	

	def get_absolute_url(self):
		return reverse('car_details', kwargs={'pk': self.pk})