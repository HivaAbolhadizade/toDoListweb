from django.db import models

# Create your models here.
class ListObject(models.Model):
    text = models.TextField('Object')