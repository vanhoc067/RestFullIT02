from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class ModelBase(models.Model):
    active = models.BooleanField(default= True)
    created_date = models.DateField(auto_now_add=True)
    Update_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(ModelBase):
    name = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.name


# Create your models here.
