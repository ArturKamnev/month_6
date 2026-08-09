from celery import shared_task
from django.core.mail import send_mail
from .models import CustomUser
from django.utils import timezone
import random
import string

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_otp_mail(email, code):
    send_mail(subject="Your OTP code", message=f"{code}", from_email='SHOP_API', recipient_list=[email],)

@shared_task
def send_report_mail():
    send_mail(subject="REPORT", message="something_important67", from_email='SHOP_API', recipient_list=["kamartur778@gmail.com"],)

# 1 таск генирирует код
@shared_task
def generate_code():
    code = ''.join(random.choices(string.digits, k=6))
    return code

@shared_task 
def send_birthday_emails():
    today = timezone.localdate()
    users = CustomUser.objects.filter(birthdate__month=today.month, birthdate__day=today.day)
    emails = [user.email for user in users]
    send_mail(subject="Happy birthday!", message="Our team want to congratulate you with your birthday!", from_email="SHOP_API", recipient_list=emails,)