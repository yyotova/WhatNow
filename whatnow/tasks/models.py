from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=250)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()


class Task(models.Model):
    title = models.CharField(max_length=250)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField()
    status = models.CharField(max_length=250)
    description = models.TextField()


class Review(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
