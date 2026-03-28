from django.db import models

class RequestCall(models.Model):

    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.mobile}"
    

class InternshipEnrollment(models.Model):
    program_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)  # New optional message field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.program_name}"