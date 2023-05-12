from django.db import models
from django.contrib.auth.hashers import make_password
class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    hospital = models.DateTimeField(max_length=50, null=False)
    tel = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'users'