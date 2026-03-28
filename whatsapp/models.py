from django.db import models


class ChatUser(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Message(models.Model):
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    message = models.TextField()
    direction = models.CharField(max_length=10)  # incoming/outgoing
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.phone} - {self.direction}"