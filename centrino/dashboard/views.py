import csv
import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import dashboard as dashboard_model, submitteddata
from .forms import dashboard as dashboard_form

def home(request):
	form = dashboard_form(
		request.POST or None,
		request.FILES or None
	)
	if form.is_valid():
		to_be_saved = []
		uploaded_file = csv.DictReader(request.FILES['csv'])
		for row in uploaded_file:
			to_be_saved.append(dashboard_model(**row))
		dashboard_model.objects.bulk_create(to_be_saved)
		return HttpResponseRedirect('/graph/')

	return render_to_response('home.html', {'form': form} , context_instance=RequestContext(request))

@csrf_exempt
def showgraph(request):
	if request.method == 'POST':
		data = json.loads(request.POST['data'])
		to_be_saved = []
		for eachdata in data:
			to_be_saved.append(submitteddata(x=eachdata[1],y=eachdata[2]))
		submitteddata.objects.bulk_create(to_be_saved)
		return HttpResponseRedirect('/')
	data = serializers.serialize('json', dashboard_model.objects.all())
	return render_to_response('graph.html', {'data':data}, context_instance=RequestContext(request))

