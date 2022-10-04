# import Django models
from django.db import models

class ChuckNorrysJokes(models.Model):
    '''chuck norrys jokes model'''
    icon_url = models.URLField(max_length=255, blank=True, default='')
    joke_id = models.CharField(max_length=255, blank=True, default='')
    url = models.URLField(max_length=255, blank=True, default='')
    value = models.TextField(blank=True)

    class Meta:
        db_table = 'chuck_norrys_jokes'

class OwnJokes(models.Model):
    '''own jokes model'''
    value = models.TextField(blank=True)

    class Meta:
        db_table = 'own_jokes'