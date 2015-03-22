from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
import datetime

def home(request):
	t = loader.get_template('hack4congress_index.html')
	f = open("interests.txt").readlines()
	c = Context({
		"interests" : f
		})
	return HttpResponse(t.render(c))

def result(request):
	interest = request.GET['id']
	with open('i2s.json') as i2s_file:
		i2s = json.load(i2s_file)
		result = i2s[interest]
	t = loader.get_template('hack4congress_results.html')
	c = Context(interest)
	return HttpResponse(t.render(c))