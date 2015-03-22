from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
import datetime

def home(request):
	t = loader.get_template('hack4congress_index.html')
	c = Context()
	return HttpResponse(t.render(c))