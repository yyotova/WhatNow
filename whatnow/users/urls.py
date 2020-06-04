from django.urls import path
from users.views import register, promote

urlpatterns = [
    path('', promote.list, name='user-list'),
    path('<int:user_id>/', promote.promote, name='promote'),
    path('register', register, name='register')
]
