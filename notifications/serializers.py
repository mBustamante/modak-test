
from rest_framework import serializers

from notifications.exceptions import NotificationThrottleException
from notifications.models import Notification, NotificationType


class NotificationSerializer(serializers.ModelSerializer):

    type = serializers.CharField()

    def validate_type(self, type_name):
        try:
            return NotificationType.objects.get(name=type_name)
        except NotificationType.DoesNotExist:
            raise serializers.ValidationError('Invalid notification type name')

    def create(self, validated_data):
        try:
            notification = Notification.create_and_send(**validated_data)
        except NotificationThrottleException as e:
            raise serializers.ValidationError(e)
        return notification

    class Meta:
        model = Notification
        fields = (
            'user',
            'type',
        )
        extra_kwargs = {
            'user': {'required': True},
            'type': {'required': True},
        }
