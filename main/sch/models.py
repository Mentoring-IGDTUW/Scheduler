from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager, Group

class Dicty(models.Model):
	name = models.CharField(max_length=50,default="")


	def __str__(self):
		return self.name

class KeyVal(models.Model):
	container = models.OneToOneField(Dicty,db_index=True)
	key = models.IntegerField(blank=False,default=0,db_index=True)
	value = models.CharField(max_length=4,default="",db_index=True)


	def __str__(self):
		return self.value
		


class Schedule(models.Model):
	day = models.CharField(max_length=8,default="")
	slots = models.CharField(max_length=8,default="")
	
	def __str__(self):
		return self.slots

class Batch(models.Model):
	group=models.OneToOneField(Group,null=True)
	stream = models.CharField(max_length=4,default="")
	year = models.IntegerField(blank=False,default=0)
	TT = models.OneToOneField(Schedule)
	dic = models.ManyToManyField(KeyVal,null=True)

	
	def __str__(self):
		return self.stream

class Person(User):
	Tid =models.CharField(max_length=6, default="", editable=False)
	#password =models.CharField(max_length=10, default="")
	#name = models.CharField(max_length=40)
	subject = models.CharField(max_length=6,default="")
	batch=models.ForeignKey(Batch,null=True)
	TT = models.OneToOneField(Schedule)
	objects=UserManager()
	dic = models.OneToOneField(KeyVal,null=True)


	def __str__(self):
		return self.name




