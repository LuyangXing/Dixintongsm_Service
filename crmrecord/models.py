# coding=utf-8
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class RecordList(models.Model):
    ServiceCode = models.AutoField(primary_key=True)
    OrderNo = models.CharField(max_length=20)

    Authors = models.CharField(max_length=10)
    ProblemSummary = models.CharField(max_length=50)
    ProblemDescription = models.TextField()
    DateTime = models.DateTimeField()

    EmergencyTreatment = models.IntegerField(max_length=1)
    CallProcessing = models.IntegerField(max_length=1)
    CustomerName = models.CharField(max_length=50, blank=True)
    Products = models.CharField(max_length=50, blank=True)

    State = models.IntegerField(max_length=1)

    Head = models.CharField(max_length=10)
    ProcessResultsSummary = models.CharField(max_length=50)
    ProcessResultsDescription = models.TextField()
    DateTime2 = models.DateTimeField()

    def display_mySafeField(self):
        return mark_safe(self.ProblemDescription) #{{instance.display_mySafeField}}

    def display_mySafeField2(self):
        return mark_safe(self.ProcessResultsDescription) #{{instance.display_mySafeField}}