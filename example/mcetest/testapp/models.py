from django.db import models
from tinymce.models import HTMLField


class MCETest(models.Model):
    text = HTMLField()

