# Create your views here.

from django.http import HttpResponse

def index(self):

	return HttpResponse("At the beginning..")