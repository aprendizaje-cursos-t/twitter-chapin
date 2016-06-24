from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='tweet')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text
