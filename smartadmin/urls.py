from django.urls import path
from . import views

urlpatterns = [

    path("", views.admin_login, name="admin_login"),
    path("admin_logout/", views.admin_logout, name="admin_logout"),

    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),

    path("admin_callbacks/", views.callback_list, name="callback_list"),
    path("admin_callback/<int:id>/contacted/", views.mark_contacted, name="mark_contacted"),

    # path("admin_chat/", views.chat_dashboard, name="chat_dashboard"),
    # path("admin_send/<int:user_id>/", views.send_message, name="send_message"),
]