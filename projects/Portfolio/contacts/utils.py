# utils.py or any helper file
from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(subject, message, recipient=None):
    """
    Sends an email notification to the admin (or a specific recipient).
    """
    if recipient is None:
        recipient = settings.EMAIL_HOST_USER  # default to admin email

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,   # sender
        [recipient],                # recipient list
        fail_silently=False,
    )
