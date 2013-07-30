# Create your views here.

from django.http import HttpResponse
from todo.models import Item

def index(self):

	# return HttpResponse("At the beginning..")
	return HttpResponse(Item.objects.all())