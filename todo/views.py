# Create your views here.
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from todo.models import Item

def index(request):

	# return HttpResponse("At the beginning..")
	template = loader.get_template("index.htmlt")
	c = RequestContext(request, {"todo": Item.objects.all()})

	return HttpResponse(template.render(c))

def done(request):
	# We're intentionally not doing anything along 
	for id_ in request.POST["mark_as_done"]:
		item = get_object_or_404(Item, pk=id_)
		item.done = True
		item.save()
	return HttpResponseRedirect("/")