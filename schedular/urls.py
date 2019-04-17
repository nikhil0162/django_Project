from django.urls import path, include
from . import views
from .views import EmailView

app_name='schedular-app'

urlpatterns=[
	# path('', views.index, name="schedular-index")
	path('', EmailView.as_view(), name='email-form'),
]