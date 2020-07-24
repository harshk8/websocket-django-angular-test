from .models import Discussion, Post
from rest_framework import serializers
from account.serializers import UserSerializer 
from notification.models import Notification
from notification.serializers import NotificationSerializer
# from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'discussion', 'creator']
        read_only_fields = ['id', 'created_date', 'updated_date']

    def save(self):
        request = self.context['request']
        post = Post()
        post.content = self.data['content']
        post.discussion = Discussion.objects.get(
            id=self.data['discussion']
            )
        post.creator = request.user
        post.save()

        # notification = Notification.objects.add_action(
        #     request.user,
        #     post,
        #     post.discussion.creator
        #     )

        # serialize = NotificationSerializer(notification)
        # channel_layer = get_channel_layer()

        # group_name = 'notification_{}'.format(
        #     notification.receive_to.username)
        # async_to_sync(channel_layer.group_send)(
        #     group_name, {
        #         "type": "broadcast_notification_message",
        #         "message": serialize.data
        #     }
        # )

        return post


class DiscussionSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Discussion
        fields = ['id', 'title', 'created_date', 'creator', 'posts']
        read_only_fields = ['id', 'created_date', 'updated_date', 'creator']

    def save(self):
        request = self.context['request']
        discussion = Discussion()
        discussion.title = self.data['title']
        discussion.creator = request.user
        discussion.save()
        return discussion