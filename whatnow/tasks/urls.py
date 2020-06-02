from django.urls import path, include

from tasks.views import index, tasks_view


app_name = 'tasks'

tasks_patterns = [
    path('', tasks_view.list, name='list'),
    path('<int:task_id>/', tasks_view.detail, name='detail'),
    path('new/', tasks_view.TaskCreateView.as_view(), name='create'),
]

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', include((tasks_patterns, 'tasks')))
]
