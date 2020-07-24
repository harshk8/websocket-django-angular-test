from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Notification
from .serializers import NotificationSerializer


class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    # def get_serializer_context(self):
    #     context = super(NotificationView, self).get_serializer_context()
    #     context.update({"request": self.request})
    #     return context
    def get_queryset(self):
    	return self.queryset.filter(
    		receive_to=self.request.user)