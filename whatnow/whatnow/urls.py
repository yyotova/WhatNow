from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tasks/', include('tasks.urls')),
<<<<<<< HEAD
    path('register/', include('users.urls')),
=======
>>>>>>> 48c809c238835abc03aae81632bf357cdc91a7da
    path('admin/', admin.site.urls),
]
