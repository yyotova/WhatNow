from django.db import models
from django.utils import timezone


class Projects(models.Model):
    title = models.CharField(max_length=250)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Tasks(models.Model):
    title = models.CharField(max_length=250)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField()
    status = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Reviews(models.Model):
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review to {self.task_id.title}'


class Comments(models.Model):
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment of {self.task_id.title}'
