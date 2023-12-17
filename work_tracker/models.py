from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    """the different work category the User is in"""
    name = models.CharField(max_length=25)

class WorkInstance(models.Model):
    """this is capturing the instance that User is in"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shift_start = models.DateTimeField(auto_now_add=True)
    shift_end = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)