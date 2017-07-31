from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

    class Meta():
        db_tales = 'userinfo'

