from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('register/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('', include('tasks.urls')),
]
