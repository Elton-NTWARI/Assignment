from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    publi_date = models.DateTimeField('Publication Date')