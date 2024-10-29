# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Students, Marks, Students_details

@receiver(post_save, sender=Students)
def student_created_updated(sender, instance, created, **kwargs):
    if created:
        print(f"New student created: {instance.name}")
    else:
        print(f"Student updated: {instance.name}")

@receiver(post_delete, sender=Students)
def student_deleted(sender, instance, **kwargs):
    print(f"Student deleted: {instance.name}")

@receiver(post_save, sender=Marks)
def marks_updated(sender, instance, **kwargs):
    print(f"Marks updated for student {instance.student.name}")

@receiver(post_save, sender=Students_details)
def student_details_updated(sender, instance, **kwargs):
    full_name = f"{instance.first_name} {instance.second_name}"
    print(f"Student details updated: {full_name}")

