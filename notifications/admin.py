
from django.contrib import admin

from notifications.models import Notification, NotificationType


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'created')


@admin.register(NotificationType)
class NotificationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_user_requests', 'time_window')
