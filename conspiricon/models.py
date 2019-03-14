from django.db import models

from django.conf import settings


class RSVP(models.Model):    
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    attending = models.BooleanField(default=True)

class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    presenter = models.TextField()
    title = models.TextField()
    file = models.FileField(upload_to=settings.FILE_UPLOAD_DIR, blank=True, null=True)
    url = models.URLField(blank=True)
    description = models.TextField()
