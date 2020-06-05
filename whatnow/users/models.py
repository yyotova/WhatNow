from django.db import models
from django.contrib.auth.models import User


class UsersType(models.Model):
    user_type = models.CharField(max_length=250)

    def __str__(self):
        return self.user_type


class Users(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UsersType, default=1, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username


class UsersTasks(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_id = models.ForeignKey('tasks.Tasks', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    current_location = models.CharField(null=True, max_length=150)
    technologies = models.TextField(null=True)
    skills = models.TextField(null=True)
    interests = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
