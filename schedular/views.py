from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailSendForm
from django.views.generic import CreateView
# Create your views here.



class EmailView(CreateView):
	form_class = EmailSendForm
	template_name = 'schedular/index.html'
# def index(request):
# 	if request.method == 'POST':
# 		form = 
# 	return render(request, 'schedular/index.html')	