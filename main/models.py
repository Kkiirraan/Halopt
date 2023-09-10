from django.db import models
from django.contrib.auth.models import User
from datetime import date  
    
# Create your models here.
class Syllabus(models.Model):
    subject_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.subject_name

class Subject(models.Model):
    sub_name = models.ForeignKey(Syllabus, blank=True, null=True, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100, blank=True)
    begin = models.CharField(max_length=100, blank=True)
    intermediate = models.CharField(max_length=100, blank=True)
    advance = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.sub_name.subject_name if self.sub_name else "sub_name"


class Topics(models.Model):
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100, blank=True)
  
    def __str__(self):
        return self.topic_name if self.topic_name else "syllabus_name"

    
    