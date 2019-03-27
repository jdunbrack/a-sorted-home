from django.db import models
import datetime
import re
from .. user_dash.models import Home
# from .. user_dash.models import Home

PW_REGEX = re.compile(r'(?=.*[0-9]+)(?=.*[A-Z]+)(?=.*[a-z]+)')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should contain at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should contain at least 2 characters."
        if PW_REGEX.match(postData['pw-entry']) == None:
            errors["password"] = "Password must contain at least 1 lowercase, 1 uppercase, and 1 number."
        if len(postData['pw-entry']) < 8:
            errors["password"] = "Password should be 8 or more characters in length."
        
        # thirteen_years = datetime.timedelta(days=4748)
        # birthday = datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d").date()
        # if (datetime.date.today() - birthday) < thirteen_years:
        #     errors["age"] = "You must be 13 years old or older to register."

        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    payment_url = models.CharField(max_length=255, blank=True)
    profile_pic = models.TextField(default="")
    my_home = models.ForeignKey(Home, related_name="owner", null=True, on_delete=models.SET_NULL)
    home = models.ForeignKey(Home, related_name="members", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email

class JoinedDate(models.Model):
    member = models.ForeignKey(User, related_name="joined_date")
    home = models.ForeignKey(Home, related_name="joined_dates")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)