from django.db import models
from django.urls import reverse
from hashids import Hashids
import datetime

class Url(models.Model):
    url = models.URLField(unique=True)
    short_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Urls'

    def __str__(self):
        return f"URL: {self.url} Code: {self.short_url}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.short_url:
            self.short_url = Hashids(min_length=6, alphabet='abcdefghijklmnopqrstuvwxyz1234567890').encode(self.pk)
            self.save()

