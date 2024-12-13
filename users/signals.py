from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    """Send welcome email to new users"""
    if created:
        subject = f'Welcome to FreelanceHaat!'
        message = (
            f'Hi {instance.get_full_name() or instance.email},\n\n'
            f'Welcome to FreelanceHaat! We\'re excited to have you join us as a {instance.user_type}.\n\n'
            f'Get started by completing your profile and exploring the platform.\n\n'
            f'Best regards,\nThe FreelanceHaat Team'
        )
        send_mail(
            subject,
            message,
            'noreply@freelancehaat.com',
            [instance.email],
            fail_silently=True,
        )