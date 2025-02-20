# signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginHistory
from django.utils import timezone

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    LoginHistory.objects.create(user=user, login_time=timezone.now(), ip_address=ip_address)
