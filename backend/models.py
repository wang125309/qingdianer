from django.db import models

class products(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=128)
    URL = models.URLField()
    file = models.CharField(max_length=256)
