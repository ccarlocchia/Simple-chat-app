from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    
    def get_localtime(utctime):
        utc = utctime.replace(tzinfo=pytz.UTC)
        localtz = utc.astimezone(timezone.get_current_timezone())
        return localtz


    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=get_localtime(datetime.now()), blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)


    