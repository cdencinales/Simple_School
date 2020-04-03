from django.db import models
from django.conf import settings

'''user resource model (dummy)'''
class Journal(models.Model):
    header = models.CharField(max_length=255, null=False, blank=True)
    body = models.TextField(null=False, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, verbose_name='Post Date')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    slug = models.SlugField(blank=True, unique=True)