from django.db import models

# Create your models here.

class DummyData(models.Model):
    number = models.IntegerField()
    id = models.UUIDField(primary_key=True, auto_created=True)
    creation = models.DateTimeField(auto_now_add=True, blank=True, null=True)