
from django.db import models

# Create your models here.
class Example(models.Model):
    title = models.CharField(max_length=255)