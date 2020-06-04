from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users.views import profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
