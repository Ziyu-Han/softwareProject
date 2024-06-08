from django.db import models

# Create your models here.


class UserInfo(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20)
    userpwd = models.CharField(max_length=20)
