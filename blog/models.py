from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_bleach.models import BleachField


# Create your models here.
class CarPost(models.Model):
	company_name = BleachField()
	model_name = BleachField()
	image = models.ImageField(upload_to='carpost_pics/', null=True, blank=True)
	launched_date = models.DateTimeField(blank=True, null=True)
	date_posted = models.DateTimeField(default=timezone.now)
	gender = models.BooleanField(default=False)
	# description = RichTextField(blank=True, null=True)
	description = RichTextUploadingField(blank=True, null=True)
	company_contact_no = models.IntegerField(blank=True, null=True) 
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.company_name	

	def get_absolute_url(self):
		return reverse('car_details', kwargs={'pk': self.pk})