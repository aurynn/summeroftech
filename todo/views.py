# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from todo.models import Item

def index(self):

	# return HttpResponse("At the beginning..")
	template = loader.get_template("index.htmlt")
	c = Context({"todo": Item.objects.all()})

	return HttpResponse(template.render(c))