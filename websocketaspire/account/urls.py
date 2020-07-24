from django.urls import path, include
from rest_framework import routers
from . import views as account_views

router = routers.SimpleRouter()

router.register(r'profile',
	account_views.UserProfileViewset, basename='profile')

urlpatterns = [

	path('', include((router.urls, 'account'))),

	path('register/',
		account_views.SignUpAPIView.as_view(), name='register'),
	path('login/',
		account_views.LoginAPIView.as_view(), name='login'),
	path('change-password/',
		account_views.ChangePasswordAPIView.as_view(),
		name='change_password'),
	path('logout/',
		account_views.LogoutAPIView.as_view(), name='logout'),

] + router.urls