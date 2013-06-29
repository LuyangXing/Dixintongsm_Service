from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class RecordList(models.Model):
    cddid=models.CharField(max_length=20)
    cwwid=models.CharField(max_length=50)
    cdatetime=models.DateTimeField()
    cstate=models.CharField(max_length=20)
    ccharger=models.CharField(max_length=20)
    cdemand=models.CharField(max_length=50)
    cnotes=models.TextField()

    def display_mySafeField(self):
        return mark_safe(self.cnotes) #{{instance.display_mySafeField}}
