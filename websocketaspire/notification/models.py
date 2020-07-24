from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
from forum.models import TimeStampModel


class NotificationQuerySet(models.QuerySet):
    pass


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQuerySet(self.model, using=self._db)

    def add_action(self, user, content_object, receive_to=None):
        similar_actions = Notification.objects.filter(
            user=user,
            # action=action,
            receive_to=receive_to if receive_to else None,
            created_date__gte=(timezone.now() - datetime.timedelta(seconds=60)),
        )

        if content_object:
            content_type = ContentType.objects.get_for_model(content_object)
            similar_actions = similar_actions.filter(
                content_type=content_type,
                object_id=content_object.id,
            )

        if not similar_actions:
            notify_content = f'{content_object.creator.username} created new post {content_object.content} under discussion {content_object.discussion.title}'
            notification = Notification(
                user=user,
                content_object=content_object,
                notify_content=notify_content,
                receive_to=receive_to
            )
            notification.save()

        return None


class Notification(TimeStampModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        blank=True,
        null=False,
        related_name='notifications',
        verbose_name='user',
    )
    receive_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        blank=True,
        null=True,
        related_name='received_notifications',
        verbose_name='Received to',
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='content type',
    )
    object_id = models.IntegerField(
        'object id',
        null=False,
        blank=False,
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    is_seen =models.BooleanField(default=False)
    notify_content = models.TextField(null=True, blank=True)

    objects = NotificationManager()

    class Meta:
        db_table = 'notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_date', ]