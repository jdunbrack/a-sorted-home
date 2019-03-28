from django.db import models
from apps.login_reg.models import User
from apps.user_dash.models import Home

class Task(models.Model):
    name = models.CharField(max_length=100)
    worker = models.ForeignKey(User, related_name="tasks", null=True, on_delete=models.SET_NULL)
    home = models.ForeignKey(Home, related_name="all_tasks")
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name