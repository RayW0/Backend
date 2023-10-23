from django.db import models


class ChatLog(models.Model):
    message = models.CharField(max_length=255, null=False, blank=True)
    date_of_creation = models.CharField(max_length=200, null=False, blank=False)
