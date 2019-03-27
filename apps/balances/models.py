from django.db import models
from .. login_reg.models import User
# Create your models here.
class Transaction(models.Model):
    payor = models.ForeignKey(User, related_name="txns_paid")
    payee = models.ForeignKey(User, related_name="txns_to_be_paid")
    amount = models.FloatField()
    store = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)