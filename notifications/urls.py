from django.urls import path
from notifications.views import ShowNotification, DeleteNotification

urlpatterns = [
    path('', ShowNotification, name='show-notification'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification'),


]
