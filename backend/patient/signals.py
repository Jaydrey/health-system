from django.db.models.signals import post_save
from django.dispatch import receiver


# emails
from django.core.mail import send_mail
from django.conf import settings

# models
from .models import Patient, Appointment

@receiver(post_save, sender=Patient)
def create_appointment(sender: Patient, instance: Patient, created: bool, **kwargs):
    if not created:
        return
    try:
        Appointment.objects.create(patient=instance)
    except Exception as e:
        print(e)




