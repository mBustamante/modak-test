
from rest_framework import viewsets, mixins

from notifications.serializers import NotificationSerializer


class NotificationViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    permission_classes = []
    serializer_class = NotificationSerializer

    # def get_throttles(self):
    #     throttles = self.throttle_classes
    #     if self.action in ['create']:
    #         throttles = [CreateNotificationThrottle]
    #     return [throttle() for throttle in throttles]
