# import Django models
from django.db import models

class MyJokes(models.Model):
    '''My jokes model'''
    value = models.TextField(blank=True)

    class Meta:
        db_table = 'my_jokes'