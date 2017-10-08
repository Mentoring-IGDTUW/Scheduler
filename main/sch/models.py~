from django.db import models
from django.utils import timezone

class Schedule(models.Model):
	day = models.CharField(max_length=8)
	slots = models.CharField(max_length=8)
	
	def __str__(self):
		return self.slots

class Person(models.Model):
	Tid =models.CharField(max_length=6, default="", editable=False)
	password =models.CharField(max_length=10, default="")
	name = models.CharField(max_length=40)
	subject = models.CharField(max_length=6)
	TT = models.OneToOneField(Schedule)
	
	def __str__(self):
		return self.name

class Batch:
	stream = models.CharField(max_length=4)
	year = models.IntegerField(blank=False)
	TT = models.OneToOneField(Schedule)
	
	def __str__(self):
		return self.stream


