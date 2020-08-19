from django.db.models.signals import post_save
from django.dispatch import receiver
from timeapp.models import *
#from timeapp.tasks import save_avgspeed_distance_to_models


# @receiver(post_save, sender=Post)
# def save_avgspeed_distance_to_model(sender, **kwargs):
#     save_avgspeed_distance_to_models.delay()