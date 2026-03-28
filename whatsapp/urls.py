from django.urls import path
from . import views

urlpatterns = [
    path("webhook/", views.whatsapp_webhook, name="whatsapp_webhook"),
    path("chat/", views.chat_dashboard, name="chat_dashboard"),
    path("send/<int:user_id>/", views.send_message, name="send_message"),
]