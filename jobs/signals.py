from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Proposal

@receiver(post_save, sender=Proposal)
def notify_proposal_status(sender, instance, created, **kwargs):
    """Notify users about proposal status changes"""
    if created:
        # Notify client about new proposal
        subject = f'New proposal for "{instance.job.title}"'
        message = (
            f'A new proposal has been submitted by {instance.freelancer.get_full_name() or instance.freelancer.email}\n'
            f'Bid Amount: ${instance.bid_amount}\n\n'
            f'View the proposal details on FreelanceHaat.'
        )
        send_mail(
            subject,
            message,
            'noreply@freelancehaat.com',
            [instance.job.client.email],
            fail_silently=True,
        )
    elif instance.accepted:
        # Notify freelancer about accepted proposal
        subject = 'Your proposal has been accepted!'
        message = (
            f'Congratulations! Your proposal for "{instance.job.title}" has been accepted.\n\n'
            f'Please contact the client to discuss the next steps.'
        )
        send_mail(
            subject,
            message,
            'noreply@freelancehaat.com',
            [instance.freelancer.email],
            fail_silently=True,
        )