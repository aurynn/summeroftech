from django.db import models
import datetime

# Create your models here.
class Item(models.Model):

	# id is auto-generated
	content = models.CharField(max_length=200)
	created = models.DateTimeField()
	done = models.BooleanField()

	def __init__(self, content):
		self.content = content
		self.created = datetime.datetime.now()
		self.done = False