from django.contrib import admin

from tasks.models import *


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end', 'description')


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_project', 'date_start', 'date_end', 'status', 'description')

    def get_project(self, obj):
        return obj.project_id.title
    get_project.short_description = 'Project'


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('get_task', 'get_user', 'review', 'date')

    def get_task(self, obj):
        return obj.task_id.title

    def get_user(self, obj):
        return obj.user_id.username

    get_user.short_description = 'User'
    get_task.short_description = 'task'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'get_task', 'get_user')

    def get_task(self, obj):
        return obj.task_id.title

    def get_user(self, obj):
        return obj.user_id.username

    get_user.short_description = 'User'
    get_task.short_description = 'task'
