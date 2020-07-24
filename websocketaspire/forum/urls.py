from django.urls import path, include
from rest_framework import routers
from . import views as forum_views


router = routers.SimpleRouter()

router.register(r'post',
	forum_views.PostView, basename='post')

router.register(r'discussion',
	forum_views.DiscussionView, basename='discussion')

urlpatterns = [

] + router.urls