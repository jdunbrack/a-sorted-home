from django.db import models
from apps.login_reg.models import User

class Job(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    worker = models.ForeignKey(User, related_name="jobs", null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, related_name="created_jobs")
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name