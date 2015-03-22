from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
import json
import datetime

def home(request):
	t = loader.get_template('hack4congress_index.html')
	f = sorted([x.strip() for x in open("/home/ec2-user/hack4congress/mysite/mysite/interests.txt").readlines()])
	c = Context({
		"interests" : f
		})
	return HttpResponse(t.render(c))

def result(request):
	interest = request.GET['id']
	with open('/home/ec2-user/hack4congress/mysite/mysite/i2s.json') as i2s_file:
		i2s = json.load(i2s_file)
		result = [x.strip() for x in i2s[interest]]
	t = loader.get_template('hack4congress_results.html')
	result = sorted(result, key=lambda x:-x.influence)
	c = Context({"interestname":interest, "res":result})
	return HttpResponse(t.render(c))