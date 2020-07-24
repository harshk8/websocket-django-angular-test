from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Discussion, Post
from .serializers import DiscussionSerializer, PostSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

    def get_serializer_context(self):
        context = super(PostView, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def create(self, request):
        serialize = self.serializer_class(
            data=request.data,
            context={"request": self.request})
        serialize.is_valid(raise_exception=True)
        data = serialize.save()
        serialize = self.serializer_class(data)
        return Response(serialize.data)


class DiscussionView(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = (AllowAny,)

    def get_serializer_context(self):
        context = super(DiscussionView, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def create(self, request):
        serialize = self.serializer_class(
            data=request.data,
            context={"request": self.request})
        serialize.is_valid(raise_exception=True)
        data = serialize.save()
        serialize = self.serializer_class(data)
        return Response(serialize.data)