
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notifications.views import NotificationViewSet

router = DefaultRouter()

router.register(
    r'notifications',
    NotificationViewSet,
    basename='dashboard_school',
)

urlpatterns = [
    path('', include(router.urls)),
]
