from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Notification
from .serializers import NotificationSerializer


# @receiver(post_save, sender=Notification)
# def new_notification(sender, instance, created, **kwargs):

#     if created:
#         serailize = NotificationSerializer(instance)
#         channel_layer = get_channel_layer()

#         group_name = 'notification_{}'.format(
#             instance.receive_to.username)
    
#         async_to_sync(channel_layer.group_send)(
#             group_name, {
#                 "type": "broadcast_notification_message",
#                 "message": serailize.data
#             }
#         )


@receiver(post_save, sender=Notification)
def notification_post_save(sender, instance, created, **kwargs):
    serailize = NotificationSerializer(instance)

    channel_layer = get_channel_layer()

    group_name = 'notification_{}'.format(
        instance.receive_to.username)
    async_to_sync(channel_layer.group_send)(
        group_name, {
            "type": "broadcast_notification_message",
            "message": serailize.data
        }
    )