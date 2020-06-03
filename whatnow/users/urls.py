from django.urls import path
from users.views import register, profile


urlpatterns = [
    path('', profile, name='profile'),
    path('', register, name='register'),
]
