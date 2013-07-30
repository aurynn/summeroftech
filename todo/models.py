from django.db import models
import datetime

# Create your models here.
class Item(models.Model):

	# id	    = models.
	content = models.CharField(max_length=200)
	created = models.DateTimeField()
	done = models.BooleanField()

	def __str__(self):
		return self.content