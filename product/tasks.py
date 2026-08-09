from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_review_report(email, product, stars, text):
    send_mail(subject="REVIEW NOTIFICATION", message=f"Your {product} got and review, stars: {stars}, text: {text}", from_email="SHOP_API", recipient_list=[email],)