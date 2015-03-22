from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
import datetime

def home(request):
	t = loader.get_template('hack4congress_index.html')
	c = Context()
	return HttpResponse(t.render(c))

def i2s_process(request):
	interest = request.GET['id']
	with open('i2s.json') as i2s_file:
		i2s = json.load(i2s_file)
		result = i2s[interest]
		return HttpResponse(result)

def result(request):
	t = loader.get_tempalate('hack4congress_results.html')
	c = Context()
	return HttpResponse(t.render(c))