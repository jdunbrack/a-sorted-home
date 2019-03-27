from django.db import models
import random
import string
# Create your models here.
def create_join_id():
    join_id = ""
    choice_set = string.ascii_letters + string.digits
    for i in range(6):
        join_id += random.choice(choice_set)
    return join_id

class Home(models.Model):
    name = models.CharField(max_length=100)
    join_id = models.CharField(max_length=6, default=create_join_id)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
