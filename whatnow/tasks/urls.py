from django.urls import path, include

<<<<<<< HEAD
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
=======
from tasks.views import index, tasks, projects, reviews, comments

app_name = 'tasks'


tasks_patterns = [
    path('', tasks.list, name='list'),
    path('<int:task_id>/', tasks.detail, name='detail'),
    path('new/', tasks.TaskCreateView.as_view(), name='create'),
]


projects_patterns = [
    path('', projects.list, name='list'),
    path('<int:project_id>/', projects.detail, name='detail'),
    path('new/', projects.ProjectCreateView.as_view(), name='create'),
]


reviews_patterns = [
    path('', reviews.list, name='list'),
    path('<int:review_id>/', reviews.detail, name='detail'),
    path('new/', reviews.ReviewCreateView.as_view(), name='create'),
]


urlpatterns = [
    path('', index, name='index'),
    path('tasks/', include((tasks_patterns, 'tasks'))),
    path('projects/', include((projects_patterns, 'projects'))),
    path('reviews/', include((reviews_patterns, 'reviews')))
>>>>>>> 48c809c238835abc03aae81632bf357cdc91a7da
]
