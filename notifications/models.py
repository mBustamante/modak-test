
import uuid
import logging
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.utils import timezone

from common.models import CustomBaseModel
from notifications.exceptions import (
    NotificationThrottleException,
    NotificationAlreadySentException
)

logger = logging.getLogger(__name__)


class NotificationType(CustomBaseModel):
    name = models.CharField(max_length=32, unique=True)
    max_user_requests = models.PositiveIntegerField(help_text='0 in unlimited')
    time_window = models.PositiveIntegerField(help_text='Time in seconds')
    template_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Notification(CustomBaseModel):

    PENDING_STATUS = 'PENDING'
    SENDING_STATUS = 'SENDING'
    SENT_STATUS = 'SENT'
    FAILED_STATUS = 'FAILED'

    STATUS_CHOICES = (
        (PENDING_STATUS, PENDING_STATUS),
        (SENDING_STATUS, SENDING_STATUS),
        (SENT_STATUS, SENT_STATUS),
        (FAILED_STATUS, FAILED_STATUS)
    )

    type = models.ForeignKey(
        'notifications.NotificationType',
        related_name='notifications',
        on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default=PENDING_STATUS,
    )
    data = models.TextField(default=None, null=True, blank=True)

    def send(self):
        if self.status in [Notification.SENDING_STATUS, Notification.SENT_STATUS]:
            raise NotificationAlreadySentException()

        # this must be async
        logger.info(f'Sendind notification of type {self.type} to user {self.user}')

    @classmethod
    def create_and_send(cls, type, user, data=None):

        key = f'th_{type.id}_{user.id}'
        now = timezone.now()
        last_valid_time = now - timezone.timedelta(seconds=type.time_window)

        notification = None
        with cache.lock(str(uuid.uuid4()), blocking_timeout=10):
            requests = cache.get(key, [])
            while requests and requests[-1] <= last_valid_time:
                requests.pop()
            if len(requests) >= type.max_user_requests:
                raise NotificationThrottleException(f'Notification rate of type {type} for user {user} exceeded.')

            requests.insert(0, now)
            cache.set(key, requests, type.time_window)

            notification = Notification.objects.create(
                type=type,
                user=user,
                data=data
            )

        notification.send()
        return notification
