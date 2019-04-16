import logging
 
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django_practice.celery import app
from django_practice.settings import EMAIL_HOST_USER

 
@app.task
def send_verification_email(user_id):
    email_to='bhardwajgaurav800@gmail.com'
    send_mail(
        'Verify your QuickPublisher account',
        'Follow this link to verify your account',
        'EMAIL_HOST_USER',
        [email_to],
        fail_silently=False,
    )
    print("runnnining mail")