from rest_framework import serializers 
from account.serializers import UserSerializer
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    subject = serializers.SerializerMethodField()
    context = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id',
            'user',
            'is_seen',
            'subject',
            'context',
            'created_date',
        )
        read_only_fields = ['id', 'created_date', 'updated_date', 'creator']

    def get_subject(self, obj):
        model = obj.content_object.__class__.__name__.lower()

        return {
            'type': model,
            'id': obj.content_object.id if obj.content_object else 0,
            'title': str(obj.content_object),
            'context_data': obj.notify_content
            }

    def get_context(self, obj):
        model = obj.content_object.__class__.__name__.lower()

        return {
            'type': model,
            'id': obj.content_object.discussion.id if obj.content_object.discussion else 0,
            'title': obj.content_object.discussion.title if obj.content_object.discussion else 'Discussion Deleted',
        }
