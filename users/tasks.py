from celery import shared_task
from django.core.mail import send_mail
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