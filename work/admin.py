from django.contrib import admin

from .models import Tasks, Rewards, Calendar, Account


class TasksAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'points', 'due_date', 'difficulty']

admin.site.register(Tasks, TasksAdmin)


class RewardsAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'points', 'priority', 'start_time', 'end_time']

admin.site.register(Rewards, RewardsAdmin)


class CalendarAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'start_time', 'end_time']

admin.site.register(Calendar, CalendarAdmin)


class AccountAdmin(admin.ModelAdmin):
    fields = ['name', 'photo', 'points']

admin.site.register(Account, AccountAdmin)
