from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eventplanner.models import Event
from datetime import datetime

from pprint import pprint

def plan_event(request):
    template = loader.get_template("eventplanner/plan_event.html")
    context = ""
    return HttpResponse(template.render(context, request))

def create_invite(request):
    template = loader.get_template("eventplanner/invite.html")
    

    new_event = Event(title=request.POST['title'], date=request.POST['date'], location=request.POST['location'], owner="TBD!")
    new_event.save()
    
    context = {
                  'title':request.POST['title'],
                  'date' :request.POST['date'],
                  'location':request.POST['location']
              }
    return HttpResponse(template.render(context, request))
