from django.db import models


class Entry(models.Model):
    start = models.DateField()
    end = models.DateField()
    task = models.ForeignKey('Task')

    class Meta:
        ordering = ['-start']


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['name']
