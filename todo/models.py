from django.db import models

# Create your models here.
class Item(models.Model):

	# id is auto-generated
	content = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	done = models.BooleanField()
