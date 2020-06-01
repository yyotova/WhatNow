from django.db import models


class UsersType(models.Model):
    user_type = models.CharField(max_length=250)


class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    user_type = models.ForeignKey(UsersType, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)


class UsersTask(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
