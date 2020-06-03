from django.contrib import admin

from users.models import *


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'get_user_type', 'phone')

    def get_user_type(self, obj):
        return obj.user_type.user_type

    get_user_type.short_description = 'User type'


@admin.register(UsersType)
class UsersTypeAdmin(admin.ModelAdmin):
    list_display = ('user_type',)


@admin.register(UsersTasks)
class UsersTasksAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_task')

    def get_user(self, obj):
        return obj.user_id.username

    def get_task(self, obj):
        return obj.task_id.title

    get_user.short_description = 'User'
    get_task.short_description = 'task'


admin.site.register(Profile)