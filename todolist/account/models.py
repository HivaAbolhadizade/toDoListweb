from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField('Email', max_length=100, unique=True)
    password = models.CharField('Password', max_length=100)

    def __str__(self):
        return self.email