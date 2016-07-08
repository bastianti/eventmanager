from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eventplanner.models import Event
from eventplanner.models import User_Invite
from contacts.models import Group
from contacts.models import User
from datetime import datetime
import string
from random import sample, choice
from pprint import pprint

def plan_event(request):
    template = loader.get_template("eventplanner/plan_event.html")
    context = ""
    return HttpResponse(template.render(context, request))

def create_invite(request):
    template = loader.get_template("eventplanner/invite.html")
    new_event = Event(title=request.POST['title'], date=request.POST['date'], location=request.POST['location'], owner="TBD!")
    new_event.save()
    group_list = Group.objects.all()
    
    context = {
                  'title':request.POST['title'],
                  'date' :request.POST['date'],
                  'location':request.POST['location'],
                  'group_list':group_list,
                  'event_id':new_event.id
              }
    return HttpResponse(template.render(context, request))


def send_invite(userid, eventid):
    user = User.objects.filter(id=userid)
    event = Event.objects.filter(id=event_id)

    contact_method = user.first_commway

    text = "Du wurst von zu {0} eingeladen, bitte sage uns, ob du dabei bist:\n <a href="
    


def enter_invite_to_db(request):
    chars = string.letters + string.digits
    length = 20
    userid_list = request.POST.getlist("userid") 
    event_id = request.POST['event_id']
    event = Event.objects.filter(id=event_id)[0]
    for userid in userid_list:
        user = User.objects.filter(id = userid)[0]
        user_hash = ''.join(choice(chars) for _ in range(length))
        new_invite = User_Invite(tnstatus='0', user=user, event=event, user_hash=user_hash)
        new_invite.save()



    

        
    #Create unique link for yes and no
    #Get preferred user contact method
    #Send Link and Test to users
    #Show confirmation on screen


