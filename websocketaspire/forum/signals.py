from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Post, Discussion
from notification.models import Notification


@receiver(post_save, sender=Post)
def new_post(sender, instance, created, **kwargs):

    if created:
        Notification.objects.add_action(
            instance.creator,
            instance,
            instance.discussion.creator,
        )
