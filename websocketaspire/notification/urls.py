from django.urls import path, include
from rest_framework import routers
from . import views as notification_views


router = routers.SimpleRouter()

router.register(r'notification',
	notification_views.NotificationView, basename='notification')

urlpatterns = [
	# path('',  notification_views.NotificationView.as_view(), name='notification')
] + router.urls 