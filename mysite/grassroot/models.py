from django.db import models

# Create your models here.
class Committee(models.Model):
	name = models.CharField()

class Senator(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    committee = models.ForeignKey(Committee)

class Bill(models.Model):
	name = models.CharField()
	num = models.IntegerField()
	committee = models.ForeignKey(Committee)
