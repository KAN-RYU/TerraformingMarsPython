from django.db import models

# Create your models here.
class TM(models.Model):
    content = models.CharField(max_length=1000, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
