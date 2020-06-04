from tasks.views import index, tasks, projects, reviews, comments, tasks_view
from django.urls import path, include

app_name = 'tasks'


tasks_patterns = [
    path('', tasks_view.list, name='list'),
    path('<int:task_id>/', tasks.detail, name='detail'),
    path('<int:task_id>/for_review', tasks.task_sent_review, name='sent-review'),
    path('close/<int:task_id>/', tasks.task_close, name='close'),
    path('<int:task_id>/asign', tasks.task_asign, name='asign'),
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
    path('new/<int:review_id>/', reviews.create, name='create'),
]
comments_patterns = [
    path('new/<int:task_id>', comments.CommentCreate.as_view(), name='create'),
]

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', include((tasks_patterns, 'tasks'))),
    path('projects/', include((projects_patterns, 'projects'))),
    path('reviews/', include((reviews_patterns, 'reviews'))),
    path('comments/', include((comments_patterns, 'comments')))

]
