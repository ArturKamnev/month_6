from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_otp_mail(email, code):
    send_mail(subject="Your OTP code", message=f"{code}", from_email='SHOP_API', recipient_list=[email],)